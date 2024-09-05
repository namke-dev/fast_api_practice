# Setup guide

### Setup virtual env
```virtualenv --python=/usr/bin/python3.11 ./venv/python3.11```

### Activate the venv
```source venv/python3.11/bin/activate```

### install dependency from requirement text file
```pip install -r requirements.txt```

### install dependency
```pip install python-dotenv```

### Create postgre DB intance in docker container
```docker run -d   --name postgres_container   -e POSTGRES_USER=sa   -e POSTGRES_PASSWORD=123456   -p 5432:5432   -v postgres_data:/var/lib/postgresql/data   postgres:latest```

### rename env.txt to .env (file in root dir)

### upgrade/ downgrade
```alembic upgrade head```

### run project
```uvicorn main:app --reload```

# build guide

### init alembic - DB Migration tool
```alembic init alembic```

### install  SQL ALchemi - ORM
```pip install sqlalchemy```
```pip install psycopg2 -binary```

### install psycopg2-binary
```pip install spycopg2-binary```

### Create revision for book table
```alembic revision -m "create book table"```

### export the env config
```pip freeze > requirements.txt```