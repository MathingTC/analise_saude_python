import sqlite3
import pandas as pd

dados = pd.read_csv("dados_tratados.csv")

#criação do banco
try:
    conexao = sqlite3.connect("banco_saude.db")
    cursor = conexao.cursor()
except sqlite3.Error as erro:
    print("Erro no banco de dados: ", erro)

#criação da tabela
cursor.execute("DROP TABLE IF EXISTS pacientes")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gender TEXT,
        age REAL,
        hypertension INTEGER,
        heart_disease INTEGER,
        ever_married TEXT,
        work_type TEXT,
        residence_type TEXT,
        average_glucose_level REAL,
        bmi REAL,
        smoking_status TEXT,
        stroke INTEGER,
        AVC text
    )
""")

#inserção dos dados
lista_pacientes = dados.values.tolist()#tá fazendo a conversão do dataframe para uma lista
#print(lista_pacientes)
for insercao in lista_pacientes:
    cursor.execute("""
        INSERT INTO pacientes
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, insercao)# cada interrogação é um placeholder, é como se fosse o valor de cada coluna

#salvando as alterações no banco
conexao.commit()
print("\nDados inserido no banco banco_saude.db.")

#consulta 1 - quantidade total de registros armazenados
cursor.execute("SELECT * FROM pacientes")
todos = cursor.fetchall()
print("\nQuantidade total de registros: ", len(todos))

#consulta 2 - pacientes com registro de AVC
cursor.execute("SELECT * FROM pacientes WHERE stroke = 1")
pacientes_com_avc = cursor.fetchall()
print("\nPacientes com registros de AVC: ", len(pacientes_com_avc))

#consulta 3 - pacientes com hipertensão que tiveram AVC
cursor.execute("SELECT * FROM pacientes WHERE hypertension = 1 AND stroke = 1")
hipertensao_avc = cursor.fetchall()
print("\nPacientes que têm hipertensão e AVC: ", len(hipertensao_avc))

conexao.close()
