## Connection Python to MongoDB
- sudo pip3 install flask-pymongo
- sudo pip3 install dnspython

## How to Install Flask
- sudo pip3 install flask

## Deployment onto Heroku
- Install Homebrew
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

- Install Heroku
brew tap heroku/brew && brew install heroku

- Login to Heroku 
heroku login

## Deployment to Heroku
$ heroku login
$ git init
$ heroku git:remote -a shopping-list-google
$ git add .
$ git commit -am "make it better"
$ heroku git:remote -a shopping-list-google


$ pip3 freeze --local > requirements.txt
Create Procfile:
$ touch Procfile


- Homepage banner image from: https://pixabay.com/de/photos/einkaufswagen-shopping-laptop-4516039/
- Colouring the navbar: https://getbootstrap.com/docs/4.0/components/navbar/
- Login: https://www.programcreek.com/python/example/58659/werkzeug.security.check_password_hash
- Logout: https://www.bogotobogo.com/python/Flask/Python_Flask_Blog_App_Tutorial_2.php

