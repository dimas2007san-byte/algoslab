import csv
import math
import matplotlib.pyplot as plt


def f(x, y):
    return x * math.exp(-(x ** 2)) - 2 * x * y


def exact_solution(x):
    return (1 + x ** 2 / 2) * math.exp(-(x ** 2))


start = 0
end = 1
h = 0.05
y0 = 1
steps = int(round((end - start) / h))


x_values = []
for i in range(steps + 1):
    x_values.append(start + i * h)


euler_values = [y0]
rk4_values = [y0]


for i in range(steps):
    x = x_values[i]

    y = euler_values[i]
    next_y = y + h * f(x, y)
    euler_values.append(next_y)

    y = rk4_values[i]
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    k3 = h * f(x + h / 2, y + k2 / 2)
    k4 = h * f(x + h, y + k3)
    next_y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    rk4_values.append(next_y)


exact_values = []
for x in x_values:
    exact_values.append(exact_solution(x))


print("x", "Точное решение", "Эйлер", "Рунге-Кутта 4")
for i in range(steps + 1):
    print(round(x_values[i], 2), round(exact_values[i], 10),
          round(euler_values[i], 10), round(rk4_values[i], 10))


euler_error = abs(exact_values[-1] - euler_values[-1])
rk4_error = abs(exact_values[-1] - rk4_values[-1])

print()
print("Точное y(1):", round(exact_values[-1], 12))
print("Ошибка метода Эйлера:", euler_error)
print("Ошибка метода Рунге-Кутты 4:", rk4_error)


with open("results.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["x", "Точное решение", "Эйлер", "Рунге-Кутта 4"])

    for i in range(steps + 1):
        writer.writerow([
            round(x_values[i], 2),
            round(exact_values[i], 12),
            round(euler_values[i], 12),
            round(rk4_values[i], 12),
        ])


plt.plot(x_values, exact_values, label="Точное решение")
plt.plot(x_values, euler_values, "o-", label="Метод Эйлера")
plt.plot(x_values, rk4_values, "o-", label="Рунге-Кутта 4")
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Решение задачи Коши")
plt.grid(True)
plt.legend()
plt.savefig("solutions.png", dpi=150)
plt.close()

print()
print("Таблица сохранена в results.csv")
print("График сохранён в solutions.png")
