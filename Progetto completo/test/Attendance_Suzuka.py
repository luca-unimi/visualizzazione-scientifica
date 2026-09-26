import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Leggi il CSV
df = pd.read_csv("Atendance suzuka.csv", encoding="utf-8")

# 2. Pulisci le colonne numeriche (hanno virgole come separatore delle migliaia)
def pulisci(col):
    return (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .replace("", np.nan)
        .astype(float)
    )

for col in ["Thursday", "Friday", "Saturday", "Sunday", "Weekend"]:
    df[col] = pulisci(col)

df = df.sort_values("Year").reset_index(drop=True)

# 3. Figura
fig, ax = plt.subplots(figsize=(14, 7))

anni = df["Year"].astype(str).values

# Barre impilate: giovedì (se presente), venerdì, sabato, domenica
p_venerdi = df["Friday"].fillna(0).values
p_sabato  = df["Saturday"].fillna(0).values
p_domenica = df["Sunday"].fillna(0).values

ax.bar(anni, p_venerdi,  color="#9ecae1", label="Venerdì (prove)")
ax.bar(anni, p_sabato,   bottom=p_venerdi,
       color="#4292c6", label="Sabato (qualifiche)")
ax.bar(anni, p_domenica, bottom=p_venerdi + p_sabato,
       color="#08519c", label="Domenica (gara)")

# 6. Stile
ax.set_xlabel("Stagione", fontsize=12)
ax.set_ylabel("Spettatori (migliaia)", fontsize=12)
ax.set_title("GP del Giappone a Suzuka — Affluenza per stagione (1987–2024)",
             fontsize=14, fontweight="bold")
ax.grid(axis="y", alpha=0.3)
ax.legend(loc="upper right", fontsize=10, framealpha=0.95)

# Formato asse Y con separatore migliaia
ax.yaxis.set_major_formatter(plt.FuncFormatter(
    lambda x, _: f"{int(x):,}".replace(",", ".")))

plt.tight_layout()
plt.show()