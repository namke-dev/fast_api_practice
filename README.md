### Setup virtual env
```virtualenv --python=/usr/bin/python3.11 ./venv/python3.11```

### Activate the venv
```source venv/python3.11/bin/activate```

### export the env config
```pip freeze > requirements.txt```

### run project
```uvicorn main:app --reload```

### init alembic - DB Migration tool
```alembic init alembic```

### install  SQL ALchemi - ORM
```pip install sqlalchemy```
```pip install psycopg2 -binary```

### Create revision for book table
```alembic revision -m "create book table"```

### upgrade/ downgrade
```alembic upgrade head```