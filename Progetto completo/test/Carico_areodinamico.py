import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Leggi il CSV
df = pd.read_csv("Valori carico areodinamico.csv", encoding="utf-8")

# 2. Escludi la riga "Totale" per i grafici (la usiamo solo per annotazione)
df_comp = df[df["componente"] != "Totale"].reset_index(drop=True)
tot_2025 = df.loc[df["componente"] == "Totale", "2025_kg"].values[0]
tot_2026 = df.loc[df["componente"] == "Totale", "2026_kg"].values[0]

componenti = df_comp["componente"].tolist()
n = len(componenti)
x = np.arange(n)
width = 0.38

# 3. Figura con due pannelli
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# ============================================================
# PANNELLO SINISTRO — Barre raggruppate (kg)
# ============================================================
bars1 = ax1.bar(x - width/2, df_comp["2025_kg"], width,
                label="2025", color="#1f77b4", edgecolor="white")
bars2 = ax1.bar(x + width/2, df_comp["2026_kg"], width,
                label="2026", color="#d62728", edgecolor="white")

# Etichette sopra le barre
for b in bars1:
    ax1.text(b.get_x() + b.get_width()/2, b.get_height() + 30,
             f"{int(b.get_height()):,}".replace(",", "."),
             ha="center", va="bottom", fontsize=9, color="#1f77b4",
             fontweight="bold")
for b in bars2:
    ax1.text(b.get_x() + b.get_width()/2, b.get_height() + 30,
             f"{int(b.get_height()):,}".replace(",", "."),
             ha="center", va="bottom", fontsize=9, color="#d62728",
             fontweight="bold")

# Delta in percentuale tra i due anni
for i, (v25, v26) in enumerate(zip(df_comp["2025_kg"], df_comp["2026_kg"])):
    delta = (v26 - v25) / v25 * 100
    y_pos = max(v25, v26) + 150
    ax1.text(i, y_pos, f"{delta:+.0f}%", ha="center",
             fontsize=9, color="black", style="italic")

ax1.set_xticks(x)
ax1.set_xticklabels(componenti, rotation=15, ha="right", fontsize=10)
ax1.set_ylabel("Carico aerodinamico (kg)", fontsize=12)
ax1.set_title("Valori assoluti per componente", fontsize=13, fontweight="bold")
ax1.grid(axis="y", alpha=0.3)
ax1.legend(fontsize=11, loc="upper left")
ax1.set_ylim(0, max(df_comp["2025_kg"].max(), df_comp["2026_kg"].max()) * 1.25)

# Annotazione totale
ax1.text(0.98, 0.95,
         f"Totale 2025: {int(tot_2025):,} kg\nTotale 2026: {int(tot_2026):,} kg".replace(",", "."),
         transform=ax1.transAxes, ha="right", va="top", fontsize=10,
         bbox=dict(boxstyle="round,pad=0.4", facecolor="#f0f0f0",
                   edgecolor="gray", alpha=0.9))

# ============================================================
# PANNELLO DESTRO — Barre impilate (%)
# ============================================================
# Prepariamo i dati impilati: 2025 e 2026 come due barre verticali
colori = ["#2c3e50", "#3498db", "#e74c3c", "#f39c12"]

bottom_2025 = 0
bottom_2026 = 0

for i, (comp, colore) in enumerate(zip(componenti, colori)):
    v25 = df_comp.loc[i, "2025_perc"]
    v26 = df_comp.loc[i, "2026_perc"]

    ax2.bar(0, v25, bottom=bottom_2025, color=colore,
            edgecolor="white", width=0.5, label=comp)
    ax2.bar(1, v26, bottom=bottom_2026, color=colore,
            edgecolor="white", width=0.5)

    # Etichetta dentro il segmento
    if v25 > 8:
        ax2.text(0, bottom_2025 + v25/2, f"{v25:.1f}%",
                 ha="center", va="center", fontsize=10,
                 color="white", fontweight="bold")
    if v26 > 8:
        ax2.text(1, bottom_2026 + v26/2, f"{v26:.1f}%",
                 ha="center", va="center", fontsize=10,
                 color="white", fontweight="bold")

    bottom_2025 += v25
    bottom_2026 += v26

ax2.set_xticks([0, 1])
ax2.set_xticklabels(["2025", "2026"], fontsize=12, fontweight="bold")
ax2.set_ylabel("Percentuale del carico totale (%)", fontsize=12)
ax2.set_title("Composizione percentuale", fontsize=13, fontweight="bold")
ax2.set_ylim(0, 100)
ax2.grid(axis="y", alpha=0.3)
ax2.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=10)

plt.tight_layout()
plt.show()