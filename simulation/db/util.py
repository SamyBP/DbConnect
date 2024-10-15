import psycopg2


def get_connection(credentials: dict):
    return psycopg2.connect(
        database=credentials.get("database"),
        user=credentials.get("user"),
        password=credentials.get("password")
    )
