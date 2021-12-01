
from flask import (
    Blueprint, flash, g, json, redirect, render_template, request, url_for
)
from flask import jsonify

from ratesapp.db import get_db

bp = Blueprint('rates', __name__, url_prefix='/rates')

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute('SELECT * FROM PORTS LIMIT 1').fetchall()
    results = []
    for p in posts:
        results.append(list(p))
    return jsonify(results)

