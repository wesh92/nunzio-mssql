# nunzio-mssql
SQL to CSV Programs

-----------------
## Installation
1. Install [Python >=3.9](https://www.python.org/downloads/)
2. Ensure that Pip is installed by running `pip --version` in a terminal. If Pip is not installed, install it by running `python -m ensurepip` in a terminal.
3. Install the required packages by running `pip install -r requirements.txt` in a terminal in the project directory.
4. Go to `py-src` folder and ensure the information in db_config.toml is filled out.
5. Run the program by running `python main.py` in a terminal in the project directory.
6. If the console asks for the `db_config.toml` file, input the FULL path to the file.
7. The program will output the CSV files to the `csv` folder.

-----------------
### Notes
If the `db_config.toml` file is not found or you choose not to use it, the program will ask for the database information in the console.
This is intentional and will mean you can only select one DB/Table at a time to export.

If `pip` is not found, try running `python -m pip` instead.
If that does not work, ensure Python is installed and added to your PATH.
If `pip` is still giving you issues, try `pip3` instead.
