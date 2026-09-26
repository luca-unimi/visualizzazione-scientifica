import pandas as pd
import matplotlib.pyplot as plt

# 1. Leggi il CSV
df = pd.read_csv("circuit_economics.csv", encoding="utf-8")

# 2. Totale affluenza per stagione (i valori sono in migliaia)
tot_per_anno = (
    df.groupby("season")["weekend_attendance_k"]
      .sum()
      .sort_index()
)

# 3. Numero di GP per stagione (per contesto)
gp_per_anno = df.groupby("season")["grand_prix"].count().sort_index()

# 4. Unisci in un unico DataFrame
riepilogo = pd.DataFrame({
    "totale_k": tot_per_anno,
    "num_gp":   gp_per_anno,
})
riepilogo["media_per_gp_k"] = riepilogo["totale_k"] / riepilogo["num_gp"]

# 5. Grafico
fig, ax = plt.subplots(figsize=(14, 7))

# Barre: totale affluenza stagionale
colors = ["#d62728" if a == 2020 else "#1f77b4" for a in riepilogo.index]
bars = ax.bar(riepilogo.index, riepilogo["totale_k"],
              color=colors, width=0.75, label="Affluenza totale stagione")

# Evidenzia il 2020
ax.annotate("2020\n(COVID-19)",
            xy=(2020, riepilogo.loc[2020, "totale_k"]),
            xytext=(2020, riepilogo["totale_k"].max() * 0.4),
            ha="center", fontsize=9, color="darkred", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="darkred"))

# Stile
ax.set_xlabel("Stagione", fontsize=12)
ax.set_ylabel("Affluenza totale (migliaia di spettatori)", fontsize=12)
ax.set_title("Affluenza totale per stagione di Formula 1 (2010–2026)",
             fontsize=14, fontweight="bold")
ax.set_xticks(riepilogo.index)
ax.tick_params(axis="x", rotation=45)
ax.grid(axis="y", alpha=0.3)

# Formato asse Y con separatore migliaia
ax.yaxis.set_major_formatter(plt.FuncFormatter(
    lambda x, _: f"{int(x):,}".replace(",", ".")))

plt.tight_layout()
plt.show()
