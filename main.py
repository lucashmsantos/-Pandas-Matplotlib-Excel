import pandas as pd
import matplotlib.pyplot as plt

#Set Diretório
plcadastro = pd.read_excel(r"C:\Users\Lucas\Documents\Python\PlanilhaCadastros\Dados.xlsx", engine='openpyxl')

#Plotando Gráfico
plt.bar(plcadastro['Vendedor'], plcadastro['Valor'])

#Configuração label
plt.xlabel('Vendedor')
plt.ylabel('Valor')
plt.title('Valores por vendedor')
plt.show()

#Run
plt.show()

