import sqlite3


class Db:
    def __init__(self, path):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def execute(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

    def __del__(self):
        self.close()
