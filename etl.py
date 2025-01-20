
# Uma função de extração que lê e consolida os dados em json
import pandas as pd
from schema import schema_dataframe
import os
import glob
from datetime import datetime


def extrair_dados(path: str) -> pd.DataFrame:
    #Faz uma busca no diretorio por arquivos do tipo especificados
    arquivos_json = glob.glob(os.path.join(path, '*.json')) # E adiciona a uma lista

    # Faz uma busca por esses arquivos na lista e transforma cada um em um dataframe
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json] # E Adiciona a uma lista de dataframes
    
    #Junta esses datafranes em um unico
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

#Uma função de transformação


def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


#Uma função que da load(salva) em csv ou parquet


def salvar_csv(df,path):
    try:    
        df.to_csv(path, index=False, encoding = 'utf-8-sig')
        print(f"Arquivo salvo em {path}")
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo {e}")
        return False


#Uma função que da load(salva) em csv ou parquet

def salvar_parquet(df,path):
    try:    
        df.to_parquet(path, index=False)
        print(f"Arquivo salvo em {path}")
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo {e}")
        return False


    



if __name__ == "__main__":
    path_pasta = 'data'
    df = extrair_dados(path=path_pasta)
    novo_df = calcular_kpi_de_total_de_vendas(df)
    schema = schema_dataframe()
    validando_df = schema.validate(novo_df)
    print(validando_df)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
   # salvarcsv = salvar_parquet(df, f"data/comercio_{timestamp}.parquet")




