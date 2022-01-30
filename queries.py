create_table_sql = """
    CREATE TABLE IF NOT EXISTS posts (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content VARCHAR(1000) NOT NULL,
        link VARCHAR(255),
        source VARCHAR(255),
        date TIMESTAMP,
        created_at TIMESTAMP
    )
"""
insert_sql = """INSERT INTO posts(title, content, link, source, date, created_at) VALUES (%s, %s, %s, %s, %s, %s)"""
exists_sql = """SELECT * FROM posts WHERE source=%s AND title = %s AND link = %s"""
