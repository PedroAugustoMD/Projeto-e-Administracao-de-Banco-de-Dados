import psycopg2

#Conexão

con = psycopg2.connect(host='localhost', database='AtividadesBD',
user='postgres', password='postgres')
cur = con.cursor()

# Inserir uma atividade em algum projeto

cur.execute("insert into atividade(descricao, codProjeto, dataInicio, dataFim) values('BD - Atividade 4', 3, '2022-06-30', '2022-07-28');")
con.commit()

# Atualizar o líder de um projeto

cur.execute("update projeto set codresponsavel = 1 where codigo = 3;")
con.commit()

# Listar todas os projetos e suas atividades

cur.execute("SELECT * FROM projeto p, atividade a WHERE a.codprojeto = p.codigo GROUP BY p.codigo, a.codigo ORDER BY p.codigo ASC;")
resultados = cur.fetchone() 

for i in resultados:
    print(i)

cur.close()
con.close()