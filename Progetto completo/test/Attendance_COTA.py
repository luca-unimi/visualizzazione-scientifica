import pandas as pd
import matplotlib.pyplot as plt

# 1. Leggi il CSV
df = pd.read_csv("Attendance_COTA.csv", encoding="utf-8")

# 2. Assicura tipi numerici (gestisce eventuali celle vuote)
df["weekend_3giorni"] = pd.to_numeric(df["weekend_3giorni"], errors="coerce")
df["domenica"]        = pd.to_numeric(df["domenica"], errors="coerce")

# 3. Ordina per anno
df = df.sort_values("anno").reset_index(drop=True)

# 4. Figura
fig, ax = plt.subplots(figsize=(13, 7))

# --- Barre: affluenza weekend (3 giorni) ---
# Colora in modo diverso l'era pre-COVID e post-COVID
colors = ["#1f77b4" if a <= 2019 else "#2ca02c" for a in df["anno"]]
bars = ax.bar(df["anno"], df["weekend_3giorni"],
              color=colors, width=0.75, label="Weekend (3 giorni)")

# --- Evidenzia il 2020 (anno saltato) ---
ax.axvline(x=2020, color="red", linestyle="--", alpha=0.6, linewidth=1.2)
ax.text(2020, ax.get_ylim()[1] * 0.95, "2020\nnon disputato",
        ha="center", va="top", fontsize=9, color="darkred",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                  edgecolor="darkred", alpha=0.9))

# --- Annota il debutto ---
primo_anno = df["anno"].min()
primo_val  = df.loc[df["anno"] == primo_anno, "weekend_3giorni"].values[0]
ax.annotate(f"Debutto COTA\n".replace(",", "."),
            xy=(primo_anno, primo_val),
            xytext=(primo_anno + 0.3, primo_val + 30_000),
            fontsize=9, color="#1f77b4",
            arrowprops=dict(arrowstyle="->", color="#1f77b4"))

# --- Stile ---
ax.set_xlabel("Anno", fontsize=12)
ax.set_ylabel("Spettatori", fontsize=12)
ax.set_title("Affluenza al Gran Premio degli Stati Uniti (COTA, 2012–2024)",
             fontsize=14, fontweight="bold")
ax.set_xticks(df["anno"])
ax.tick_params(axis="x", rotation=45)
ax.grid(axis="y", alpha=0.3)

# Formato asse Y con separatore delle migliaia
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{int(x):,}".replace(",", ".")))

plt.tight_layout()
plt.show()