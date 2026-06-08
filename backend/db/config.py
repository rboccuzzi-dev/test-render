from sqlalchemy import create_engine, text
import os

# mysql+pymysql://usuario:password@host/db
engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_LINK')}:{os.getenv('DB_PORT')}/restaurante",
    connect_args={
        "ssl": {
            "ca": os.getenv("SSL_CERT"),
        }
    },
    echo=False,
    future=True
)


def ejecutar_query_lectura(query, params=None):
    with engine.connect() as conn:
        resultado = conn.execute(text(query), params or ())
        return resultado.mappings().all()

def ejecutar_query_escritura(query, params=None):
    with engine.begin() as conn:
        resultado = conn.execute(text(query), params or ())
        return resultado.lastrowid
