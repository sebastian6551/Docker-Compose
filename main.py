import pymysql

class DataBase:
    def __init__(self):
      self.connection = pymysql.connect(
        host = 'Localhost',
        user = 'root',
        password = '',
        db = 'composeBase'
      )

      self.cursor = self.connection.cursor()

    def get_hits(self):
      instruccion1 = 'UPDATE webExample SET hits = hits+1'
      instruccion2 = 'SELECT hits FROM webExample'

      try:
        self.cursor.execute(instruccion1)
        self.cursor.execute(instruccion2)
        hits = self.cursor.fetchone()
        print("Hello World! I have been seen", hits[0], "times.")
        self.connection.commit()
        self.connection.close()

      except Exception as exc:
        raise exc

database = DataBase()
database.get_hits()
