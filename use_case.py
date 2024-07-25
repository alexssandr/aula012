from src.interface.classes.classes_file import CsvProcessor

vendas = CsvProcessor('vendas.csv')
print(vendas.ler_arquivo())
print('###############')
print(vendas.filtrar_por('Cidade','Salvador'))
print('###############')
print(vendas.sub_filtro('Valor', 77.46))