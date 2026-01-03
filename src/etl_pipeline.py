from datetime import datetime
from extract import extract
from transform import transform
from load import load_to_csv, load_to_db
import pandas as pd
import sqlite3

csv_file_path = 'data/processed/Countries_by_GDP.csv'
db_name = 'World_Economies.db'
conn = sqlite3.connect(db_name)
table_name = 'Countries_by_GDP'
log_file = 'logs/etl_project_log.txt' 
URL = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'

def log_progress(message):
    time_format = '%Y-%h-%d-%H:%M:%S'
    now  = datetime.now()
    timestamp = now.strftime(time_format)
    with open(log_file, 'a') as log_f:
        log_f.write(timestamp + ',' + message + '\n')

def run_query(query_statement, sql_connection):
    # display only the entries with more than a 100 billion USD economy
    query_output = pd.read_sql(query_statement, sql_connection)
    print('query_statement: ', query_statement)
    print('query_output: \n', query_output)


if __name__ == "__main__":
    # Log the initialization of the ETL process 
    log_progress('ETL Initiated')

    # Extraction phase
    log_progress('Extraction Phase Initiated')
    extraction = extract(URL)
    log_progress('Extraction Phase Ended')

    # Transform phase 
    log_progress('Transformation Phase Initiated')
    transformation = transform(extraction)
    log_progress('Extraction Phase Ended')

    # loading Phase
    log_progress('CSV Loading Phase Initiated')
    load_to_csv(transformation, csv_file_path)
    log_progress('CSV Loading Phase Ended')

    log_progress('DB Loading Phase Initiated')
    load_to_db(transformation, table_name, conn)
    log_progress('CSV Loading Phase Ended')

    # Log the completion of the ETL process 
    log_progress("ETL Ended") 

    #run_query in terminal
    query = f'SELECT * FROM {table_name} WHERE GDP_USD_billions >= 100'
    run_query(query, conn)

