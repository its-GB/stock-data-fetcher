import requests
import csv
from config import read_config
from database import create_database, insert_data, commit_and_close
from utils import get_companies, get_yesterday

# Read configuration file
config = read_config()

# Get values from the configuration file
api_key = config.get('common', 'api_key')
db_file = config.get('database', 'db_file')
daily_url = config.get('api', 'daily_url')

# Create the SQLite database and table
conn, c = create_database(db_file)

# Fetch data for each company
for company_name, symbol in get_companies(config):
    # Fetch daily data for the previous day
    url = daily_url.format(symbol=symbol, api_key=api_key)
    response = requests.get(url)

    # Skip header row
    next(csv.reader(response.text.splitlines(), delimiter=','))

    # Process data rows
    yesterday = get_yesterday()
    for row in csv.reader(response.text.splitlines(), delimiter=','):
        if row[0] == yesterday:
            data = (
                row[0],
                company_name,
                float(row[1]),
                float(row[4]),
                float(row[2]),
                float(row[3]),
                int(row[5])
            )
            insert_data(c, data)

commit_and_close(conn)

print(f'Daily data saved to {db_file}')
