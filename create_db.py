import sqlite3


def create_base():
    conn = sqlite3.connect('base.db')
    info = '''
        CREATE TABLE "passwords" (
        "service"	TEXT,
        "user"	TEXT NOT NULL,
        "password"	TEXT NOT NULL
        )'''
    cursor = conn.cursor()
    cursor.execute(info)
    cursor.close()


def create_pass_master():
    master = input('Crie sua password master: ')
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute(f"""
                    INSERT INTO passwords (service, user, password) 
                    VALUES ('_master', '_master', '{master}')
                    """)
    conn.commit()
    cursor.close()


def db():
    try:
        create_base()
        create_pass_master()
    except sqlite3.OperationalError as e:
        print(e)