import pandas as pd
df_1 = pd.DataFrame({'Nombre':['Maria','Jose','David','Juan','Pedro','Ivan'],
    'Carrera':['Auditoria', 'Fisica', 'Quimica', 'Historia', 'Programacion', 'Economia'],
                     'EDAD':[27,23,20,25,24,21]}).set_index('Nombre')
df_2 = pd.DataFrame({'Nombre':['Marco','Johana','Mauricio','Luna'],
                     'Carrera':['Medicina', 'Informatica', 'Quimica', 'Historia'],
                     'EDAD':[19,28,20,22]}).set_index('Nombre')
df = pd.concat([df_1,df_2])
#print(df)
autos_1 = pd.DataFrame({'AUTOS':['Audi','Nissan','BMW'],
                        'COLOR':['Rojo','Negro','Blanco']}).set_index('AUTOS')
autos_2 = pd.DataFrame({'AUTOS':['Audi','Nissan','BMW'],
                        'MODELOS':[2018,2022,2024]}).set_index('AUTOS')
autos = pd.concat([autos_1,autos_2],axis=1)
#print(autos)
autos_3 = pd.DataFrame({'AUTOS':['Audi','Nissan','BMW'],
                        'COLOR':['Rojo','Negro','Blanco']})
autos_4 = pd.DataFrame({'AUTOS':['Audi','Toyota','BMW'],
                        'MODELOS':[2018,2022,2024]})
autos_5 = pd.merge(autos_3,autos_4,how='outer')
print(autos_5)