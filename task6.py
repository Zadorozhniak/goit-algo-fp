def greedy_algorithm(items, budget):
    # Створюємо список страв з їхніми характеристиками та співвідношенням калорій/вартість
    item_list = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        item_list.append({
            "name": name,
            "cost": info["cost"],
            "calories": info["calories"],
            "ratio": ratio
        })
    
    # Сортуємо страви за співвідношенням калорій до вартості (спадання)
    sorted_items = sorted(item_list, key=lambda x: x["ratio"], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    # Вибираємо страви починаючи з найвищчим співвідношенням
    for item in sorted_items:
        if total_cost + item["cost"] <= budget:
            selected_items.append(item["name"])
            total_cost += item["cost"]
            total_calories += item["calories"]
    
    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }

def dynamic_programming(items, budget):
    # Перетворюємо словник у список для зручності
    item_list = []
    for name, info in items.items():
        item_list.append((name, info["cost"], info["calories"]))
    
    n = len(item_list)
    # Створюємо таблицю DP де dp[i][j] - максимальні калорії для бюджету j з першими i стравами
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        name, cost, calories = item_list[i-1]
        for j in range(budget + 1):
            if cost > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + calories)
    
    # Відновлюємо набір страв
    selected_items = []
    remaining_budget = budget
    total_calories = dp[n][budget]
    
    for i in range(n, 0, -1):
        if dp[i][remaining_budget] != dp[i-1][remaining_budget]:
            name, cost, calories = item_list[i-1]
            selected_items.append(name)
            remaining_budget -= cost
    
    return {
        "selected_items": selected_items,
        "total_cost": budget - remaining_budget,
        "total_calories": total_calories
    }

# Приклад використання
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

print("Жадібний алгоритм:")
greedy_result = greedy_algorithm(items, budget)
print(greedy_result)

print("\nДинамічне програмування:")
dp_result = dynamic_programming(items, budget)
print(dp_result)