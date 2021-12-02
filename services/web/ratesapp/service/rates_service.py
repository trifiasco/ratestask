
from ratesapp.queries import get_ports_from_slug
from ratesapp.queries import get_rates_query
from ratesapp.utils import db_utils

def is_slug(val):
    if len(val) == 5 and val.isupper():
        return False
    return True

def get_port_codes(slug):
    if is_slug(slug) == False:
        return [slug]


    ports = db_utils.get_rows(get_ports_from_slug.query, {'slug': slug})
    results = []
    for p in ports:
        results.append(p['port'])
    return results

def row_aggregate_to_dto(row):
    return {
        'day': row['day'].isoformat(),
        'price': int(round(row['price'])) if row['price'] is not None else None,
    }

def get_rates(date_from, date_to, origin, destination):
    origin_ports = get_port_codes(origin)
    destination_ports = get_port_codes(destination)
    rates_rows = db_utils.get_rows(get_rates_query.query, {
        'date_from': date_from,
        'date_to': date_to,
        'orig_code': tuple(origin_ports),
        'dest_code': tuple(destination_ports)
    })
    rates = [row_aggregate_to_dto(r) for r in rates_rows]

    return rates
