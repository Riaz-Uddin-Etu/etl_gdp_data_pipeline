def load_to_csv(df, file_path):
    df.to_csv(file_path)

def load_to_db(df, sql_table_name, sql_connection):
    df.to_sql(sql_table_name, sql_connection, if_exists = 'replace', index = False)