# Tarvij

first install python package :
```
$ virtualenv env
```

Now install the python Packages :
```
$ pip install -r requirements.txt
```
Create the DB tables :
```
$ python database.py create
```
```
$ python main.py database create
```

if you need to drop the tables (careful if you drop the DB , all the tables will be lost):
```
$ python main.py database drop
```
if you need to recreate the table :
```
$ python main.py database recreate/
```