import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# 1. Leggi il CSV (una riga per ogni coppia anno-nazione)
df = pd.read_csv("nazioni per season.csv", encoding="utf-8")

# 2. Conta quante nazioni distinte ci sono per ogni anno
nazioni_per_anno = df.groupby("anno")["nazione"].nunique().sort_index()

# 3. Conta anche quante nazioni hanno ospitato più di un GP
gp_per_anno = df.groupby("anno")["nazione"].count().sort_index()
multi_gp = gp_per_anno - nazioni_per_anno

# 4. Figura
fig, ax = plt.subplots(figsize=(14, 7))

anni = nazioni_per_anno.index.values
valori = nazioni_per_anno.values

# Barre con gradiente di colore in base al valore
norm = plt.Normalize(valori.min(), valori.max())
colori = plt.cm.viridis(norm(valori))

bars = ax.bar(anni, valori, color=colori, width=0.85,
              edgecolor="white", linewidth=0.5)

# Evidenzia il 2020 (anno COVID)
if 2020 in nazioni_per_anno.index:
    val_2020 = nazioni_per_anno.loc[2020]
    ax.annotate("2020\n(COVID)",
                xy=(2020, val_2020),
                xytext=(2020, val_2020 + 4),
                ha="center", fontsize=9, color="darkred",
                arrowprops=dict(arrowstyle="->", color="darkred"))

# Stile
ax.set_xlabel("Stagione", fontsize=12)
ax.set_ylabel("Numero di nazioni con almeno un GP", fontsize=12)
ax.set_title("Nazioni ospitanti per stagione di Formula 1 (1950–2025)",
             fontsize=14, fontweight="bold")
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)
ax.yaxis.set_major_locator(MaxNLocator(integer=True))

plt.tight_layout()
plt.xlim((1948, 2028))
plt.show()