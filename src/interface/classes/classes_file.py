import pandas as pd

class CsvProcessor:
    def __init__(self, caminho) -> None:
        self.caminho = caminho
        self.df = None
        self.df_filtrado = None
        
    def ler_arquivo(self):
        self.df = pd.read_csv(self.caminho)
        return self.df
    
    def filtrar_por(self, coluna, atributo):
        self.df_filtrado = self.df[self.df[coluna] == atributo]
        return self.df_filtrado
    
    def sub_filtro(self, coluna, atributo):
        return self.df_filtrado[self.df_filtrado[coluna] == atributo]

