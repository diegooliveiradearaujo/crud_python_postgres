import psycopg2 as pg

#CONFIGURAÇÃO DO POSTGRES - OBS: LOCALMENTE
conexao = pg.connect(host='localhost',
                     database='exemplo',
                     user='postgres',
                     password='admin'
                    )
conectado = conexao.cursor()

#criar_tabela = "create table postgres_python.tb_python( id int not null, nome varchar not null, idade int not null)"
#conectado.execute(criar_tabela)
#conexao.commit()


def inserir_dados(a,b,c):
    comando_insercao=("insert into postgres_python.tb_python (id,nome,idade) values (%s,%s,%s)")
    conectado.execute(comando_insercao,(a,b,c))
    conexao.commit()

def editar_dados():
    novo_nome=input("Qual é o novo nome? ")
    condicao_idade=int(input("Qual é a condição da idade? "))
    comando_edicao = ("update postgres_python.tb_python SET nome = %s WHERE idade = %s")
    conectado.execute(comando_edicao,(novo_nome,condicao_idade))
    conexao.commit()
    print("Dados alterados com sucesso!")

def remover_todos_dados():
    comando_exclusao = "truncate postgres_python.tb_python"
    conectado.execute(comando_exclusao)
    conexao.commit()
    print("Dados excluídos com sucesso!")

def remover_tabela():
    comando_exc_tabela = "drop table postgres_python.tb_python"
    conectado.execute(comando_exc_tabela)
    conexao.commit()
    print("Tabela excluída com sucesso!")

def visualizar_dados():
    comando_visualizacao = "select * from postgres_python.tb_python"
    conectado.execute(comando_visualizacao)
    resultado = conectado.fetchall()
    print(resultado)
    for linhas in resultado:
        print("\nid: ", linhas[0])
        print("nome: ", linhas[1])
        print("idade: ", linhas[2])

print("1 - Inserir dados;")
print("2 - Editar/atualizar dados;")
print("3 - Remover todos os registros;")
print("4 - Remover tabela;")
print("5 - Visualizar dados")
opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    id = int(input("Qual é o id do registo? ")) #1
    nome = input("Qual é o nome? ") #diego
    idade = int(input("Qual é a idade? ")) #30
    inserir_dados(id,nome,idade)
    print("Dados enviados com sucesso!")
elif opcao == 2:
    editar_dados()
elif opcao == 3:
    remover_todos_dados()
elif opcao == 4:
    remover_tabela()
elif opcao == 5:
    visualizar_dados()
    













