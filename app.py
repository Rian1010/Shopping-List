import os
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = session.get('email-address')

    if request.method == 'POST':
        email = request.form["email-address"]
        password = request.form['pass']
        acc = mongo.db.account.find_one({"email-address": email})
        print(email, password, acc)
        if mongo.db.account.find_one({"email-address": email}) and mongo.db.account.find_one({"pass": password}):
            session['email'] = acc['email-address']
            return render_template('index.html')
        else:
            return 'Invalid email or password'

    return render_template('login.html')

# First try
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     users = mongo.db.user
#     user_login = users.find_one({'name' : request.form['username']})

#     if user_login:
#         if bcrypt.hashpw(request.form['pass'].encode['utf-8'], user_login['password'].encode('utf-8')) == user_login['password'].encode('utf-8'):
#             session['name'] = request.form['username']
#             return redirect(url_for('index.html'))
#     else:
#         flash(f'Invalid username')         
#     return 'Invalid username or password'

@app.route('/register', methods=['POST', 'GET'])
def register():
    email = session.get('email-address')

    if request.method == 'POST':
        email = request.form['email-address']
        password = request.form['pass']
        account = {'email-address': email, 'pass': password}

        if mongo.db.account.find_one({'email-address': email}):
            return 'User already exists.'
        else:
            mongo.db.account.insert_one(account)
            session['email'] = request.form['email-address']
            return render_template('index.html', account=account, password=password)

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('login')

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

@app.route('/updateListName/<list_id>', methods=['GET','POST'])
def updateListName(list_id):
    listName = mongo.db.listName
    listName.update({'_id': ObjectId(list_id)},
                    {
            'listName': request.form.get('listName'),
    })
    return redirect(url_for('shoppingListName'))

@app.route('/updateItemName/<item_id>', methods=['GET', 'POST'])
def updateItemName(item_id):
    itemName = mongo.db.itemName
    itemName.update({'_id': ObjectId(item_id)})
    return redirect(url_for('shoppingListName', itemName=itemName))

@app.route('/insertList', methods=['GET', 'POST'])
def insertList():
    listName = mongo.db.listName
    listName.insert_one({
            'listName': request.form.get('listName'),
    },)
    return redirect(url_for('shoppingListName'))

@app.route('/insertItem', methods=['GET', 'POST'])
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
    mongo.db.listName.remove({"_id": ObjectId(list_id)})
    mongo.db.itemName.remove({"_id": ObjectId(list_id)})
    return redirect(url_for('shoppingListName'))

@app.route('/deleteItem/<item_id>')
def deleteItem(item_id):
    mongo.db.itemName.remove({"_id": ObjectId(item_id)})
    return redirect(url_for('shoppingListName'))

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
        port=os.environ.get('PORT'),
        debug=True)