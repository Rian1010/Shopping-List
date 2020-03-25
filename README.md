
## How to Install Flask:
- sudo pip3 install flask

## Connection Python to MongoDB:
- sudo pip3 install flask-pymongo
- sudo pip3 install dnspython

- Install Heroku:
brew tap heroku/brew && brew install heroku

## Deployment onto Heroku
- Install Homebrew:
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ heroku login
$ git init
$ heroku git:remote -a shopping-list-google
$ git add .
$ git commit -m ""
$ heroku git:remote -a shopping-list-google


$ pip3 freeze --local > requirements.txt
Create Procfile:
$ touch Procfile


- Cover picture of the homepage is from: [Pixabay](https://pixabay.com/de/photos/einkaufswagen-shopping-laptop-4516039/)
- Cover picture on the Shopping-List Page is from: [Pixabay](https://pixabay.com/de/photos/einkaufswagen-einkaufen-shopping-1080840/)
- Colouring the navbar: [getbootstrap](https://getbootstrap.com/docs/4.0/components/navbar/)
- Login: 
    - [Program Creek](https://www.programcreek.com/python/example/58659/werkzeug.security.check_password_hash)
    -[The online course that I am currently doing](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/course/)
    - First try for login and registration [YouTube Video by Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE)
- Logout: [BogoToBogo](https://www.bogotobogo.com/python/Flask/Python_Flask_Blog_App_Tutorial_2.php)
- Flask for loops:
[Ansiblemaster](https://ansiblemaster.wordpress.com/2016/07/27/jinja2-using-loop-index-and-loop-length-examples-etchosts-and-workers-properties/)

##My First Step After Installing Everything
A basic design for the website was required. I used yellow for the navigation bars and footer because 

At first, I tried adding each shopping-list item separately:
@app.route('/insertItem/<owner_id>', methods=['GET', 'POST'])
def insertItem(owner_id):
    itemName = mongo.db.itemName
    itemName.insert_one({
        'owner': session['email'],
        'itName': request.form.get('itName'),
        'amount': request.form.get('amount')
    })
    return redirect(url_for('shoppingList'))
