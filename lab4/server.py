from flask import Flask, render_template, request
from main import Psql

app = Flask(__name__)

psql = Psql('postgres',
            dbname='lab4base',
            user='postgres',
            host='localhost',
            port="5430"
            )


@app.route("/", methods=['post', 'get'])
def table_display():
    if request.method == 'POST':
        command = request.form.get('command')
        message = psql.execute(command)
        return render_template("response.html", command=command, message=message)

    table_list = psql.execute(
        "SELECT table_name FROM information_schema.tables WHERE (table_schema = 'public') ORDER BY table_name;")
    data = {}
    for table in table_list:
        table_data = psql.get_table_data(table[0])
        data.update({table[0]: table_data})

    return render_template("main.html", data=data)


app.run()
