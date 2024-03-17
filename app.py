from flask import Flask, request, render_template
import pymysql.cursors
app = Flask(__name__)

# Configure database connection
connection = pymysql.connect(
    host='your_host',
    user='your_user',
    password='your_password',
    db='your_database',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Define a route for fetching hospital data
@app.route('/get_hospitals', methods=['POST'])
def get_hospitals():
    try:
        with connection.cursor() as cursor:
            # Fetch hospitals for the given speciality ID (9 in this case)
            speciality_id = request.form['specialityId']
            sql = f"SELECT * FROM hospitals WHERE speciality_id = {speciality_id}"
            cursor.execute(sql)
            hospitals = cursor.fetchall()

        return render_template('hospital_list.html', hospitals=hospitals)

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
