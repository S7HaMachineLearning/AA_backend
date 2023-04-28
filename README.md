# AA_backend

## Dependencies
`pip install fastapi "uvicorn[standard]"`

## Run the server
`python -m uvicorn main:app`

## Run local server, but accessible over network
`python -m uvicorn main:app --host 0.0.0.0 --port 8000`



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