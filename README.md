# flask-skeleton-sqlalchemy-migrate-login

This repository provides a skeleton for starting new Flask Project. All the commit messages indicate the progress and dependecies added over time.

>How to start with it?

You have already started! Download and move into repository

First create a virtual environement. Surf over internet and install it . Then

```
$ virtualenv venv
$ . venv/bin/activate

```
Now install requirements
```
$ pip install -r requirements.txt
```

> It has Flask_sqlalchemy, flask_migrate, Blueprints and flask_login

Name is confusing catalog contains a route to login_user and auth is just for checking it.

> How to use Flask_sqlalchemy on CLI

Way 1:(Showing insertion)
```
>>> from app import db
>>> from app import create_app
>>> fap=create_app('dev')
>>> app_ctx=fap.app_context()
>>> app_ctx.push()
>>> db.create_all()
>>> from app.catalog.models import Publication
>>> pb=Publication(name='Oxford')
>>> db.session.add(pb)
>>> db.session.commit()
>>> app_ctx.pop()
```

Way 2: 
```
$export FLASK_APP=run.py
$flask shell (gives u 'app' directly)
>>> from app.catalog.models import Publication
>>> pb=Publication(name='Gita Press')
>>> from app import db
>>> db.session.add(pb)
>>> db.session.commit()
```

>How to use Flask_Migrate

```
Flask Migrate tutorial https://www.youtube.com/watch?v=IxCBjUapkWk
its quite simple now just put
$ flask db
$ flask db init -> creates a repository which contains script
$ flask db migrate -> creates script by watching models
$ flask db updgrade -> does the magic
$ flask db stamp head -> to tell migration that it is updated Now.
```
You can read commit messages and comments also for help.

>How to run it?

```
$ export FLASK_APP=run.py
$ flask run
```
or simply
```
$ python run.py
```
You can switch over environments too.!! 'dev' is default. 
```
$ export FLASK_ENV=dev
```
Uses sqlite3. So:
```
$ sudo apt install sqlite3
$ sqlite3 app.db (only is db.create_all() is called )
(venv) mohit:~/MyProjects/Flask (master) $ sqlite3 app.db
SQLite version 3.22.0 2018-01-22 18:45:57
Enter ".help" for usage hints.
sqlite> .tables
alembic_version  book             funny            publication    
sqlite> select * from funny;
1|1234|manna|1
2|1234|mohit|1
sqlite> select * from publication;
1|Oxford|
2|Gita Press|
sqlite> select * from book;
sqlite> .quit
```

Thanks !!
