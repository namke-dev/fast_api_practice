### Setup virtual env
```virtualenv --python=/usr/bin/python3.11 ./venv/python3.11```

### Activate the venv
```source venv/python3.11/bin/activate```

### install dependency from requirement text file
```pip install -r requirements.txt```

### export the env config
```pip freeze > requirements.txt```

### Create postgre DB intance in docker container
```docker run -d   --name postgres_container   -e POSTGRES_USER=sa   -e POSTGRES_PASSWORD=123456   -p 5432:5432   -v postgres_data:/var/lib/postgresql/data   postgres:latest```

### init alembic - DB Migration tool
```alembic init alembic```

### install  SQL ALchemi - ORM
```pip install sqlalchemy```
```pip install psycopg2 -binary```

### install psycopg2-binary
```pip install spycopg2-binary```

### define app config by create .env file in root dir
```
# PostgreSQL
ASYNC_DB_ENGINE=postgresql+asyncpg
DB_ENGINE=postgresql
DB_HOST=localhost
DB_USERNAME=sa
DB_PASSWORD=123456
DB_NAME=todoapi
DB_PORT=5432

DEFAULT_PASSWORD=secrec@123
JWT_SECRET=secrec@123
JWT_ALGORITHM=HS256
```
### Create revision for book table
```alembic revision -m "create book table"```

### upgrade/ downgrade
```alembic upgrade head```

### run project
```uvicorn main:app --reload```

### get auth token with acocunt: admin/123456