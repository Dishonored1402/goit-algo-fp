import random
import matplotlib.pyplot as plt

def monte_carlo_dice_simulation(throws):
    sums_frequency = {i: 0 for i in range(2, 13)}

    for _ in range(throws):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        total_sum = dice_1 + dice_2
        sums_frequency[total_sum] += 1

    probabilities = {k: v / throws for k, v in sums_frequency.items()}
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color="skyblue", edgecolor="black")
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Ймовірність сум за методом Монте-Карло")
    plt.xticks(range(2, 13))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    throws = 100000
    probabilities_mc = monte_carlo_dice_simulation(throws)

    print("Ймовірності сум за методом Монте-Карло:")
    for total, prob in probabilities_mc.items():
        print(f"Сума {total}: {prob:.4f}")

    plot_probabilities(probabilities_mc)

    analytical_probs = {
        2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
        7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
    }

    print("\nАналітичні ймовірності:")
    for total, prob in analytical_probs.items():
        print(f"Сума {total}: {prob:.4f}")

    plt.bar(analytical_probs.keys(), analytical_probs.values(), color="lightgreen", label="Аналітичні", alpha=0.7)
    plt.bar(probabilities_mc.keys(), probabilities_mc.values(), color="skyblue", label="Монте-Карло", alpha=0.7)
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність")
    plt.title("Порівняння ймовірностей: Аналітичні vs Монте-Карло")
    plt.xticks(range(2, 13))
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
