#Importando as bibliotecas a serem utilizadas
import pandas as pd
import datetime as dt
#Lendo o arquivo
base = pd.read_csv('netflix daily top 10.csv')
#Espiando os dados - 5 primeiras linhas, 5 útimas e tamanho
display(base)
#Descobrindo o período de análise
inicio = pd.to_datetime(base['As of']).dt.date.min()
fim = pd.to_datetime(base['As of']).dt.date.max()
print(inicio, fim)
#Verificando os tipos de dados e valores nulos, para verificar se posteriormente há necessidade de tratar os dados
base.info()
#Entendendo os valores nulos
base['Netflix Exclusive'].value_counts()
#Entendemos aqui que os valores nulos nessa coluna corresponde a não
#Analisando informações estatísticas
base.describe()
#Plotando um gráfico 
base.plot(kind = 'box', figsize = (10, 6), subplots = True);
#Verificamos que existem muitos valores outliers
#Quem seriam esses outliers?
base[base['Days In Top 10'] >= 100]
base.Title.value_counts()
#Percebemos que o desenho 'Cocomelon' é nosso outlier
#Entendendo melhor a última coluna, trata-se da pontuação do título a partir da coloção no ranking
base['Viewership Score'].hist()
#Percebemos que os filmes não permanecem muito tempo no top 10
base[base['Viewership Score'] == base['Viewership Score'].max()]
#Confirmamos que o título que permaneceu por mais tempo no top 10 é o desenho 'Cocomelon'
