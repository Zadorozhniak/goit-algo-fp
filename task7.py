import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(num_rolls):
    # Підрахунок сум
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Симуляція кидків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sums_count[total] += 1
    
    # Обчислення ймовірностей
    probabilities = {k: v / num_rolls for k, v in sums_count.items()}
    
    return sums_count, probabilities

def theoretical_probabilities():
    theory = {
        2: 1/36,
        3: 2/36,
        4: 3/36,
        5: 4/36,
        6: 5/36,
        7: 6/36,
        8: 5/36,
        9: 4/36,
        10: 3/36,
        11: 2/36,
        12: 1/36
    }
    return theory

def print_comparison(monte_carlo_probs, theory_probs):
    print("Сума | Монте-Карло | Теоретична | Різниця")
    print("-----|-------------|------------|--------")
    for sum_val in range(2, 13):
        mc_prob = monte_carlo_probs[sum_val]
        th_prob = theory_probs[sum_val]
        diff = abs(mc_prob - th_prob)
        print(f"{sum_val:4} | {mc_prob:.4f}     | {th_prob:.4f}    | {diff:.4f}")

def plot_probabilities(monte_carlo_probs, theory_probs):
    sums = list(range(2, 13))
    mc_probs = [monte_carlo_probs[s] for s in sums]
    th_probs = [theory_probs[s] for s in sums]
    
    plt.figure(figsize=(10, 6))
    plt.bar([s - 0.2 for s in sums], mc_probs, width=0.4, label='Монте-Карло', alpha=0.7)
    plt.bar([s + 0.2 for s in sums], th_probs, width=0.4, label='Теоретична', alpha=0.7)
    plt.xlabel('Сума кубиків')
    plt.ylabel('Ймовірність')
    plt.title('Порівняння ймовірностей сум кубиків')
    plt.xticks(sums)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

# Осн. частина програми
if __name__ == "__main__":
    num_rolls = 1000000  
    
    print(f"Симуляція {num_rolls} кидків двох кубиків...")
    sums_count, monte_carlo_probs = monte_carlo_dice_simulation(num_rolls)
    theory_probs = theoretical_probabilities()
    
    
    print("\nРезультати симуляції:")
    print_comparison(monte_carlo_probs, theory_probs)
    
    # Графік
    plot_probabilities(monte_carlo_probs, theory_probs)