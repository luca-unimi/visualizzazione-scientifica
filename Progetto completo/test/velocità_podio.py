import pandas as pd
import matplotlib.pyplot as plt
import re

# 1. Leggi il CSV tollerando i byte rotti
df = pd.read_csv(
    "Category Best Laps.csv",
    encoding="utf-8",
    encoding_errors="replace",
)

# 2. Pulisci spazi e caratteri “curvi”
df["Tempo"] = (
    df["Tempo"]
    .astype(str)
    .str.strip()
    .str.replace("’", "'", regex=False)
    .str.replace("‘", "'", regex=False)
    .str.replace("”", '"', regex=False)
    .str.replace("“", '"', regex=False)
    .str.replace("�", '"', regex=False)
)
df["Categoria"] = df["Categoria"].astype(str).str.strip()

# 3. Converte il tempo in secondi
def to_seconds(t):
    m = re.match(r'^(\d+)\'(\d+)"(\d+)$', t)
    if m:
        minuti, secondi, milli = m.groups()
        return int(minuti) * 60 + int(secondi) + int(milli) / 1000
    if ":" in t:
        minuti, secondi = t.split(":")
        return int(minuti) * 60 + float(secondi)
    return float(t)

def format_lap(secondi):
    minuti = int(secondi // 60)
    resto = secondi - minuti * 60
    return f"{minuti}:{resto:06.3f}"

df["tempo_sec"] = df["Tempo"].apply(to_seconds)
df["Tempo_formattato"] = df["tempo_sec"].apply(format_lap)

# 4. Ordina dal più veloce al più lento
df = df.sort_values("tempo_sec").reset_index(drop=True)

# 5. Inverti l'altezza: tempo più basso = barra più alta
tmax, tmin = df["tempo_sec"].max(), df["tempo_sec"].min()
df["altezza"] = tmax + tmin - df["tempo_sec"]

# 6. Colori: oro, argento, bronzo per le prime 3, blu per le altre
COLORE_ORO     = "#FFD700"
COLORE_ARGENTO = "#C0C0C0"
COLORE_BRONZO  = "#CD7F32"
COLORE_RESTO   = "steelblue"

colori = []
for i in range(len(df)):
    if i == 0:
        colori.append(COLORE_ORO)
    elif i == 1:
        colori.append(COLORE_ARGENTO)
    elif i == 2:
        colori.append(COLORE_BRONZO)
    else:
        colori.append(COLORE_RESTO)

# 7. Plot — altezza invertita (più veloce = più alta)
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df["Categoria"], df["altezza"], color=colori,
              edgecolor="black", linewidth=0.5)

# annotazione con tempo formattato M:SS.mmm
for x, y, t in zip(df["Categoria"], df["altezza"], df["Tempo_formattato"]):
    ax.text(x, y, t, ha="center", va="bottom", fontsize=9)

# 9. Stile
ax.set_xlabel("Categoria")
ax.set_ylabel("Tempo sul giro (invertito)")
ax.set_title("Best Laps per categoria — Spa-Francorchamps")

# rimuove le ticks dell'asse Y
ax.tick_params(axis="y", left=False, labelleft=False)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.ylim(90)
plt.show()

print(df[["Categoria", "tempo_sec", "Tempo_formattato", "altezza"]])