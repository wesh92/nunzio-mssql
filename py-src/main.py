"""
Console Application in Python
Used to connect to a MSSQL table and return the results as a CSV file in the current directory.

Author: Wes Hahn
Python Version: 3.9.5
Last Updated: 2022-10-03
"""

import pandas as pd
import sqlalchemy as sa
import tomli
from logging import log, WARNING, ERROR

class TomlHelper:
    """Helper class to read the config.toml file."""

    def __init__(self, file_path=r"nunzio-mssql\py-src\db_config.toml"):
        self.file_path = file_path

    def read(self):
        """Read the config.toml file and return the values as a dictionary."""
        with open(self.file_path, "rb") as f:
            return tomli.load(f)

class MSSQL:
    def __init__(self, server, database, user, password):
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.engine = sa.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server")
    
    # read a table from the database
    # save the results as a CSV file in the current directory
    def read_tables_to_csv(self, table_name, file_name):
        df = pd.read_sql_table(table_name, self.engine)
        df.to_csv(file_name, index=False)
        return f"File {file_name} created."
    
# create a console application
if __name__ == "__main__":
    try:
        config_filepath = input("Enter the FULL path to the config toml file: ")
        if config_filepath == "":
            config = TomlHelper().read()
        else:
            config = TomlHelper(config_filepath).read()
        if config:
            db_info = config["db_login"]
            table_and_files = config["db_exports"]["tables_and_files"]
            for i in range(len(table_and_files)):
                table_name = table_and_files[0][i]
                file_name = table_and_files[1][i]
                mssql = MSSQL(db_info["server"], db_info["database"], db_info["user"], db_info["password"])
                mssql.read_tables_to_csv(table_name, file_name)
                print(f"""File {file_name} created.\n
                    Exported {table_name} to {file_name}.""")
    except FileNotFoundError as fnf_error:
        log(ERROR, fnf_error)
        log(WARNING,"If you were expecting a config file, please create one in the same directory as this script.")
        log(WARNING, "The config file should be in TOML format. You can find more information here: https://learnxinyminutes.com/docs/toml/")
        log(WARNING, "Proceeding with user inputs below.")
        # take user input
        server = input("Enter the server name: ")
        database = input("Enter the database name: ")
        user = input("Enter the user name: ")
        password = input("Enter the password: ")
        table_name = input("Enter the table name: ")
        file_name = input("Enter the file name (not a path, just a name ending in .csv): ")
        # create an instance of the SQL class
        sql = MSSQL(server, database, user, password)
        # call the read_tables_to_csv method
        sql.read_tables_to_csv(table_name, file_name)
        print(f"""File {file_name} created.\n
            Exported {table_name} to {file_name}.""")
