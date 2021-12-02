from flask import (
    Blueprint, flash, g, json, redirect, render_template, request, url_for
)
from flask import jsonify
from werkzeug.exceptions import BadRequest

from ratesapp.service.rates_service import get_rates

bp = Blueprint('rates', __name__, url_prefix='/rates')

@bp.route('/')
def index(methods=['GET']):
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    origin = request.args.get('origin')
    destination = request.args.get('destination')

    if not origin:
        raise(BadRequest("Invalid origin arguments"))
    if not destination:
        raise(BadRequest("Invalid destination arguments"))
    if not date_from:
        raise(BadRequest("Invalid date_from arguments"))
    if not date_to:
        raise(BadRequest("Invalid date_to arguments"))

    results = get_rates(date_from, date_to, origin, destination)
    return jsonify(results)

