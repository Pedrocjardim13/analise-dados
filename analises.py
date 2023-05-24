import pandas as pd
import plotly.express as px

tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")

tabela = tabela.drop("Unnamed: 8", axis=1)

tabela = tabela.dropna()

tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    grafico.update_layout(bargap=0.2)
    grafico.show()