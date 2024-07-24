import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_hander

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_connect_to_db():
    assert db_connection_hander.get_engine() is None

    db_connection_hander.connect_to_db()
    db_engine = db_connection_hander.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
    