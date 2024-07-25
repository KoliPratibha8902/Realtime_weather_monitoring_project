from flask import Flask, jsonify, render_template
import pymysql.cursors
from datetime import datetime, timedelta

app = Flask(__name__)

# Your MySQL database connection details
db_connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='D@8sep2002',
    database='weather',
    cursorclass=pymysql.cursors.DictCursor
)

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch data for the charts
@app.route('/data')
def get_data():
    try:
        with db_connection.cursor() as cursor:
            # Get the current time and calculate a time threshold (e.g., 1 hour ago)
            current_time = datetime.now()
            time_threshold = current_time - timedelta(hours=1)

            # Execute the MySQL query to fetch specific columns for records within the time threshold
            query = '''
                SELECT city, time_local, humidity, temperature, wind_speed, pressure, cloudcover
                FROM weatherdata
                WHERE time_local >= %s
                ORDER BY time_local DESC
                LIMIT 4
            '''

            cursor.execute(query, (time_threshold,))
            data = cursor.fetchall()

        return jsonify(data)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to fetch data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
