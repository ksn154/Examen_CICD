from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS visits(
            id INT AUTO_INCREMENT PRIMARY KEY,
            visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        cursor.execute("INSERT INTO visits() VALUES()")
        conn.commit()

        cursor.execute("SELECT COUNT(*) FROM visits")
        count = cursor.fetchone()[0]

        cursor.close()
        conn.close()

        return f"Application works! Total visits: {count}"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)