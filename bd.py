import psycopg2

def connect_to_db():
    try:
        connection = psycopg2.connect(
            user="kubernetes",
            password="senhaforteaqui",
            host="127.0.0.1",
            port="5432",
            database="kubernetes_deploy"
        )

        cursor = connection.cursor()
        print("Conexão com o banco de dados PostgreSQL estabelecida com sucesso")

        # Execute suas operações de banco de dados aqui

    except (Exception, psycopg2.Error) as error:
        print("Erro ao conectar ao PostgreSQL", error)

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("Conexão com o PostgreSQL encerrada")

connect_to_db()
