from etl import extrair_dados, salvar_csv, calcular_kpi_de_total_de_vendas
from datetime import datetime
from schema import schema_dataframe
import os
path = 'data'
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
dado_consolidada = extrair_dados(path)
dado_transformado = calcular_kpi_de_total_de_vendas(dado_consolidada)
schema = schema_dataframe()
validando_df_consolidado = schema.validate(dado_transformado)
print(validando_df_consolidado)
salvarcsv = salvar_csv(validando_df_consolidado, f"data/vendas_consolidadas_{timestamp}.csv")