import matplotlib.pyplot as plt

# Открываем файл
with open("rmsd.xvg", 'r') as f:
    lines = [line for line in f if not line.startswith(('#', '@'))]

# Парсим данные
data = [list(map(float, line.strip().split())) for line in lines]
time, rmsd = zip(*data)

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(time, rmsd, label='RMSD')
plt.xlabel('Time (ns)')
plt.ylabel('RMSD (nm)')
plt.title('RMSD over Time')
plt.grid(True)
plt.legend()
plt.show()