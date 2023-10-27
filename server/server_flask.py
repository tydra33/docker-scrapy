import psycopg2
from flask import Flask, render_template


app = Flask(__name__)

db_config = {
    "host": "127.0.0.1",
    "port": "5432",
    "database": "flats_db",
    "user": "postgres",
    "password": "ardit33",
}


@app.route("/")
def index():
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM flat")
    data = cursor.fetchall()

    conn.close()
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
