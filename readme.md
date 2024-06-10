### Project Structure

smart_kitchen_backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── auth.py
├── requirements.txt
├── alembic.ini
├── alembic/
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/
└── .env

### Requirements 

`pytohon=3.11`
`pip install -r requirements.txt`

### inital Migration 

`alembic revision --autogenerate -m "Initial migration"`
`alembic upgrade head`


### Run Server 

`uvicorn app.main:app --reload`




