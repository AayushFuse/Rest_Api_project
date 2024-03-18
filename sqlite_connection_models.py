from conn import DatabaseConnection


class DatabaseOperations:
    def __init__(self) -> None:
        self.conn = DatabaseConnection().get_cursor()
        self.cursor = self.conn.cursor()

    def create_table(self, table_name: str):
        query = f"""CREATE TABLE {table_name} (
                    ID INT PRIMARY KEY NOT NULL,
                    NAME CHAR(20) NOT NULL,
                    ROLL CHAR(20) NOT NULL,
                    ADDRESS CHAR(50),
                    CLASS CHAR(20))"""

        self.cursor.execute(query)

    def insert_records(self,id,name,roll,address,p_class):
        query = (
            "INSERT INTO STUDENT (ID,NAME,ROLL,ADDRESS,CLASS)"
            "VALUES (:ID, :NAME, :ROLL, :ADDRESS, :CLASS);"
        )
        params = {
            "ID": id,
            "NAME": name,
            "ROLL": roll,
            "ADDRESS": address,
            "CLASS": p_class,
        }

        self.cursor.execute(query, params)
        self.conn.commit()

    def get_records(self):
        query = "SELECT * FROM STUDENT"
        return self.cursor.execute(query).fetchall()


db = DatabaseOperations()
db.create_table('STUDENT')
db.insert_records(1,"Aayush",9,"Dhapasi",2)
db.insert_records(2,"Abhishek",10,"Tokyo",1)
print(db.get_records())