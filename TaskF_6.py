items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = []

    for item, details in sorted_items:
        if budget >= details['cost']:
            budget -= details['cost']
            total_calories += details['calories']
            selected_items.append(item)

    return selected_items, total_calories

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item, details = item_list[i - 1]
        cost, calories = details['cost'], details['calories']

        for b in range(budget + 1):
            if b < cost:
                dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)

    total_calories = dp[n][budget]
    selected_items = []
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            item, details = item_list[i - 1]
            selected_items.append(item)
            b -= details['cost']

    selected_items.reverse()
    return selected_items, total_calories

budget = 100
print("Жадібний алгоритм")
greedy_result = greedy_algorithm(items, budget)
print("Вибрані елементи:", greedy_result[0])
print("Загальна кількість калорій:", greedy_result[1])

print("\nДинамічне програмування")
dynamic_result = dynamic_programming(items, budget)
print("Вибрані елементи:", dynamic_result[0])
print("Загальна кількість калорій:", dynamic_result[1])
