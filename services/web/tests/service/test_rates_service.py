import pytest
from datetime import datetime
from unittest.mock import MagicMock
from ratesapp.service import rates_service
from ratesapp.utils import db_utils


def test_is_slug():
    assert rates_service.is_slug("AABBC") == False
    assert rates_service.is_slug("northeast_main") == True

def test_get_port_codes():
    assert rates_service.get_port_codes("AABBC") == ["AABBC"]

    db_utils.get_rows = MagicMock(return_value=[{'port': "AABBC"}])
    assert rates_service.get_port_codes("northeast_main") == ["AABBC"]

def test_get_rates():
    rates_service.get_port_codes = MagicMock(return_value=["AABBC"])
    dt = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    test_arg = {'day': dt, 'price': 1220}
    test_result = {'day': dt.isoformat(), 'price': 1220}
    db_utils.get_rows = MagicMock(return_value=[test_arg])

    assert rates_service.get_rates('', '', '', '') == [ test_result ]



