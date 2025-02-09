# MySQL Default Credentials Checker

A Python script to connect to a MySQL database using default credentials read from a file.

## Prerequisites

- Python 3.x
- `mysql-connector-python` package

## Installation
1. Clone this repository:
   ```bash
    git clone https://github.com/josemlwdf/MySQL-default-credentials
    ```

2. Install the dependencies using the following command:

    ```bash
    sudo pip install -r requirements.txt --break-system-packages
    ```

## Usage

1. Ensure that you have a file named `default_db_credentials1.txt` in the same directory as the script. This file should contain the default credentials in the format `user:password`, each on a new line.

2. Run the script with the following command:

    ```bash
    python3 MySQL_default_creds.py <ip> <port>
    ```

## Note

This script attempts to connect to a MySQL server using default credentials read from a file. Use this script responsibly and only on systems where you have permission to perform such actions.
