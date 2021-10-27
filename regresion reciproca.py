import numpy as np
import matplotlib.pyplot as plt
def estimate_alpha_beta(x, y):
    #sacando valores del sistema de ecuaciones
    sumatoria_1_div_y = np.sum(1/y)
    sumatoria_x_div_y = np.sum(x*(1/y))
    sumatoria_x_al_cuadrado = np.sum(x**2)
    sumatoria_x = np.sum(x)
    n = np.size(x)
    #Coeficientes de regresion
    a = np.array([[n,sumatoria_x],[sumatoria_x,sumatoria_x_al_cuadrado]])
    b = np.array([[sumatoria_1_div_y],[sumatoria_x_div_y]])
    res = np.linalg.inv(a).dot(b)
    return(res)
#Funcion de graficado
def plot_regression(x,y,b):
    plt.scatter(x, y, color="r", marker = "o", s=30)
    y_pred = 1 / b[0] + b[1]*x
    plt.plot(x, y_pred, color = "b")
    #Etiquetado
    plt.xlabel('Longitud [m]')
    plt.ylabel('Qcond [kJ]')
    plt.show()

#Codigo main
def main():
    #DATASET
    x = np.array([0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.008,0.009,0.010])
    y = np.array([393120,196560,131040,98280,78624,65520,56160,49140,43680,39312])
    #Obteniendo alpha y beta
    b = estimate_alpha_beta(x, y)
    print(f'Los valores de alpha = {b[0]}, b1 = {b[1]}*x')
    print(f'La ecuacion resultante es : Qcond=1/({b[0]}+{b[1]})')
    #Grafica la linea de regresion
    plot_regression(x,y,b)

if __name__=='__main__':
    main()