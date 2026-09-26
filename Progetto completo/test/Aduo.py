import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

# 1. Leggi il CSV
df = pd.read_csv("Aduo ICE.csv", encoding="utf-8")

# 2. Baseline e soglie ADUO
BASE        = 500
BENCHMARK   = df.loc[df["costruttore"] == "Red Bull-Ford", "potenza_iniziale_hp"].values[0]
SOGLIA_2PCT = BENCHMARK * 0.98   # ~548.8 hp
SOGLIA_4PCT = BENCHMARK * 0.96   # ~537.6 hp

# 3. Colori
COLORE_INIZIALE = "#e0e0e0"
COLORE_ADUO1    = "#2980b9"
COLORE_ADUO2    = "#e74c3c"
COLORE_BORDO    = "#b0b0b0"

# 4. Figura
fig, ax = plt.subplots(figsize=(13, 7))

y_pos = np.arange(len(df))
height = 0.55

# Linee soglia ADUO (dietro le barre)
ax.axvline(SOGLIA_2PCT, color="orange", linestyle="--",
           linewidth=1.5, alpha=0.8, zorder=1)
ax.axvline(SOGLIA_4PCT, color="purple", linestyle="--",
           linewidth=1.5, alpha=0.8, zorder=1)

# Etichette delle soglie (in alto)
ax.text(SOGLIA_2PCT, -0.75, f"Soglia 2%\n({SOGLIA_2PCT:.1f} hp)",
        ha="center", va="bottom", fontsize=9, color="orange",
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                  edgecolor="orange", alpha=0.9))
ax.text(SOGLIA_4PCT, -0.75, f"Soglia 4%\n({SOGLIA_4PCT:.1f} hp)",
        ha="center", va="bottom", fontsize=9, color="purple",
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                  edgecolor="purple", alpha=0.9))

# Barre
for i, row in df.iterrows():
    y       = y_pos[i]
    ini     = row["potenza_iniziale_hp"]
    a1      = row["potenza_aduo1_hp"]
    a2      = row["potenza_aduo2_hp"]
    attuale = row["potenza_attuale_hp"]

    # Barra iniziale (grigio)
    ax.barh(y, ini - BASE, left=BASE, height=height,
            color=COLORE_INIZIALE, edgecolor=COLORE_BORDO,
            linewidth=1, zorder=2)

    # Segmento ADUO 1
    if pd.notna(a1):
        ax.barh(y, a1 - ini, left=ini, height=height,
                color=COLORE_ADUO1, edgecolor="white",
                linewidth=1, zorder=3)
        # Segmento ADUO 2 (solo Ferrari)
        if pd.notna(a2):
            ax.barh(y, a2 - a1, left=a1, height=height,
                    color=COLORE_ADUO2, edgecolor="white",
                    linewidth=1, zorder=4)

    # Etichetta valore attuale
    ax.text(attuale + 0.8, y, f"{attuale:.0f} hp",
            va="center", ha="left", fontsize=11,
            fontweight="bold", color="#333333", zorder=5)

# 5. Stile
ax.set_yticks(y_pos)
ax.set_yticklabels(df["costruttore"], fontsize=12, fontweight="bold")
ax.set_xlabel("Potenza ICE (hp)", fontsize=12)
ax.set_title("F1 2026 — Potenza ICE, aggiornamenti ADUO e soglie di deficit",
             fontsize=14, fontweight="bold", pad=15)
ax.set_xlim(BASE, 580)
ax.set_ylim(len(df) - 0.5, -1.2)   # spazio per le etichette in alto
ax.grid(axis="x", alpha=0.3, linestyle="--", zorder=0)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 6. Legenda in basso a destra
legenda = [
    Patch(facecolor=COLORE_INIZIALE, edgecolor=COLORE_BORDO, label="Potenza iniziale"),
    Patch(facecolor=COLORE_ADUO1,    edgecolor="white",       label="ADUO 1"),
    Patch(facecolor=COLORE_ADUO2,    edgecolor="white",       label="ADUO 2 (Ferrari)"),
    plt.Line2D([0], [0], color="orange", linestyle="--",      label=f"Soglia 2% ({SOGLIA_2PCT:.1f} hp)"),
    plt.Line2D([0], [0], color="purple", linestyle="--",      label=f"Soglia 4% ({SOGLIA_4PCT:.1f} hp)"),
]
ax.legend(handles=legenda, loc="lower right",
          fontsize=9, framealpha=0.95, edgecolor="gray")

plt.tight_layout()
plt.show()