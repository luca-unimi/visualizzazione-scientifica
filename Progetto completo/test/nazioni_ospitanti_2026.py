import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


df = pd.read_csv("nazioni stagione 2026.csv", encoding="utf-8")
df = df.sort_values("gp_ospitati", ascending=True).reset_index(drop=True)


fig, ax = plt.subplots(figsize=(11, 9))

bars = ax.barh(df["nazione"], df["gp_ospitati"],
               edgecolor="white", linewidth=0.8)

# Stile
ax.set_xlabel("Numero di GP ospitati", fontsize=12)
ax.set_ylabel("Nazione", fontsize=12)
ax.set_title("Stagione F1 2026 — GP ospitati per nazione",
             fontsize=14, fontweight="bold", pad=15)
ax.grid(axis="x", alpha=0.3, linestyle="--")
ax.set_axisbelow(True)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_xlim(0, df["gp_ospitati"].max() + 0.6)

plt.tight_layout()
plt.show()