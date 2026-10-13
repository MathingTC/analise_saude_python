import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("dados_tratados.csv")

#Gráfico 1 – Distribuição das idades dos pacientes com registro de AVC
com_avc = dados[dados["stroke"] == 1]

plt.figure()
com_avc["age"].plot(kind="hist", bins=10, edgecolor="black") #esse gráfico é um histograma k
plt.title("Distribuição das idades dos pacientes com AVC")
plt.xlabel("Idade/anos")
plt.ylabel("Quantidade de pacientes")
plt.savefig("grafico1_idade_avc.png")
plt.show()

#Gráfico 2 – Comparação entre pacientes com e sem AVC - com o nivel médio de glicose
glicose_AVC = dados.groupby("AVC")["avg_glucose_level"].mean()

plt.figure()
glicose_AVC.plot(kind="bar", rot=0)
plt.title("Nível médio de glicose: paciente com e sem AVC")
plt.xlabel("Grupos de AVC")
plt.ylabel("Nível médio de glicose")
plt.savefig("grafico2_glicose_avc.png")
plt.show()

#Gráfico 3 - AVC por faixa etária
faixa_0_17 = dados[dados["age"] < 18]
faixa_18_39 = dados[(dados["age"] >= 18) & (dados["age"] <= 39)]
faixa_40_59 = dados[(dados["age"] >= 40) & (dados["age"] < 60)]
faixa_60_mais = dados[dados ["age"] >= 60]

taxas = pd.Series(
    [
        faixa_0_17["stroke"].mean() * 100,
        faixa_18_39["stroke"].mean() * 100,
        faixa_40_59["stroke"].mean() * 100,
        faixa_60_mais["stroke"].mean() * 100,
    ],
    index=["0-17", "18-39", "40-59", "60 ou mais"]
)

print(taxas.round(2))   

plt.figure()
taxas.plot(kind="bar", rot=0)
plt.title("Taxa de AVC por Faixa Etária")
plt.xlabel("Faixa etária (anos)")
plt.ylabel("Pacientes com AVC (%)")
plt.savefig("grafico3_taxa_avc_faixa_etaria.png")
plt.show()
