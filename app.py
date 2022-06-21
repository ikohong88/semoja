from flask import Flask, redirect, render_template, request, jsonify, url_for, app
# from pymongo import MongoClient
# JWT와 관련 여부 확인 필요
# from dotenv import load_dotenv
import os

# Flask
app = Flask(__name__)

# .env
# load_dotenv()
# ID = os.environ.get('DB_ID')
# PW = os.environ.get('DB_PW')


#index handler start
@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)