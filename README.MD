python3 -m venv venv

source venv/bin/activate

pip install -r req.txt

python manage.py runserver

urls:
<<<<<<< HEAD
/auth/users
/auth/users/login
=======

/api/auth/registration

/api/auth/login

>>>>>>> 1cbd04f756e118dfc78c9093364474272e352417
/api/category

/api/product

login: pydev
password:123123

<<<<<<< HEAD

post to registration:
{
    "user": {
        "username": "user.username",
        "email": "user.email",
        "password": "user.password"
    }
}


output:
{
    "email": "user.username",
    "username": "user.login",
    "token": "user.token"
}


post to login:
{
    "user": {
        "email": "user.email",
        "password": "user.password"
    }
}


output:
{
    "user": {
         "email": "user.username",
         "username": "user.login",
         "token": "user.token"
    }
}
=======
admin panel - http://localhost:8000/admin
>>>>>>> 1cbd04f756e118dfc78c9093364474272e352417
