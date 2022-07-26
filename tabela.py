
import pandas
#calcular indicadores
tabela= pandas.read_excel(R"C:\Users\gabir\Downloads\Vendas - Dez.xlsx")
quantidade = tabela["Quantidade"].sum()
faturamento = tabela["Valor Final"].sum()
print(" a quantidade vendida foi {:,} e o valor de faturamento de R${:,.2f}".format(quantidade,faturamento))
