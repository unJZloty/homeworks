import numpy as np

# Создаем массив из чисел
arr = np.array([1, 2, 3, 4, 5])

# Умножаем каждый элемент на 3
arr_mp = arr * 3

# Находим среднее значение
mean_value = np.mean(arr)

# Находим сумму всех элементов
sum_value = np.sum(arr)

print("Массив:", arr)
print("Умноженный на 3 массив:", arr_mp)
print("Среднее значение:", mean_value)
print("Сумма элементов:", sum_value)


import matplotlib.pyplot as plt

# Данные для визуализации
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Создаем график
plt.plot(x, y)

# Добавляем заголовок и подписи осей
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")

# Показать график
plt.show()


from PIL import Image, ImageFilter

# Открываем изображение
image = Image.open("image.jpg")

# Изменяем размер
resized_image = image.resize((300, 300))

# Применяем размытие
blurred_image = resized_image.filter(ImageFilter.BLUR)

# Сохраняем новое изображение
blurred_image.save("blurred_image.png")
