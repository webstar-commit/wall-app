# Wall App | Simple Django App 

## Getting Started

These instructions will get you a copy of the project up and running.


### Installing

##### Make your python env and install requirements:

```
$ python3 -m venv env
$ source env/bin/activate 
$ git clone git@github.com:mahmoudadev/wall-app.git
$ cd wall-app
$ pip3 install -r requirements.txt
```


- First, run the following command to have your `.env` file
```
cp .env.example .env
```
 and Then by any text editor open `.env` and set up your _local settings_

- Make sure your Email server credentials set correctly, then run the following commands

```
$ python manage.py migrate
$ python manage.py runserver
```
- Finally, you can navigate to `localhost:8000/`

create an account and post on the wall. 

##### Main API's endpoints:
```
    GET   /api/v1/posts/
    POST  /api/v1/posts/create

```

- I have created also `login` and `register` API's endpoint. in case we need to integrate with 
mobile application or desktop software.

so here are the auth endpoints:
```
    POST  /api/v1/auth-rest/login/
    PoST  /api/v1/auth-rest/registration/
    POST  /api-token-auth/
```


Thank you!
