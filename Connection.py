from flask import Flask, render_template, request,session,redirect  ,jsonify
import psycopg2
from flask_session import Session
from json import dumps
from datetime import date
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.static_folder='static'
Session(app)
conn = psycopg2.connect(host='localhost', database='aravali',
                        user='postgres', password='ronit123')
cursor = conn.cursor()
user_id = 0


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/form')
def index():
    return render_template('Form.html')

@app.route('/thank')
def thank():
    return render_template('Thank.html')

@app.route('/form', methods=['post','get'])
def form():
    print("Hello")
    if request.method == 'POST':
        Village_name = request.form.get('village')
        Panchayat = request.form.get('Panchayat')
        Health_worker_name = request.form.get('worker')
        Block = request.form.get('block')
        Name = request.form.get('name')
        Age = request.form.get('age')
        Gender = request.form.get('Gender')
        Relative_name = request.form.get('Relative')
        Mobile_num = request.form.get('Mobile')
        VA_Right_Eye = request.form.get('right')
        VA_Left_Eye = request.form.get('left')
        Disease = request.form.get('Disease')
        Comments = request.form.get('Comment')
        cursor.execute('select count(*) from ba.blind')
        result = cursor.fetchone()
        count = result[0]+1
        print(result)
        insert_query = """ INSERT INTO ba.blind VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        try:
            record = (int(count), Village_name, Panchayat, Health_worker_name, Block, Name, int(Age), Gender, Relative_name, int(Mobile_num), VA_Right_Eye ,VA_Left_Eye, Disease, Comments)
            print(insert_query,record)
            cursor.execute(insert_query, record)
            conn.commit()
            count = cursor.rowcount
            print(count, "Record inserted successfully into Blind table")
            
        except:
            return "Invalid details"
    return render_template('Form.html')

if __name__ == '__main__':
    app.run(debug=True)
