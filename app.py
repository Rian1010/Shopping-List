import os
from flask import Flask, render_template, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__, template_folder='template')
app.config["MONGO_DBNAME"] = 'myFirstCluster'
app.config["MONGO_URI"] = 'mongodb+srv://Rian:j4JWQ1Ntzc9u0U7m@myfirstcluster-ges2b.mongodb.net/shopping-list?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return 'Hello ' + session['username']

    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/shopping-list.html')
def shopping_list():
    return render_template('shopping-list.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)