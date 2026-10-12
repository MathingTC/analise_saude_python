import pandas as pd

#carregamento do dataset
dados = pd.read_csv("Atividade2.csv")

#Preparação e limpeza dos dados
#Análise básica
linhas, colunas = dados.shape
print(f"Quantidade de registros: ", linhas)
print(f"Quantidade de características: ", colunas)

print("Primeiras linhas do dataset:")
print(dados.head())

print("\Colunas e seus tipos de dados:")
print(dados.dtypes)

print("\nInformações estátiscas: ")
print(dados.describe())

#valores ausentes
print("Valores ausentes:")
print(dados.isnull().sum())#só tem valores ausentes no BMI??

#realizando um filtrp
bmi_ausente = dados[dados["bmi"].isnull()]
print("\nRegistros com BMI ausente: ", len(bmi_ausente))
print("\nQuantos desses com AVC: ", len(bmi_ausente[bmi_ausente["stroke"] == 1]))#vê nas linhas com o BMI 
                                                                                 #ausente quantas tem AVC

#ajuda a identificar o que é unknown pq o isnull não reconhece, o unknown é uma ausência disfarçada em texto
print("\nCategorias de smoking_status:")
print(dados["smoking_status"].value_counts())

#remove todos os NaN/Unknown da coluna BMI e troca pela média de BMI
media_bmi = dados["bmi"].mean()#aqui q é realizada a média
dados["bmi"] = dados["bmi"].fillna(media_bmi)#troca os NaN pela média
print("\nMédia do BMI: ", round(media_bmi, 2))

#alteração dos smoking_status unknown para não informado
dados.loc[dados["smoking_status"] == "Unknown", "smoking_status"] = "não informado"

#transformação com lambda
dados["AVC"] = dados["stroke"].apply(lambda avc: "Com AVC" if avc == 1 else "Sem AVC")

#evidencias dados tratados
print("\nAgora não tem mais valores ausentes/inexistentes:")
print(dados.isnull().sum())

print("\nQuantidade de registros se manteve:", dados.shape[0])

print("\nDados de fumantes:")
print(dados["smoking_status"].value_counts())

print("\nNova coluna 'AVC':")
print(dados["AVC"].value_counts())

#salvando a base
dados.to_csv("dados_tratados.csv", index=False)
print("\nArquivo 'dados_tratados.csv' salvo.")
