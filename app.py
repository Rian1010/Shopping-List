import os
import bcrypt
from flask import Flask, render_template, session, url_for, request, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__, template_folder='template')
app.config["MONGO_DBNAME"] = 'myFirstCluster'
app.config["MONGO_URI"] = 'mongodb+srv://Rian:j4JWQ1Ntzc9u0U7m@myfirstcluster-ges2b.mongodb.net/shopping-list?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'

mongo = PyMongo(app)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')

    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.user
    user_login = users.find_one({'name' : request.form['username']})

    if user_login:
        if bcrypt.hashpw(request.form['pass'].encode['utf-8'], user_login['password'].encode('utf-8')) == user_login['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index.html'))
    return 'Invalid username or password'


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        user_exists = users.find_one({'name': request.form['username']})

        if user_exists is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'The username that you have entered already exists!'

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('signin')

@app.route('/shoppingList')
def shoppingListName():
    listName = mongo.db.listName.find()
    return render_template('index.html', listName=listName)

@app.route('/listItem')
def listItem():
    itemName = mongo.db.itemName.find()
    return render_template('index.html', itemName=itemName)

@app.route('/addShoppingList')
def addShoppingList():
    listName = mongo.db.listName.find()
    return render_template('addShoppingList.html', listName=listName)

@app.route('/addItem')
def addItem():
    itemName = mongo.db.itemName.find()
    return render_template('addItem.html', itemName=itemName)

@app.route('/updateListName/<list_id>', methods=['POST'])
def updateListName(list_id):
    listName = mongo.db.listName.find()
    listName.update({'_id': ObjectId(list_id)})
    return redirect(url_for('shoppingListName'))

@app.route('/updateItemName/<item_id>', methods=['POST'])
def updateItemName(item_id):
    itemName = mongo.db.itemName.find()
    itemName.update({'_id': ObjectId(item_id)})
    return redirect(url_for('shoppingListName'))

@app.route('/insertList', methods=['POST'])
def insertList():
    listName = mongo.db.listName
    listName.insert_one(request.form.to_dict())
    return redirect(url_for('shoppingListName'))

@app.route('/insertItem', methods=['POST'])
def insertItem():
    itemName = mongo.db.itemName
    itemName.insert_one(request.form.to_dict())
    return redirect(url_for('shoppingListName'))

@app.route('/editList/<list_id>')
def editList(list_id):
    listName = mongo.db.listName.find_one({"_id": ObjectId(list_id)})
    return render_template('editShoppingList.html', listName=listName)

@app.route('/editItem/<item_id>')
def editItem(item_id):
    itemName = mongo.db.itemName.find_one({"_id": ObjectId(item_id)})
    return render_template('editListItem.html', itemName=itemName)

@app.route('/deleteList/<list_id>')
def deleteList(list_id):
    mongo.db.remove({"_id": ObjectId(list_id)})
    return redirect(url_for('shoppingListName'))

@app.route('/deleteItem/<item_id>')
def deleteItem(item_id):
    mongo.db.remove({"_id": ObjectId(item_id)})
    return redirect(url_for('shoppingListName'))

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)