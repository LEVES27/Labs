import math

def zminni(a, m, b):
    # Обчислюємо середнє значення (Математичне очікування) E
    E = (a + 4*m + b) / 6
    # Обчислюємо стандартне відхилення SD
    SD = (b - a) / 6
    return E, SD

tasks = []
while True:
    # Запитуємо користувача про числа для завдання
    a = float(input("Enter the 'a' number for a task (or enter '0' to finish): "))
    if a == 0:
        break
    m = float(input("Enter the 'm' number for the same task: "))
    b = float(input("Enter the 'b' number for the same task: "))
    tasks.append((a, m, b))

# Обчислюємо середні значення (Математичне очікування) E та стандартні відхилення SD для кожного завдання
E_tasks, SD_tasks = zip(*[zminni(*task) for task in tasks])

# Обчислюємо суму середніх значень (Математичних очікувань) E для всіх завдань
E_project = sum(E_tasks)
# Обчислюємо загальне стандартне відхилення SD для всіх завдань
SD_project = math.sqrt(sum(sd**2 for sd in SD_tasks))

# Обчислюємо довірчий інтервал 95% для проекту
CI_min = E_project - 2*SD_project
CI_max = E_project + 2*SD_project

# Виводимо результати довірчого інтервалу 95% для проекту
print(f"Project's 95% confidence interval: {CI_min:.2f} ... {CI_max:.2f} points")
