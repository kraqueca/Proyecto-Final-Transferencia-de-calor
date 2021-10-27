import numpy as np
import matplotlib.pyplot as plt

def estimate_b0_b1(x, y):
    n = np.size(x)
    #Sacamos promedios de X y de Y 
    m_x, m_y = np.mean(x), np.mean(y)
    #Calcular la sumatoria de XY y mi sumatoria de XX
    sumatoria_xy = np.sum((x-m_x)*(y-m_y))
    sumatoria_xx = np.sum(x*(x-m_x))
    #Coeficientes de regresion
    b_1 = sumatoria_xy / sumatoria_xx
    b_0 = m_y - b_1*m_x
    return(b_0, b_1)

#Funcion de graficado
def plot_regression(x,y,b):
    plt.scatter(x, y, color="r", marker = "o", s=30)

    y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color = "b")
    #Etiquetado
    plt.xlabel('x-Independiente')
    plt.ylabel('y-Dependiente')

    plt.show()

#Codigo main
def main():
    #DATASET
    x = np.array([0,10,20,30,40,50,60,70,80,90,100])
    y = np.array([0.94,0.96,1,1.05,1.07,1.09,1.14,1.17,1.21,1.24,1.28])
    #Obteniendo b1 y b2
    b = estimate_b0_b1(x, y)
    print(f'Los valores de b0 = {b[0]}, b1 = {b[1]}')
    #Grafica la linea de regresion
    plot_regression(x,y,b)

if __name__=='__main__':
    main()