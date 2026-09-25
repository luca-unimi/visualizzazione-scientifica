import pandas as pd
import matplotlib.pyplot as plt
import re

"""df = pd.read_csv(
    "Category Best Laps.csv",
    encoding="utf-8",
    encoding_errors="replace",
)

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
df["Tempo_formattato"] = df["tempo_sec"].apply(format_lap)   # ← nuova colonna

df = df.sort_values("tempo_sec").reset_index(drop=True)

tmax, tmin = df["tempo_sec"].max(), df["tempo_sec"].min()
df["altezza"] = tmax + tmin - df["tempo_sec"]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["Categoria"], df["altezza"], color="steelblue")

# annotazione con il tempo formattato M:SS.mmm
for x, y, t in zip(df["Categoria"], df["altezza"], df["Tempo_formattato"]):
    ax.text(x, y, t, ha="center", va="bottom", fontsize=9)

ax.set_xlabel("Categoria")
ax.set_ylabel("Tempo sul giro")
ax.set_title("Best Laps per categoria a Spa-Francorchamps")
plt.xticks(rotation=45, ha="right")
plt.yticks([])
plt.ylim(90)
plt.tight_layout()
plt.show()

print(df[["Categoria", "tempo_sec", "Tempo_formattato"]])"""




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

# 4. Ordina dal più veloce al più lento (barre basse → alte)
df = df.sort_values("tempo_sec").reset_index(drop=True)

# 5. Plot — altezza = tempo reale, nessuna inversione
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["Categoria"], df["tempo_sec"], color="steelblue")

# annotazione con tempo formattato M:SS.mmm
for x, y, t in zip(df["Categoria"], df["tempo_sec"], df["Tempo_formattato"]):
    ax.text(x, y, t, ha="center", va="bottom", fontsize=9)

ax.set_xlabel("Categoria")
ax.set_ylabel("Tempo sul giro")
ax.set_title("Best Laps per categoria — Spa-Francorchamps")

# rimuove le ticks dell'asse Y (se vuoi)
ax.tick_params(axis="y", left=False, labelleft=False)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.ylim(90)
plt.show()

print(df[["Categoria", "tempo_sec", "Tempo_formattato"]])