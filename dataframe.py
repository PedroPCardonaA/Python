import pandas as pd
import numpy as np
data = {'NOMBRE':['Maria','Jose','David','Juan','Pedro','Ivan'],
        'CARRERA':['Auditoria', 'Fisica', 'Quimica', 'Historia', 'Programacion', 'Economia'],
        'CORREO':['qxZVh@example.com', 'qxZVh@example.com', 'qxZVh@example.com', 'qxZVh@example.com', 'qxZVh@example.com', 'qxZVh@example.com'],
        }
estudiantes = pd.DataFrame(data)
#print(estudiantes)
df = pd.DataFrame([['Maria',27],['Jose',23],['David',20],['Juan',25],['Pedro',24],['Ivan',21]],
                  columns=['NOMBRE','EDAD'])
#print(df)
df_raid = pd.DataFrame(np.random.randn(4,3),columns=['A','B','C'])
print(df_raid)
