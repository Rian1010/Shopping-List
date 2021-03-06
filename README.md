# Shopping-List 
This project is a web application that was made for users to list up the products, which they have to purhase, into one online-shopping-list. It is a responsive app, which can be used on multiple devices. Click [here](http://shopping-list-google.herokuapp.com/) to go to the Heroku link.

## Installations
### How to Install Flask:
- $ sudo pip3 install flask

### Connection Python to MongoDB:
- $ sudo pip3 install flask-pymongo
- $ npm install bson-objectid

### Install dnspython
- $ sudo pip3 install dnspython

### Install Heroku:
- $ brew tap heroku/brew && brew install heroku

## Deployment onto Heroku
### Install Homebrew:
- $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
- $ heroku login
- $ git init
### The Github repository gets initialised through git init
- $ pip3 freeze --local > requirements.txt
- $ touch Procfile
### A Procfile indicates to Heroku, which file is supposed to be used to run the application
- $ git add .
###  Each file gets added through git add .
- $ git commit -m ""
- $ heroku git:remote -a shopping-list-google
- $ git push heroku master
### Run the application on Heroku by using the following line:
- $ heroku ps:scale web=1

## Technologies
- HTML5
- Bootstrap v4.1.3
- CSS3
- Python
- Flask
- Pymongo
- MongoDB
- Git, GitHub and Heroku

## Process

### My First Step After Installing Everything
A basic design for the website was required, so I made a wireframe. I used yellow for the navigation bars and footer because I find that it fits to the shopping theme and I added purple elements too, as purple fits well together with yellow.

I started to get the basic functionalities for the shopping-list done, through CRUD (Create, Read, Update and Delete), which I have learned from my online course. So, I made a shopping-list that could insert, edit and delete items, but it would be visible to anyone entering the page. So, I started working on a registration and login functionality.

### Attempts of Including Login and Registration Functionalities
At first, I intended to make login and registration functionalities with passwords that would be hidden in the database. So I watched a tutorial by a YouTuber called [Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE), who uses bcrypt to do it. But after trying out his code and researching about it, I could not make it work properly, as it would register someone, but not sign them in. Due to the fact that it was consuming lots of time, I decided to use the way I learned from my online course of how to add these utilities onto a website. Therefore, I only used flask and pymongo for it in the app.py file. However, I had only learned how to create different users, while having their information be visible to other accounts, so I had to find a way to enable each user to have their own shopping-list, that no one else could view or edit.

### Creating One Shopping-List for Each Account
The way I solved the problem of one shopping-list being visible to everyone, was to set an 'owner' in the collection for the shopping-list-items, called 'itemName'. The 'owner' would be equal to the entered email-address, which would be inserted into the collection called 'account', through the registration or login. If the session contains the same email, as set to the 'owner' in the 'itemName' collection, then the user can view the details of the shopping-list in the 'itemName' collection. 

## Challenges
The biggest challenge for me was to enable each user to have a shopping-list, which only they could view because I had never done that before. Espacially for this part, I got many errors, which I solved with time by going through the code in the app.py file and the HTML templates. 

At first, I was going to have a limited amount of items that could be edited. Once one would login, the user should get a set amount of empty values for item names and their quantity, which one should edit in order to create one's own shopping-list. Here is an example of what I had done, in the code below:
```python
    itemName = mongo.db.itemName
    itemName.insert_one({
        'owner': session['email'],
        'itName': "",
        'amount': "",
        'itName2': "",
        'amount2': ""
    })
```
As a result, I had removed the insertion functionality for new items. However, the problem was that the amount of empty strings I had set, like in the example above, would be added over and over again, after each time a user would login. So, I moved that part of the code to the registration route instead, so that that set amount of values for the items and quantity would appear only once after a user's registration. Then, the problem was that, if one deleted a shopping-list, one could never get it back. As a result, I decided to include the functionality of adding individual shopping-list-items back again. Throughout the process of coding again, I connected the 'owner' with the session['email] for the shopping-list information to be added to the corresponding accounts on MongoDB. So, that is when I noticed this pattern of having to include this following line of code, among the other strings in the collection, to the routes for insertions and updates: 
```python
'owner': session['email'],
```

Therefore, I managed to finish the web application, which now has editable shopping-lists that persist between logins. Finally, I worked on the last touches of the design of the website and uploaded it onto Heroku and Github. 

## Tests
- Used print() to check what sessions got passed through when a user logged in or registered and if variables were picking up the correct information
- Tested out the functionalities of each insertion, update, deletion, login and registration myself by creating multiple accounts and making different shopping-lists on each one
- Checked the responsiveness of the site on the Chrome DevTools, my deskop and my phone

## Resources
- Cover picture of the homepage is from: [Pixabay](https://pixabay.com/de/photos/einkaufswagen-shopping-laptop-4516039/)
- Cover picture on the Shopping-List Page is from: [Pixabay](https://pixabay.com/de/photos/einkaufswagen-einkaufen-shopping-1080840/)
- Colouring the navbar: [Bootstrap](https://getbootstrap.com/docs/4.0/components/navbar/)
- About a Login Functionality: 
    - [programcreek](https://www.programcreek.com/python/example/58659/werkzeug.security.check_password_hash)
    - [The online course that I am currently doing](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/course/)
    - First try for login and registration [YouTube Video by Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE)
- About a Logout Functionality: [BogoToBogo](https://www.bogotobogo.com/python/Flask/Python_Flask_Blog_App_Tutorial_2.php)
- About lask and its for loops:
[ANSIBLE](https://ansiblemaster.wordpress.com/2016/07/27/jinja2-using-loop-index-and-loop-length-examples-etchosts-and-workers-properties/)


