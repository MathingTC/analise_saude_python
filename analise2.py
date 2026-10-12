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

#Comparando quem tem hipertensão e doença cardíaca com quem teve AVC
print("\nPercentual de pessoas com e sem AVC que também possuem hipertensão e doença cardíaca: ")
print((dados.groupby("AVC")[["hypertension", "heart_disease"]].mean() * 100).round(2))

#agora em quantidade, não percentual
print("\nQuantidade de pessoas em cada grupo: ")
print(dados.groupby("AVC")[["hypertension", "heart_disease"]].sum())

#percentual de quem tem alguma das condições, qual o percentual de quem tem AVC?
print("\nPorcentagem de quem tem hipertensão que também tem AVC(0 é não tem AVC e 1 é que tem): ")
print((dados.groupby("hypertension")["stroke"].mean() * 100).round(2))
print("\nPorcentagem de quem tem doença cardíaca que também tem AVC(0 é não tem AVC e 1 é que tem) : ")
print((dados.groupby("heart_disease")["stroke"].mean() * 100).round(2))

#comparação da glicose de quem tem AVC e quem não tem
print("\nNível médio de glicose das pessoas com e sem AVC: ")
print(dados.groupby("AVC")["avg_glucose_level"].agg(["mean", "min", "max"]).round(2))

#comparação do IMC de quem tem AVC e quem não tem
print("\nIMC médio das pessoas com e sem AVC: ")
print(dados.groupby("AVC")["bmi"].agg(["mean", "min", "max"]).round(2))

#comparação de quem fuma e quem não fuma com quem tem AVC
print("\nQuantidade de pessoas que fumam que tem AVC: ")
print(com_avc["smoking_status"].value_counts())


