import numpy as np

califas=np.array([60,70,90])
print("------  ej 1 imprimir califas -------")
print(califas)
print(type(califas))#Muestra el tipo de arreglo
print("------ ej 2 dimensiones de un array --------")
califas=np.array(60)
print(califas)
print("Dimesion :", califas.ndim)
print(" ------ ej 1 dimesion de un array ------- ")
califas=np.array([60,70,90])
print(califas)
print("Dimesion :", califas.ndim)
print(" ------ ej 2 dimesion de un array ------- ")
califas = np.array([
    [
        [60, 70, 90],
        [50, 80, 98]
    ],
    [
    [60, 70, 90],
    [50, 80, 98]
]
]) #Un arreglo de tres dimensiones es como una tabla de excel
print(califas)
print("Dimesion :", califas.ndim)
