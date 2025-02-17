# Stock Data Fetcher

This project fetches historical and daily stock data for the top 10 Indian companies by market capitalization and stores it in a SQLite database.

## Features

- Fetches historical stock data for a specified date range
- Fetches daily stock data for the previous day
- Stores the data in a SQLite database
- Configurable via a `config.ini` file
- Modular design with separate modules for configuration, database operations, and data fetching

## Prerequisites

- Python 3.x
- `configparser` and `sqlite3` libraries (listed in `requirements.txt`)

## Installation

1. Clone the repository:

   git clone https://github.com/its-GB/stock-data-fetcher.git

2. Change to the project directory:

   cd stock-data-fetcher

3. Create a virtual environment (optional but recommended):

   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

4. Install the required libraries:

   pip install -r requirements.txt

## Configuration

1. Update the `config.ini` file with your AlphaVantage API key and the desired companies:

[common]
api_key = YOUR_API_KEY
companies =
    Reliance Industries Limited,RELIANCE.BSE
    Tata Consultancy Services Limited,TCS.BSE
    HDFC Bank Limited,HDFCBANK.BSE
    Infosys Limited,INFY.BSE
    ICICI Bank Limited,ICICIBANK.BSE
    Hindustan Unilever Limited,HINDUNILVR.BSE
    State Bank of India,SBI.BSE
    Bharti Airtel Limited,BHARTIARTL.BSE
    Life Insurance Corporation of India Limited,LIC.BSE
    ITC Limited,ITC.BSE

2. Specify the start and end dates for the historical data in the `config.ini` file:

[historical]
start_date = 2020-01-01
end_date = 2024-05-31

3. Set the SQLite database file name in the `config.ini` file:

[database]
db_file = stock_data.db

## Usage

1. Run the `historical_stock_data.py` script to fetch and store the historical stock data:

   python historical_stock_data.py

   This script fetches the historical data for the specified date range and saves it to the SQLite database.

2. Run the `daily_stock_data.py` script to fetch and store the daily stock data for the previous day:

   python daily_stock_data.py

   This script fetches the daily data for the previous day and saves it to the SQLite database.

The data will be saved to the specified SQLite database file (default: `stock_data.db`).

## Running the Stock Data Queries
1. Prerequisites

   - Ensure you have SQLite installed on your system.
   - Ensure you have a Python environment set up with the necessary dependencies for running the historical_stock_data.py or daily_stock_data.py script.

2. Steps

    1. Run the Python script to populate the stock_data.db database:
        - Run either the historical_stock_data.py or daily_stock_data.py script to populate the stock_data.db SQLite database file with the stock data. This will create the stock_data.db file if it doesn't already exist.
    2. Run the queries using a SQLite UI tool:
        - Open a SQLite UI tool like DB Browser for SQLite or SQLiteStudio.
        - Connect to the stock_data.db database file.
        - Click on the "Execute SQL" button or menu option to open the SQL editor.
        - Open the `sql_queries.sql` file and copy the contents.
        - Paste the queries into the SQL editor.
        - Click the "Execute" button to run the queries against the stock_data.db database.
    3. View the query results:
        - The query results will be displayed in the SQLite UI tool's results pane.
        - You can save the query results to a file or export them to a CSV format for further analysis.


## Project Structure

- `config.py`: Handles reading the configuration from the `config.ini` file.
- `database.py`: Provides functions for creating the SQLite database and table, inserting data, and managing the database connection.
- `utils.py`: Contains utility functions, such as getting the list of companies and the previous day's date.
- `historical_stock_data.py`: Fetches and stores the historical stock data.
- `daily_stock_data.py`: Fetches and stores the daily stock data for the previous day.

