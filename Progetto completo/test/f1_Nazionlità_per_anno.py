import pandas as pd
import matplotlib.pyplot as plt

# 1. Carica il CSV
df = pd.read_csv("Nazionalità per anno.csv", encoding="utf-8-sig")

# 2. Statistiche per anno
naz_per_year    = df.groupby("anno")["nazionalita"].nunique().sort_index()
piloti_per_year = df.groupby("anno")["num_piloti"].sum().sort_index()

# 3. Cumulata: quante nazionalità UNICHE sono apparse dal 1950 fino a quell'anno
visti = set()
cum_naz = []
for anno, gruppo in df.sort_values("anno").groupby("anno"):
    visti.update(gruppo["nazionalita"].unique())
    cum_naz.append(len(visti))
cum_naz = pd.Series(cum_naz, index=sorted(df["anno"].unique()))


# ============================================================
# FIGURA 1 — Nazionalità distinte per stagione
# ============================================================
plt.figure(figsize=(12, 6))

colors = ["#d62728" if a <= 1960 else "#1f77b4" for a in naz_per_year.index]
plt.bar(naz_per_year.index, naz_per_year.values, color=colors, width=0.9)
plt.axvspan(1949.5, 1960.5, color="red", alpha=0.08)
plt.text(1955, naz_per_year.max() * 0.95,
         "Era Indy 500\n(1950–1960)",
         ha="center", va="top", fontsize=9, color="darkred")

plt.title("Nazionalità distinte per stagione")
plt.xlabel("Anno")
plt.ylabel("Numero di nazionalità")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# FIGURA 2 — Curva cumulata delle nazionalità
# ============================================================
plt.figure(figsize=(12, 6))

plt.plot(cum_naz.index, cum_naz.values, marker="o", markersize=3,
         color="darkgreen", linewidth=1.8)
plt.fill_between(cum_naz.index, cum_naz.values, alpha=0.2, color="green")
plt.axvspan(1949.5, 1960.5, color="red", alpha=0.08)

primo  = cum_naz.index[0]
ultimo = cum_naz.index[-1]
plt.annotate(f"{cum_naz.iloc[0]} nel {primo}",
             xy=(primo, cum_naz.iloc[0]),
             xytext=(primo + 5, cum_naz.iloc[0] + 5),
             fontsize=9,
             arrowprops=dict(arrowstyle="->", color="gray"))
plt.annotate(f"{cum_naz.iloc[-1]} nel {ultimo}",
             xy=(ultimo, cum_naz.iloc[-1]),
             xytext=(ultimo - 25, cum_naz.iloc[-1] - 8),
             fontsize=9,
             arrowprops=dict(arrowstyle="->", color="gray"))

plt.title("Crescita cumulata delle nazionalità (uniche dal 1950)")
plt.xlabel("Anno")
plt.ylabel("Nazionalità totali mai viste fino a quell'anno")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# FIGURA 3 — Piloti totali per stagione
# ============================================================
plt.figure(figsize=(12, 6))

plt.plot(piloti_per_year.index, piloti_per_year.values,
         color="purple", linewidth=1.5)
plt.fill_between(piloti_per_year.index, piloti_per_year.values,
                 alpha=0.2, color="purple")
plt.axvspan(1949.5, 1960.5, color="red", alpha=0.08)
plt.text(1955, piloti_per_year.max() * 0.95,
         "Picco dovuto\nall'Indy 500",
         ha="center", va="top", fontsize=9, color="darkred")

plt.title("Piloti totali per stagione")
plt.xlabel("Anno")
plt.ylabel("Numero di piloti")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()


# ============================================================
# Riepilogo testuale
# ============================================================
print("Nazionalità totali distinte dal 1950 ad oggi:", cum_naz.iloc[-1])
print("Nazionalità nel 1950:", cum_naz.iloc[0])
print("Picco nazionalità in un anno:",
      naz_per_year.max(), "nel", naz_per_year.idxmax())