# pizza-restaurant-api
## Setup

We'll build up our Flask application from a few models and views that are ready
to go. Run these commands to install the dependencies and set up the database:

```console
$ pipenv install; pipenv shell
$ cd server
$ flask db init
$ flask db migrate -m 'initial migration'
$ flask db upgrade head
$ python seed.py
$ export FLASK_APP=app.py
$ export FLASK_RUN_PORT=5555
```

You can view the models in the `server/models.py` module, and the migrations in
the `server/migrations/versions` directory. 

Then, run the server:

```console
$ python app.py
```

With that set up, let's work on getting Flask and SQLAlchemy working together!

---
## 📂 Project Structure