import time


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


# Жадібний алгоритм
def greedy_algorithm(budget, foods):
    sorted_foods = sorted(
        foods.items(),
        key=lambda item: item[1]["calories"] / item[1]["cost"],
        reverse=True,
    )
    result = {}
    total_cost = 0
    total_calories = 0

    for name, data in sorted_foods:
        if total_cost + data["cost"] <= budget:
            result[name] = 1
            total_cost += data["cost"]
            total_calories += data["calories"]

    return result, total_cost, total_calories


# Динамічне програмування
def dynamic_programming(budget, foods):
    food_names = list(foods.keys())
    n = len(food_names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    keep = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = food_names[i - 1]
        cost = foods[name]["cost"]
        calories = foods[name]["calories"]
        for b in range(budget + 1):
            if cost <= b:
                if dp[i - 1][b - cost] + calories > dp[i - 1][b]:
                    dp[i][b] = dp[i - 1][b - cost] + calories
                    keep[i][b] = 1
                else:
                    dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = dp[i - 1][b]

    # Відновлюємо набір страв
    result = {}
    b = budget
    total_cost = 0
    total_calories = 0
    for i in range(n, 0, -1):
        if keep[i][b]:
            name = food_names[i - 1]
            result[name] = 1
            total_cost += foods[name]["cost"]
            total_calories += foods[name]["calories"]
            b -= foods[name]["cost"]

    return result, total_cost, total_calories


if __name__ == "__main__":
    budget = 100
    greedy_result, greedy_cost, greedy_cal = greedy_algorithm(budget, items)
    dp_result, dp_cost, dp_cal = dynamic_programming(budget, items)

    print("----- Жадібний алгоритм -----")
    print(f"Вибрані страви: {greedy_result}")
    print(f"Витрачено бюджету: {greedy_cost}")
    print(f"Сумарні калорії: {greedy_cal}")

    print("----- Динамічне програмування -----")
    print(f"Вибрані страви: {dp_result}")
    print(f"Витрачено бюджету: {dp_cost}")
    print(f"Сумарні калорії: {dp_cal}")
