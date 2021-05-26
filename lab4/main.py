import psycopg2


class Psql:

    def __init__(self, password, dbname='lab4base', user='postgres', host='localhost', port="5430"):
        self.conn = psycopg2.connect(dbname=dbname,
                                     user=user,
                                     password=password,
                                     host=host,
                                     port=port)

        self.cursor = self.conn.cursor()
        print('Connect Successed')

    def get_data_command(self):
        text = input("Input SQL command -->")
        self.cursor.execute(text)
        data = self.cursor.fetchall()
        print(data, tablefmt='orgtbl')

    def get_data_file(self):
        file_name = input("Paste absolute SQL file location -->")
        with open(file_name, "r") as f:
            for line in f.readlines():
                self.cursor.execute(line)
                data = self.cursor.fetchall()
                print(data, tablefmt='orgtbl')

    def execute(self, command):
        self.cursor.execute(command)
        data = self.cursor.fetchall()
        return data

    def get_table_data(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name};")
        colum_names = [desc[0] for desc in self.cursor.description]
        data = self.cursor.fetchall()
        return [colum_names, data]

    def __del__(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    psql = Psql('postgres',
                dbname='lab4base',
                user='postgres',
                host='localhost',
                port="5430")

    psql.get_data_file()
