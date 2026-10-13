import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("dados_tratados.csv")

#Gráfico 1 – Distribuição das idades dos pacientes com registro de AVC
com_avc = dados[dados["stroke"] == 1]

plt.figure()
com_avc["age"].plot(kind="hist", bins=10, edgecolor="black")
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

