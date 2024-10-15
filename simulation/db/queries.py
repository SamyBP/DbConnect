def create_test_table(conn):
    sql = """
        create table if not exists test(
            id serial primary key,
            message text
        );
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def cleanup_between_tests(conn):
    cursor = conn.cursor()
    cursor.execute("truncate table test")
    conn.commit()


def add_entry(conn):
    cursor = conn.cursor()
    cursor.execute("insert into test(message) values ('Test message');")
    conn.commit()


def get_number_of_inserts(conn):
    cursor = conn.cursor()
    cursor.execute("select count(*) from test;")
    return cursor.fetchone()[0]
