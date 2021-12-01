import sqlite3

import click
from flask import current_app, g

from sqlalchemy import create_engine

def get_db():
    if 'db' not in g:
        g.db = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.dispose()

def init_app(app):
    app.teardown_appcontext(close_db)
