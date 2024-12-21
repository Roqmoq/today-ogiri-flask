from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        # MySQLに接続
        connection = mysql.connector.connect(
            host="db",  # docker-compose.ymlで定義したサービス名
            user="root",
            password="password",
            database="test_db"
        )
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()
        return f"Tables: {tables}"
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
