import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

df = pd.read_csv("Nazionalità per anno.csv", encoding="utf-8-sig")

# Prima apparizione di ogni nazione
prima_apparizione = df.groupby("nazionalita")["anno"].min()

# Quante nuove nazioni entrano per ogni anno
nuove_per_anno = prima_apparizione.value_counts().sort_index()

# Cumulata
cumulata = nuove_per_anno.cumsum()

# Reindex per avere tutti gli anni (anche quelli con 0 nuove)
tutti_anni = range(df["anno"].min(), df["anno"].max() + 1)
nuove_per_anno = nuove_per_anno.reindex(tutti_anni, fill_value=0)
cumulata = cumulata.reindex(tutti_anni).ffill().fillna(0)

fig, ax1 = plt.subplots(figsize=(14, 7))

# Barre: nuove nazioni per anno
ax1.bar(nuove_per_anno.index, nuove_per_anno.values,
        color="#e67e22", alpha=0.75, width=0.85,
        label="Nuove nazioni entrate quell'anno")

ax1.set_xlabel("Anno", fontsize=12)
ax1.set_ylabel("Nuove nazioni", fontsize=12, color="#e67e22")
ax1.tick_params(axis="y", labelcolor="#e67e22")
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
ax1.set_ylim(0, nuove_per_anno.max() + 1)

# Linea: cumulata
ax2 = ax1.twinx()
ax2.plot(cumulata.index, cumulata.values, "-",
         color="#2c3e50", linewidth=2.5,
         label="Nazioni cumulate dal 1950")
ax2.set_ylabel("Nazioni totali", fontsize=12, color="#2c3e50")
ax2.tick_params(axis="y", labelcolor="#2c3e50")
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
ax2.set_ylim(0, cumulata.max() + 5)

# Titolo e legenda
ax1.set_title("Nazioni in F1 — Nuove entrate e nazioni totali",
              fontsize=14, fontweight="bold")
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2,
           loc="upper center", fontsize=10)

plt.tight_layout()
plt.show()