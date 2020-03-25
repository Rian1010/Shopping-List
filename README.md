# Shopping-List 
This project is a web application that was made for users to list up the products that they need to purhase into one online shopping-list. It is a responsive app, which can be used on multiple devices. Click [here](http://shopping-list-google.herokuapp.com/) to get to the link to the Heroku link.

## Installations
### How to Install Flask:
- sudo pip3 install flask

### Connection Python to MongoDB:
- sudo pip3 install flask-pymongo
- sudo pip3 install dnspython

- Install Heroku:
brew tap heroku/brew && brew install heroku

### Deployment onto Heroku
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

## Tools
- HTML
- Bootstrap 4
- CSS
- Python
- Flask
- Pymongo
- MongoDB

## Process

### My First Step After Installing Everything
A basic design for the website was required, so I made a wireframe. I used yellow for the navigation bars and footer because I find that it fits to the shopping theme and I added purple elements too, as purple fits well together with yellow.

I started to get the basic functionalities for the shopping-list done, through CRUD (Create, Read, Update and Delete), which I have learned from my online course. So, I made a shopping-list that could insert, edit and delete items, but it would be visible to anyone entering the page. So, I started working on a registration and login functionality.

### Attempts of Including Login and Registration Functionalities
At first, I intended to make login a registration functionalities with passwords that would be hidden in the database, so I watched a tutorial by a YouTuber called [Pretty Printed](https://www.youtube.com/watch?v=vVx1737auSE), who uses bcrypt to do it. But after trying out his code and researching about it, I could not make it work properly, as it would register someone, but not sign them in. Due to the fact that it was consuming lots of time, I decided to use the way I learned from my online course of how to add these utilities onto a website. Therefore, I only used flask and pymongo for it in the app.py file. However, I had only learned how to create different users, while having their information be visible to other accounts. So, I had to find a way to enable each user to have their own shopping-list, that no one else could view or edit.

### Creating One Shopping-List for Each Account
The way I solved the problem of one shopping-list being visible to everyone, was to set an 'owner' in the collection for the shopping-list-items, called 'itemName'. The 'owner' would be equal to the entered email-address through the registration or login, which would be inserted into the collection called 'account'. If the session contains the same email, as set to the 'owner' in the 'itemName' collection, then the user can view the details of the shopping-list in the 'itemName' collection. 

## Challenges
The biggest challenge for me was to enable each user to have a shopping-list, which only they can view, as I had never done that before. Espacially for this part, I got many errors, which I solved with time by going through the code in app.py and the HTML templates. 

At first, I was going to have a limited amount of items that could be edited. Once someone would login, they should get a set amount of empty item names and number of items, which they should edit in order to create their shopping-lists, such as in the code below:
    itemName = mongo.db.itemName
    itemName.insert_one({
        'owner': session['email'],
        'itName': "",
        'amount': "",
        'itName2': "",
        'amount2': ""
    })

As a result, I had removed the insertion functionality for new items. However, the problem was that the amount of empty strings I had set, like in the example above, would be added over and over again, after each time a user would login. So, I moved that part of the code to the registration route, so that that set amount of items and quantity values would appear only after a user's registration. Then, the problem was that, if one deleted a shopping-list, one could never get it back. As a result, I decided to include the functionality of adding individual shopping-list-items again. As I was coding it, I connected the 'owner' with the session['email] for the shopping-list information to be added to the corresponding accounts on MongoDB. So, that is when I noticed this pattern of having to include this following line of code among the other collection strings to insertions and updates: 
- 'owner': session['email'],

Therefore, I managed to finish this website, which now has editable shopping-lists, which persist between logins. Finally, I worked on the last touches of the design of the website and uploaded it onto Heroku and Github. 

## Tests
- Used print() to check what sessions got passed through when a user logged in or registered and if variables were picking up the correct information
- Tested out the functionalities of each insertion, update, deletion, login and registration myself by creating multiple accounts and making different shopping-lists on each one

## Resources
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


