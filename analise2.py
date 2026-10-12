import pandas as pd

dados = pd.read_csv("dados_tratados.csv")

#grupos avc
com_avc = dados[dados["stroke"] == 1] #aqui filtra só quem teve avc
sem_avc = dados[dados["stroke"] == 0] #quem n teve

print("Com AVC: ", len(com_avc))
print("Sem AVC: ", len(sem_avc))

print("Percentual de quem tem AVC: ", round(len(com_avc) / len(dados) * 100, 2), "%")

#idades com avc
print(dados.groupby("AVC")["age"].agg(["count", "mean", "min", "max"]).round(2))

print("\n===Análise de idade com o AVC===")
#quantos com avc de acordo com a idade
idosos_avc = dados[(dados["stroke"] == 1) & (dados["age"] >= 60)]
print("\nPessoas com AVC e idade maior ou igual a 60: ", len(idosos_avc))

idosos_sem = dados[(dados["stroke"] == 0) & (dados["age"] >= 60)]
print("\nPessoas sem AVC e idade maior ou igual a 60: ", len(idosos_sem))

nIdosos_avc = dados[(dados["stroke"] == 1) & (dados["age"] < 60)]
print("\nPessoas com AVC e idade menor que 60: ", len(nIdosos_avc))

nIdosos_sem = dados[(dados["stroke"] == 0) & (dados["age"] < 60)]
print("\nPessoas sem AVC e idade menor que 60: ", len(nIdosos_sem))

#2 e 3. HIPERTENSÃO E DOENÇA CARDÍACA
print("\nAAAAAAAAAAAAAAAAAAA")
print((dados.groupby("AVC")[["hypertension", "heart_disease"]].mean() * 100).round(2))
