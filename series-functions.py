import pandas as pd
numeros = pd.Series([1,2,3,4,5,6,7,8,9,10])
tem = numeros.std()
#print(numeros.describe())
serie = pd.Series({'Matematicas':6, 'Fisica':7, 'Quimica':8, 'Historia':9, 'Programacion':10, 'Economia':4})
##print(serie.sort_index(ascending=False))
data = 5
new_serie = pd.Series(data, index=[0,1,2,3,4,5])
##print(new_serie)
data_list = ['Messi', 'Cristiano Ronaldo','Benzema']
index = ['PSG', 'Manchester United', "Real Madrid"]
football = pd.Series(data_list, index=index)
print(football)