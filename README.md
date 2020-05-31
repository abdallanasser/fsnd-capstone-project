# fsnd-capstone-project
## Getting Started

### Installing Dependencies


#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Configuring the DB

For this project you'll have to setup a local postgresql DB and then complete the info about it on the [`models.py`](models.py) file.

## Example DB

For an example DB you can create manually using the following [`Example.txt`](example.txt)

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Sourcing setup.sh sets some environment variables used by the app.

Setting the FLASK_ENV variable to development will detect file changes and restart the server automatically.

Setting the FLASK_APP variable to app.py directs flask to use the this file to find the application.

## Avaible Endpoints

GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/


## API behavior and RBAC controls

The API has two roles

Roles:

manager:
    All permissions.

    (read:actors, read:movies, add:actor, change:actor, change:movie, delete:actor,  add:movie, delete:movie)

client:
    read:movies
    

## Testing Endpoints

### Includes tests demonstrating role-based access control:
To test the working endpoints please use the Postman collection provided: capstone-test-endpoints.postman_collection.json

### Includes at least one test for expected success and error behavior for each endpoint using the unittest library:
To test using unittest, make sure to have the backend runing, available data created on the db and from inside the backend folder, run:

```bash
python test_app.py;
```

## Heroku Link

The app has been deployed succesfully to Heroku with latest changes

URL: https://fsndcapstoneproject.herokuapp.com/
