import pandas as pd
import pandera as pa

def schema_dataframe() -> pa.DataFrameSchema:
    return pa.DataFrameSchema ({
    
        "Produto": pa.Column(str),
        "Categoria": pa.Column(str),
        "Quantidade": pa.Column(int, checks = pa.Check.le(10)),
        "Venda": pa.Column(int, checks = pa.Check.le(1500)),
        "Data": pa.Column(),
        "Total": pa.Column(int, checks= pa.Check.le(4500))
        
    })