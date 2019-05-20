import cx_Oracle
import pandas as pd

class Connector:

    def __init__(self, config):
        ip = config["ip"]
        port = config["port"]
        user = config["user"]
        password = config["password"]
        tnsname = config["tnsname"]

        try:
            self.connection = cx_Oracle.connect(
                user + '/' +
                password + '@' +
                ip + ':' +
                port + '/' +
                tnsname)
        except Exception as e:
            content = (tnsname + ' is Unreachable,The reason is ' + str(e)).strip()
            print(content)
        else:
            self.cursor = self.connection.cursor()

    def executeDataFrame(self, sql):
        return pd.read_sql(sql=sql, con=self.connection)