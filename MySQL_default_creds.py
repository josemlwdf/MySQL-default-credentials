import mysql.connector
import sys
import threading

def def_cred():
    """
    A function to get default credentials for db access.
    """
    with open("default_db_credentials1.txt", "r") as fp:
        def_db_val = fp.read()
    return def_db_val.splitlines()

def connect_mysql_ip_port(ip, port, user="", passwd=""):
    """
    A function to connect ip for that port.
    """
    try:
        mysql.connector.connect(host=ip,
                                user=user,
                                password=passwd,
                                port=port,
                                connection_timeout=10)
        print(f"[+] Credentials Found: {user}:{passwd}")
    except:
        pass

def connect_db(ip, port, _connect_mysql_ip_port):
    """
    Function to connect MySQL db with default cred
    """
    for row in def_cred():
        user, passwd = row.split(':')
        try:
            t1 = threading.Thread(target=connect_mysql_ip_port, args=(ip, port, user, passwd))
            t1.start()
        except:
            pass
		   
def main(ip, port):
    """
    Start of Script.
    """
    connect_db(ip, port, connect_mysql_ip_port)

if __name__ == "__main__":
    if len(sys.argv) != 3:
      sys.exit("Usage: python3 MySQL_default_creds.py ip port")
    main(sys.argv[1], int(sys.argv[2]))
