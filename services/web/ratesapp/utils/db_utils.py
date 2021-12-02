
from ratesapp.db import get_db

def get_rows(query, params):
    db = get_db()
    return db.execute(query, params).fetchall()
