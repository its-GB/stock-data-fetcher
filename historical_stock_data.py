import requests
import csv
from datetime import datetime
from config import read_config
from database import create_database, insert_data, commit_and_close
from utils import get_companies

# Read configuration file
config = read_config()

# Get values from the configuration file
api_key = config.get('common', 'api_key')
db_file = config.get('database', 'db_file')
historical_url = config.get('api', 'historical_url')
start_date = datetime.strptime(config.get('historical', 'start_date'), '%Y-%m-%d')
end_date = datetime.strptime(config.get('historical', 'end_date'), '%Y-%m-%d')

# Create the SQLite database and table
conn, c = create_database(db_file)

# Fetch data for each company
for company_name, symbol in get_companies(config):
    # Fetch historical data
    url = historical_url.format(symbol=symbol, api_key=api_key)
    response = requests.get(url)

    # Skip header row
    next(csv.reader(response.text.splitlines(), delimiter=','))

    # Process data rows
    for row in csv.reader(response.text.splitlines(), delimiter=','):
        try:
            date = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            continue

        if start_date <= date <= end_date:
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

print(f'Historical data saved to {db_file}')