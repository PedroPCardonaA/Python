import pandas as pd
df = pd.read_csv('ModalidadVirtual.csv')
#print(df['carrera'][1])
#print(df['edad'] > 23)
filter = df['edad'] > 23
#print(df[filter])
df['TURNO'] = pd.Series(['Mañana','Tarde','Noche','Mañana','Tarde','Noche','Mañana','Tarde','Noche','Mañana','Tarde','Noche'])
print(df)
TURNO = df.pop('TURNO')
print(df)
# DROP delete rows
print(df[(df['sexo'] == 'Mujer') & (df['edad'] > 23)])
