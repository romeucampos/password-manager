import sqlite3
import sys

import create_db


class Data:
    def __init__(self):
        self.base = sqlite3.connect('base.db')
        self.funcs = {
                        'o': self.options,
                        'l': self.listed,
                        'v': self.views,
                        'i': self.insert,
                        's': sys.exit
                    
                    }
        

    def read(self, info):
        conn = self.base
        cursor = conn.cursor()
        cursor.execute(info)
        f = cursor.fetchall()
        cursor.close()
        return f

    def insert(self):
        service = input('digite a serviço: ')
        user = input('digite a usuário: ')
        password = input('digite a password: ')
        conn = self.base
        cursor = conn.cursor()
        cursor.execute(f"""
                        INSERT INTO passwords (service, user, password) 
                        VALUES ('{service}', '{user}', '{password}')
                        """)
        conn.commit()
        cursor.close()
        print('serviço cadastrado!\n')

    def login(self):
        senha = self.read("""
                        SELECT *
                        FROM passwords
                        WHERE service = '_master'
                        """)
        login = input('digite seu password master: ')
        return senha[0][2] == login

    def listed(self):
        lista = self.read("""
                        SELECT service
                        FROM passwords
                        WHERE service != '_master'
                        """)
        for l in lista:
            print(l)

    def views(self):
        service = input('digite a senha que quer: ')
        info = f"""
                SELECT *
                FROM passwords
                WHERE service = '{service}'
                """
        print(self.read(info))

    def options(self):
        print(
            f'{"-"*40}\n'
            f'o: opções\n'
            f'l: listar servições registrados\n'
            f'v: visualizar a senha\n'
            f'i: inseri\n'
            f's: sair\n'
            f'{"-"*40}\n'
            )
    
    def main(self):
        
        if data.login():
            print('senha correta\n')

            while True:     

                func = input('digite "o" para mostrar opções: ')

                try:
                    data.funcs.get(func)()

                except Exception as e:
                    print('essa opçãos não existe')
        else:
            print('senha incorreta')


if __name__ == '__main__':
    try:
        data = Data()
        data.main()
    except sqlite3.OperationalError as e:
        create_db.db()
        data.main()
    
