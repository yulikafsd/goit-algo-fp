import numpy as np
import pandas as pd

# Аналітичні дані з завдання
analytical_probs = {
    2: "2.78% (1/36)",
    3: "5.56% (2/36)",
    4: "8.33% (3/36)",
    5: "11.11% (4/36)",
    6: "13.89% (5/36)",
    7: "16.67% (6/36)",
    8: "13.89% (5/36)",
    9: "11.11% (4/36)",
    10: "8.33% (3/36)",
    11: "5.56% (2/36)",
    12: "2.78% (1/36)",
}


# Симуляція кидання двох кубиків
def monte_carlo_simulation(num_throws=100_000):
    dice1 = np.random.randint(1, 7, size=num_throws)
    dice2 = np.random.randint(1, 7, size=num_throws)
    sums = dice1 + dice2
    counts = {total: np.sum(sums == total) for total in range(2, 13)}
    return counts


# Побудова таблиці ймовірностей
def display_probability_table(counts, num_throws):
    table_data = []
    for total in range(2, 13):
        count = counts.get(total, 0)
        percent_sim = count / num_throws * 100

        # Порівняння симуляції з аналітикою
        analytical_percent = float(analytical_probs[total].split("%")[0])
        diff = percent_sim - analytical_percent
        table_data.append(
            {
                "Сума": total,
                "Імовірність (симуляція)": f"{percent_sim:.2f}%",
                "Імовірність (аналітична)": analytical_probs[total],
                "Похибка (%)": f"{diff:.2f}",
            }
        )
    df = pd.DataFrame(table_data)
    avg_diff = df["Похибка (%)"].astype(float).abs().mean()
    return df, avg_diff


if __name__ == "__main__":
    num_throws = 1_000_000
    counts = monte_carlo_simulation(num_throws)
    table, avg_diff = display_probability_table(counts, num_throws)

    print(table.to_string(index=False))
    print(
        f"\nСереднє абсолютне відхилення симуляційної ймовірності від аналітичної: {avg_diff:.2f}%"
    )
