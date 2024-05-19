import numpy as np
import matplotlib.pyplot as plt

# Adatok betöltése a fájlból
loaded_data = np.load('Bot_3/Bot_3_watch_time.npy')

# A vonaldiagram létrehozása
x = np.arange(len(loaded_data))  # x tengely értékei (0, 1, 2, ...)
y = np.cumsum(loaded_data)  # Az értékek kumulatív összege

# Vonaldiagram
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.xlabel('Idő')
plt.ylabel('Érték')
plt.title('Vonaldiagram')

# Pontdiagram
plt.subplot(2, 2, 2)
plt.scatter(x, loaded_data)
plt.xlabel('Idő')
plt.ylabel('Érték')
plt.title('Pontdiagram')

# Oszlopdiagram
plt.subplot(2, 2, 3)
plt.bar(x, loaded_data, align='center', alpha=0.5)
plt.xlabel('Idő')
plt.ylabel('Érték')
plt.title('Oszlopdiagram')

# Szórásdiagram
plt.subplot(2, 2, 4)
plt.plot(x, y, 'g-', label='Domború görbe')
plt.fill_between(x, y, color='green', alpha=0.3)
plt.xlabel('Idő')
plt.ylabel('Érték')
plt.title('Domború görbe')

plt.tight_layout()  # Automatikus elrendezés beállítása
plt.show()
