query = '''
    SELECT
        days.day,
        CASE WHEN ap.cnt < 3 THEN null ELSE ap.price END
    FROM
    (
        SELECT day::date FROM generate_series(%(date_from)s::timestamp, %(date_to)s::timestamp, '1 day'::interval) day
    ) days
    LEFT JOIN
    (
        SELECT AVG(price) AS price, day, COUNT(*) AS cnt
        FROM prices
        WHERE
            orig_code IN %(orig_code)s AND
            dest_code IN %(dest_code)s AND
            day >= %(date_from)s AND
            day <= %(date_to)s
        GROUP BY day
    ) AS ap
    ON ap.day = days.day
'''
