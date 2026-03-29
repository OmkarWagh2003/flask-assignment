from flask import Flask, jsonify, render_template, request, redirect
import json
from pymongo import MongoClient

app = Flask(__name__)

# 🔴 Replace this later
client = MongoClient("mongodb+srv://waghomkar109_db_user:Omkar123@cluster0.o0devwt.mongodb.net/?appName=Cluster0")
db = client["testdb"]
collection = db["users"]

@app.route('/api')
def api():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect('/success')

    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)