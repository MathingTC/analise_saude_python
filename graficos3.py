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
