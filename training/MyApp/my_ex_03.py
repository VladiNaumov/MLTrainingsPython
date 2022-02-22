# Постановка ML задачи линейной регрессии

from numpy.linalg import inv
from matplotlib import pyplot as plt
import numpy as np


"""
Х это площадь дома
Y это цена

X = [20, 27, 36, 45, 54, 61, 78]
Y = [40, 50, 80, 90, 100, 120, 155]
"""

"""
шагом определите данные, с которыми предстоит работать. 
Входы (регрессоры, x) и выход (предиктор, y) должны быть массивами (экземпляры класса numpy.ndarray) или похожими объектами. 
"""

# добовляем тревиальную переменную - данная переменная в нешем случае всегда равна 1
X = np.array([[1, 20], [1, 27], [1, 36], [1, 45], [1, 54], [1, 61], [1, 78]])
print(X)

# добовляем вектор Y в каторый записываем цены домов
Y = np.array([[40], [50], [80], [90], [100], [120], [155]])
print(Y)

# выводим площадь и цену на систему координат (представляем графически)
plt.scatter(X_area, Y_price, 40, 'g', 'o', alpha=0.8)
plt.show()



# Выписываем формулу (X в степени T умноженная на Х )по кусочкам. Сначала перемножим матрицу объекты-признаки саму на себя
X_T_X = (X.T).dot(X)
print(X_T_X)

# Теперь найдём обратную матрицу к ней.
# Тут вручную прогграммировать ничего не надо - для нахождения обратной матрицы уже есть готовая реализация в библеотеке NumPy
X_T_X_inverted = inv(X_T_X)
print(X_T_X_inverted)

# Вывод - это коэффициент линейной регрессии
w = X_T_X_inverted.dot(X.T).dot(Y)
print( "это коэффициент линейной регрессии w_1=%.5f, w_2=%.3f" % (w[0][0],w[1][0]))

# То есть наш набор из пяти точек прекрасно описывает прямая линия с уравнением  y=−17.5 + 0.714⋅x. 
# Давайте проверим это графически.
# задаём границы координатных осей
margin = 10 # это отступы
X_min = 20
X_max = X[:,1].max()+ margin

# набор точек, чтобы нарисовать прямую
X_support = np.linspace(X_min, X_max, num=100) # функция np.linspace() генерирует последовательность точек между X_min и X_max (num=100 это для отоброжение линии)
# предсказания нашей модели
Y_model = w[0][0] + w[1][0]*X_support

# Исходные данные подготовлены! Осталось нарисовать график

# настройка графика
plt.xlim(X_min, X_max)
plt.ylim(0, Y[:,0].max() + margin)
# рисуем исходные точки
plt.scatter(X[:,1], Y[:,0], 40, 'g', 'o', alpha=0.8)
# предсказания модели
plt.plot(X_support, Y_model)

plt.show()
