# AA_backend

The backend for the AA project.\
A REST api running in python, using FastAPI and SQLite.

The database is stored in the file `database.db` in the root directory of the project.



## Development

Create new venv
```
python -m venv .venv
```

Activate venv (powershell)
```
.venv/Scripts/Activate.ps1
```

Exit venv by executing
```
deactivate
```
### Dependencies
Install all dependencies
```
$ pip install -r requirements.txt
```

Update  requirements.txt 
```
pip3 freeze > requirements.txt 
```

## Running server
Run the server
```
$ python -m uvicorn main:app
```

Run local server, but accessible over network
```
$ python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

## Testing

All tests are located in the `tests` directory.\
A test database is also included in this folder and is used for testing.

To test all the existing tests, run the following command in the root directory of the project
```
$ python -m unittest discover -s tests/ -p "*_test.py"
```

## Database

### Sensor table
```sql
CREATE TABLE "sensors" (
	"id"	INTEGER,
	"haSensorId"	TEXT NOT NULL,
	"type"	INTEGER NOT NULL,
	"createdOn"	INTEGER,
	"updatedOn"	INTEGER,
	"deleted"	INTEGER DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
```

### Automation table
```sql
CREATE TABLE "automations" (
	"id"	INTEGER,
	"value"	TEXT NOT NULL,
	"type"	INTEGER NOT NULL,
	"createdOn"	INTEGER,
	"updatedOn"	INTEGER,
	"deleted"	INTEGER DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
```

### Feedback table
```sql
CREATE TABLE "feedback" (
	"id"	INTEGER,
	"automationId"	INTEGER NOT NULL,
	"type"	INTEGER,
	"createdOn"	INTEGER,
	"updatedOn"	INTEGER,
	"deleted"	INTEGER DEFAULT 0,
	PRIMARY KEY("id" AUTOINCREMENT)
);
```