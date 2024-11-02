import mysql.connector


class Database:
    def __init__(self):
        self.user = "root"
        self.password = ""
        self.host = "localhost"
        self.database = "my_note"
        self.integrity_error = mysql.connector.errors.IntegrityError

        self.connection = mysql.connector.connect(
            user=self.user, password=self.password, host=self.host)

        self.cursor = self.connection.cursor()

        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
        self.connection.commit()
        self.cursor.execute(f"USE {self.database}")

    def create_table(self):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS user_info (id INTEGER PRIMARY KEY AUTO_INCREMENT, "
                            f"email VARCHAR(100) UNIQUE, password VARCHAR(10))")
        self.connection.commit()

    def create_note_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS deleted_notes (email VARCHAR(50), note VARCHAR(1000))")
        self.connection.commit()


# Database().create_table()
Database().create_note_table()
