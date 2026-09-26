import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("velocita.csv")

# variabili lette dal CSV
anni      = df["anno"].tolist()
vel_media = df["vel_media"].tolist()
top_speed = df["top_speed"].tolist()
tempi_str = df["tempo_giro"].tolist()

# ------------------------------------------------------------
# FIGURA: grafico a sinistra, tabella a destra
# ------------------------------------------------------------
fig, (ax_graf, ax_tab) = plt.subplots(
    1, 2,
    figsize=(16, 7),
    gridspec_kw={"width_ratios": [1.4, 1]}
)

# ============================================================
# PANNELLO SINISTRO — Grafico velocità media
# ============================================================
ax_graf.plot(anni, vel_media, "o-", color="#1f77b4",
             linewidth=2.5, markersize=8, label="Velocità media giro")
ax_graf.fill_between(anni, vel_media, alpha=0.15, color="#1f77b4")

# Sfondi per ere tecnologiche
ax_graf.axvspan(1999, 2005.5, alpha=0.07, color="blue")
ax_graf.axvspan(2005.5, 2013.5, alpha=0.07, color="orange")
ax_graf.axvspan(2013.5, 2021.5, alpha=0.07, color="green")
ax_graf.axvspan(2021.5, 2025.5, alpha=0.07, color="purple")
ax_graf.axvspan(2025.5, 2026.5, alpha=0.07, color="red")

# Linee tratteggiate per i cambi di regolamento
for x, lab in [(2000, "V10"), (2006, "V10→V8"), (2014, "V8→V6 Turbo"),
               (2022, "Effetto suolo"), (2026, "Nuove regole")]:
    ax_graf.axvline(x=x, color="gray", linestyle="--", alpha=0.6, linewidth=1)
    ax_graf.text(x, max(vel_media) + 3, lab, rotation=90,
                 ha="right", va="top", fontsize=8, color="gray")

"""# Etichette ere
ax_graf.text(2002.5, max(vel_media) + 1, "V10", ha="center",
             fontsize=10, color="blue", fontweight="bold")
ax_graf.text(2009.5, max(vel_media) + 1, "V8", ha="center",
             fontsize=10, color="orange", fontweight="bold")
ax_graf.text(2017.5, max(vel_media) + 1, "V6 Turbo Ibrido", ha="center",
             fontsize=10, color="green", fontweight="bold")
ax_graf.text(2023.5, max(vel_media) + 1, "2022", ha="center",
             fontsize=9, color="purple", fontweight="bold")
ax_graf.text(2025.8, max(vel_media) + 1, "2026", ha="center",
             fontsize=9, color="red", fontweight="bold")"""

ax_graf.set_xlabel("Anno", fontsize=12)
ax_graf.set_ylabel("Velocità media del giro (km/h)", fontsize=12)
ax_graf.set_title("Monza — Velocità media del giro", fontsize=13, fontweight="bold")
ax_graf.set_ylim(240, max(vel_media) + 8)
ax_graf.grid(axis="y", alpha=0.3)
ax_graf.legend(loc="lower right", fontsize=10)

# ============================================================
# PANNELLO DESTRO — Tabella
# ============================================================
ax_tab.axis("off")

col_labels = ["Anno", "Top speed\n(km/h)", "Vel. media\n(km/h)", "Tempo\ngiro"]
table_data = []
for a, ts, vm, t in zip(anni, top_speed, vel_media, tempi_str):
    table_data.append([str(a), f"{ts:.1f}", f"{vm:.1f}", t])

tabella = ax_tab.table(
    cellText=table_data,
    colLabels=col_labels,
    cellLoc="center",
    loc="center",
    colWidths=[0.18, 0.28, 0.28, 0.22]
)

tabella.auto_set_font_size(False)
tabella.set_fontsize(11)
tabella.scale(1, 1.8)

# Stile intestazione
for i in range(len(col_labels)):
    cell = tabella[0, i]
    cell.set_facecolor("#2c3e50")
    cell.set_text_props(color="white", fontweight="bold")

# Colora le celle in base all'era
colori_ere = ["#dbe9f6", "#fdebd0", "#d5f5e3", "#e8daef", "#fadbd8"]
for riga in range(1, len(table_data) + 1):
    anno_riga = int(table_data[riga - 1][0])
    if anno_riga <= 2005:
        col = colori_ere[0]
    elif anno_riga <= 2013:
        col = colori_ere[1]
    elif anno_riga <= 2021:
        col = colori_ere[2]
    elif anno_riga <= 2025:
        col = colori_ere[3]
    else:
        col = colori_ere[4]
    for j in range(len(col_labels)):
        tabella[riga, j].set_facecolor(col)

ax_tab.set_title("Top speed vs prestazione sul giro",
                 fontsize=13, fontweight="bold", pad=20)

# ------------------------------------------------------------
# Titolo generale
# ------------------------------------------------------------
fig.suptitle(
    "Monza: la top speed resta stabile (o cala), ma i tempi sul giro migliorano\n"
    "grazie a downforce, efficienza aerodinamica e gestione del drag",
    fontsize=14, fontweight="bold", y=1.02
)

plt.tight_layout()
plt.show()