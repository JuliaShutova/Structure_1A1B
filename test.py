import numpy as np
import matplotlib.pyplot as plt

# Фиктивные данные: время и RMSD
time = np.arange(0, 10, 1)          # 10 временных точек
rmsd_values = np.random.rand(10) * 2  # Случайные значения от 0 до 2 Å

# Построение графика
plt.plot(time, rmsd_values, 'bo-', linewidth=2, markersize=5)
plt.xlabel("Время (нс)")
plt.ylabel("RMSD (Å)")
plt.title("Пример графика RMSD")
plt.grid(True)
plt.show()