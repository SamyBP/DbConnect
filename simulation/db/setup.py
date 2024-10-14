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
    cursor.execute("vacuum full")
    cursor.commit()
