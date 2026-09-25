import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


race= pd.read_csv("F1_Race_Results.csv ")
piloti=pd.read_csv("F1_Driver_Standings.csv")
costruttori=pd.read_csv("F1_Constructor_Standings.csv")


quali2025= pd.read_csv("Formula1_2025Season_QualifyingResults.csv")
quali2026= pd.read_csv("Formula1_2026Season_QualifyingResults.csv")
gare2025= pd.read_csv("Formula1_2025Season_RaceResults.csv")
gare2026= pd.read_csv("Formula1_2026Season_RaceResults.csv")











#russel vs antonelli



"""
def confronto_punti_antonelli_russell2025():
    df = gare2025[gare2025["Driver"].isin(["Kimi Antonelli", "George Russell"])].copy()
    df["Points"] = pd.to_numeric(df["Points"], errors="coerce").fillna(0)
    df = df[["Track", "Driver", "Points"]].reset_index(drop=True)

    kimi = df[df["Driver"] == "Kimi Antonelli"].reset_index(drop=True)
    russell = df[df["Driver"] == "George Russell"].reset_index(drop=True)
   
    plt.figure(figsize=(12, 6))
    plt.plot(kimi["Track"], kimi["Points"], marker="o", linewidth=2, label="Kimi Antonelli", color="tab:blue")
    plt.plot(russell["Track"], russell["Points"], marker="s", linewidth=2, label="George Russell", color="tab:orange")
    plt.title("Confronto punti Kimi Antonelli vs George Russell - 2025")
    plt.xlabel("Gara")
    plt.ylabel("Punti")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("immagini/confronto_punti_antonelli_russell2025.png", dpi=200)
    plt.show()
def confronto_punti_antonelli_russell2026():
    df = gare2026[gare2026["Driver"].isin(["Kimi Antonelli", "George Russell"])].copy()
    df["Points"] = pd.to_numeric(df["Points"], errors="coerce").fillna(0)
    df = df[["Track", "Driver", "Points"]].reset_index(drop=True)

    kimi = df[df["Driver"] == "Kimi Antonelli"].reset_index(drop=True)
    russell = df[df["Driver"] == "George Russell"].reset_index(drop=True)
   
    plt.figure(figsize=(12, 6))
    plt.plot(kimi["Track"], kimi["Points"], marker="o", linewidth=2, label="Kimi Antonelli", color="tab:blue")
    plt.plot(russell["Track"], russell["Points"], marker="s", linewidth=2, label="George Russell", color="tab:orange")
    plt.title("Confronto punti Kimi Antonelli vs George Russell - 2026")
    plt.xlabel("Gara")
    plt.ylabel("Punti")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("immagini/confronto_punti_antonelli_russell2026.png", dpi=200)

    plt.show()
"""

def confronto_punti_cumulati_2025():
    df = gare2025[gare2025["Driver"].isin(["Kimi Antonelli", "George Russell"])].copy()
    df["Points"] = pd.to_numeric(df["Points"], errors="coerce").fillna(0)
    df = df[["Track", "Driver", "Points"]].reset_index(drop=True)

    risultati = {}
    for driver in ["Kimi Antonelli", "George Russell"]:
        subset = df[df["Driver"] == driver].copy().reset_index(drop=True)
        subset["Punti cumulati"] = subset["Points"].cumsum()
        risultati[driver] = subset

    k = risultati["Kimi Antonelli"].copy()
    g = risultati["George Russell"].copy()
    merged = k[["Track", "Punti cumulati"]].rename(columns={"Punti cumulati": "Kimi"}).merge(
        g[["Track", "Punti cumulati"]].rename(columns={"Punti cumulati": "Russell"}),
        on="Track",
        how="inner"
    )
    merged["differenza"] = (merged["Kimi"] - merged["Russell"]).abs()
    max_row = merged.loc[merged["differenza"].idxmax()]

    plt.figure(figsize=(12, 6))
    plt.plot(risultati["Kimi Antonelli"]["Track"], risultati["Kimi Antonelli"]["Punti cumulati"],
             marker="o", linewidth=2, label="Kimi Antonelli", color="tab:blue")
    plt.plot(risultati["George Russell"]["Track"], risultati["George Russell"]["Punti cumulati"],
             marker="s", linewidth=2, label="George Russell", color="tab:orange")

    idx = merged.index.get_loc(merged["differenza"].idxmax())
    x_value = merged.iloc[idx]["Track"]
    y_value = max(merged.iloc[idx]["Kimi"], merged.iloc[idx]["Russell"])
    plt.axvline(x=x_value, color="red", linestyle="--", linewidth=1.5)
    plt.text(x_value, y_value + 2, f"Max gap: {int(max_row['differenza'])} pts", color="red", fontsize=9, ha="left", va="bottom")

    plt.title("Punti cumulati Kimi Antonelli vs George Russell - 2025")
    plt.xlabel("Gara")
    plt.ylabel("Punti cumulati")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("immagini/confronto_punti_cumulati_2025.png", dpi=200)

    plt.show()
def confronto_punti_cumulati_2026():

    df = gare2026[gare2026["Driver"].isin(["Kimi Antonelli", "George Russell"])].copy()
    df["Points"] = pd.to_numeric(df["Points"], errors="coerce").fillna(0)
    df = df[["Track", "Driver", "Points"]].reset_index(drop=True)

    risultati = {}
    for driver in ["Kimi Antonelli", "George Russell"]:
        subset = df[df["Driver"] == driver].copy().reset_index(drop=True)
        subset["Punti cumulati"] = subset["Points"].cumsum()
        risultati[driver] = subset

    k = risultati["Kimi Antonelli"].copy()
    g = risultati["George Russell"].copy()
    merged = k[["Track", "Punti cumulati"]].rename(columns={"Punti cumulati": "Kimi"}).merge(
        g[["Track", "Punti cumulati"]].rename(columns={"Punti cumulati": "Russell"}),
        on="Track",
        how="inner"
    )
    merged["differenza"] = (merged["Kimi"] - merged["Russell"]).abs()
    max_row = merged.loc[merged["differenza"].idxmax()]

    plt.figure(figsize=(12, 6))
    plt.plot(risultati["Kimi Antonelli"]["Track"], risultati["Kimi Antonelli"]["Punti cumulati"],
             marker="o", linewidth=2, label="Kimi Antonelli", color="tab:blue")
    plt.plot(risultati["George Russell"]["Track"], risultati["George Russell"]["Punti cumulati"],
             marker="s", linewidth=2, label="George Russell", color="tab:orange")

    x_value = max_row["Track"]
    y_value = max(max_row["Kimi"], max_row["Russell"])
    plt.axvline(x=x_value, color="red", linestyle="--", linewidth=1.5)
    plt.text(x_value, y_value + 2, f"Max gap: {int(max_row['differenza'])} pts", color="red", fontsize=9, ha="left", va="bottom")

    plt.title("Punti cumulati Kimi Antonelli vs George Russell - 2026")
    plt.xlabel("Gara")
    plt.ylabel("Punti cumulati")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("immagini/confronto_punti_cumulati_2026.png", dpi=200)
    plt.show()


def tempo_a_secondi(valore):
    if pd.isna(valore) or valore == "":
        return np.nan
    if isinstance(valore, str):
        valore = valore.strip()
        if ":" in valore:
            minuti, secondi = valore.split(":")
            return float(minuti) * 60 + float(secondi)
        return float(valore)
    return float(valore)
def confronto_qualifying_kimi_antonelli_2026():
    df = quali2026[quali2026["Driver"] == "Kimi Antonelli"].copy()
    for col in ["Q1", "Q2", "Q3"]:
        df[col] = df[col].apply(tempo_a_secondi)

    df = df[["Track", "Q1", "Q2", "Q3"]].reset_index(drop=True)

    plt.figure(figsize=(12, 6))
    plt.plot(df["Track"], df["Q1"], marker="o", linewidth=2, label="Q1", color="tab:blue")
    plt.plot(df["Track"], df["Q2"], marker="s", linewidth=2, label="Q2", color="tab:orange")
    plt.plot(df["Track"], df["Q3"], marker="^", linewidth=2, label="Q3", color="tab:green")

    plt.title("Kimi Antonelli - Confronto tempi Q1, Q2, Q3 - 2026")
    plt.xlabel("Gara")
    plt.ylabel("Tempo (s)")
    plt.xticks(rotation=45, ha="right")
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("immagini/confronto_qualifying_2026.png", dpi=200)
    plt.show()


def confronto_qualifying_australia_2026():
    df = quali2026[quali2026["Track"] == "Australia"].copy()
    for col in ["Q1", "Q2", "Q3"]:
        df[col] = df[col].apply(tempo_a_secondi)

    df = df[["Driver", "Q1", "Q2", "Q3"]].dropna(subset=["Driver"]).reset_index(drop=True)

    x = np.arange(len(df))
    width = 0.25

    plt.figure(figsize=(16, 8))
    plt.bar(x - width, df["Q1"], width=width, color="tab:blue", label="Q1")
    plt.bar(x, df["Q2"], width=width, color="tab:orange", label="Q2")
    plt.bar(x + width, df["Q3"], width=width, color="tab:green", label="Q3")

    plt.title("Tempi di qualifiche - Australia 2026")
    plt.xlabel("Piloti")
    plt.ylabel("Tempo (s)")
    plt.xticks(x, df["Driver"], rotation=45, ha="right")
    plt.ylim(df[["Q1", "Q2", "Q3"]].min().min() - 0.2, df[["Q1", "Q2", "Q3"]].max().max() + 0.2)
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.savefig("immagini/confronto_qualifying_australia_2026.png", dpi=200)

    plt.show()


def q1_australia_2026_percentuale():
    df = quali2026[quali2026["Track"] == "Australia"].copy()
    df = df[["Driver", "Q1"]].dropna(subset=["Q1"]).copy()
    df["Q1_secondi"] = df["Q1"].map(lambda x: pd.to_timedelta("00:" + str(x)).total_seconds())

    tempo_più_veloce = df["Q1_secondi"].min()
    df["percentuale_vs_fastest"] = (df["Q1_secondi"] / tempo_più_veloce) * 100
    df = df.sort_values("Q1_secondi").reset_index(drop=True)

    colors = ["gold", "silver", "saddlebrown"] + ["steelblue"] * max(0, len(df) - 3)

    plt.figure(figsize=(14, 8))
    plt.barh(df["Driver"], df["percentuale_vs_fastest"], color=colors)
    plt.gca().invert_yaxis()
    plt.axvline(107, color="red", linestyle="--", linewidth=1.5, label="107%")
    plt.title("Q1 GP Australia 2026 - tempo % rispetto al più veloce")
    plt.xlabel("% rispetto al tempo più veloce")
    plt.ylabel("Pilota")
    plt.grid(axis="x", linestyle="--", alpha=0.3)
    plt.legend()

    for i, val in enumerate(df["percentuale_vs_fastest"]):
        plt.text(val + 0.08, i, f"{val:.2f}%", va="center", fontsize=9)

    plt.xlim(df["percentuale_vs_fastest"].min() * 0.98, df["percentuale_vs_fastest"].max() * 1.08)
    plt.tight_layout()
    plt.savefig("immagini/q1_australia_2026_percentuale.png", dpi=200)
    plt.show()


def antonelli_podio_2025():
    df = gare2025[gare2025["Driver"] == "Kimi Antonelli"].copy()
    df["Position"] = pd.to_numeric(df["Position"], errors="coerce")

    counts = {
        
        "Secondo": int((df["Position"] == 2).sum()),
        "Terzo": int((df["Position"] == 3).sum()),
        "Fuori podio": int((df["Position"] > 3).sum())
    }

    labels = list(counts.keys())
    values = list(counts.values())

    colors = [
        "#C0C0C0" if label == "Secondo" else
        "#8B4513" if label == "Terzo" else
        "#1f77b4" if label == "Fuori podio" else
        "#FFD700"
        for label in labels
    ]

    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        values,
        labels=labels,
        autopct=lambda pct: f"{pct * sum(values) / 100:.0f}",
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1.2},
        textprops={"fontsize": 10},
        colors=colors
    )
    plt.title("Kimi Antonelli - posizioni 2025")
    plt.tight_layout()
    plt.savefig("immagini/antonelli_podio_2025.png", dpi=200)
    plt.show()

def antonelli_podio_2026():
    df = gare2026[gare2026["Driver"] == "Kimi Antonelli"].copy()
    df["Position"] = pd.to_numeric(df["Position"], errors="coerce")

    counts = {
        "Primo": int((df["Position"] == 1).sum()),
        "Secondo": int((df["Position"] == 2).sum()),
        "Terzo": int((df["Position"] == 3).sum()),
        "Fuori podio": int((df["Position"] > 3).sum())
    }

    labels = list(counts.keys())
    values = list(counts.values())

    colors = [
        "#FFD700" if label == "Primo" else
        "#C0C0C0" if label == "Secondo" else
        "#8B4513" if label == "Terzo" else
        "#1f77b4"
        for label in labels
    ]

    plt.figure(figsize=(8, 8))
    wedges, texts, autotexts = plt.pie(
        values,
        labels=labels,
        autopct=lambda pct: f"{pct * sum(values) / 100:.0f}",
        startangle=90,
        wedgeprops={"edgecolor": "white", "linewidth": 1.2},
        textprops={"fontsize": 10},
        colors=colors
    )
    plt.title("Kimi Antonelli - posizioni 2026")
    plt.tight_layout()
    plt.savefig("immagini/antonelli_podio_2026.png", dpi=200)

    plt.show()





def confronto_coppie_team_2026_vincite():
    import itertools

    df = gare2026[["Track", "Driver", "Team", "Position"]].copy()
    df["Position"] = pd.to_numeric(df["Position"], errors="coerce")

    total_races = int(df["Track"].nunique())

    def build_rows(source_df):
        rows = []
        for team, team_df in source_df.groupby("Team"):
            drivers = sorted(team_df["Driver"].dropna().unique().tolist())
            if len(drivers) < 2:
                continue

            preferred_pairs = []
            if "Max Verstappen" in drivers and "Isack Hadjar" in drivers:
                preferred_pairs = [("Max Verstappen", "Isack Hadjar")]

            candidate_pairs = preferred_pairs + [
                pair for pair in itertools.combinations(drivers, 2)
                if pair not in preferred_pairs and tuple(reversed(pair)) not in preferred_pairs
            ]

            used_drivers = set()
            for driver_a, driver_b in candidate_pairs:
                if driver_a in used_drivers or driver_b in used_drivers:
                    continue

                pair_df = team_df[team_df["Driver"].isin([driver_a, driver_b])].copy()
                pivot = pair_df.pivot_table(index="Track", columns="Driver", values="Position", aggfunc="first")
                if pivot.empty or driver_a not in pivot.columns or driver_b not in pivot.columns:
                    continue

                used_drivers.update({driver_a, driver_b})

                def compare_positions(row):
                    a = row[driver_a]
                    b = row[driver_b]

                    a_valid = pd.notna(a)
                    b_valid = pd.notna(b)

                    if a_valid and not b_valid:
                        return "A"
                    if b_valid and not a_valid:
                        return "B"
                    if not a_valid and not b_valid:
                        return None
                    if a < b:
                        return "A"
                    if b < a:
                        return "B"
                    return None

                results = pivot.apply(compare_positions, axis=1)
                wins_a = int((results == "A").sum())
                wins_b = int((results == "B").sum())
                pair_total_races = int(len(pivot))

                rows.append({
                    "Team": team,
                    "DriverA": driver_a,
                    "DriverB": driver_b,
                    "WinsA": wins_a,
                    "WinsB": wins_b,
                    "TotalRaces": pair_total_races,
                })

        return pd.DataFrame(rows)

    risultati = build_rows(df)
    if not risultati.empty:
        driver_totals = pd.concat([
            risultati[["DriverA", "WinsA"]].rename(columns={"DriverA": "Driver", "WinsA": "Wins"}),
            risultati[["DriverB", "WinsB"]].rename(columns={"DriverB": "Driver", "WinsB": "Wins"})
        ], ignore_index=True)
        excessive_drivers = driver_totals.groupby("Driver")["Wins"].sum()
        excessive_drivers = excessive_drivers[excessive_drivers > total_races].index.tolist()
        if excessive_drivers:
            df_clean = df.drop_duplicates(subset=["Track", "Driver"], keep="last").reset_index(drop=True)
            risultati = build_rows(df_clean)

    if risultati.empty:
        raise ValueError("Nessuna coppia di piloti con la stessa macchina trovata nel 2026.")

    fig, ax = plt.subplots(figsize=(16, 7))
    x = np.arange(len(risultati))
    width = 0.8

    max_races = int(risultati["TotalRaces"].max())
    seg_a = risultati["WinsA"].astype(float).to_numpy()
    seg_b = risultati["WinsB"].astype(float).to_numpy()

    ax.set_yticks(np.arange(0, max_races + 1, 1))
    ax.set_ylim(0, max_races + 1)
    ax.bar(x, seg_a, width=width, color="#1f77b4", alpha=0.9, label="Driver A")
    ax.bar(x, seg_b, width=width, bottom=seg_a, color="#d62728", alpha=0.85, label="Driver B")

    for i, row in risultati.iterrows():
        label_a = row["DriverA"].replace(" ", "\n", 1)
        label_b = row["DriverB"].replace(" ", "\n", 1)
        ax.text(i, seg_a[i] / 2, label_a, ha="center", va="center", color="white", fontsize=8, fontweight="bold")
        ax.text(i, seg_a[i] + seg_b[i] / 2, label_b, ha="center", va="center", color="white", fontsize=8, fontweight="bold")

    ax.legend(frameon=False)

    ax.set_xticks(x)
    ax.set_xticklabels(risultati["Team"], rotation=25, ha="right")
    ax.set_ylim(0, max_races + 1)
    ax.set_title("Confronto vittorie intra-team in gara - 2026")
    ax.set_xlabel("Macchina / Team")
    ax.set_ylabel("Gare disputate")
    ax.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig("immagini/confronto_coppie_team_2026_vincite.png", dpi=200)
    plt.show()


def antonellivsrussel():
    
    confronto_punti_cumulati_2025()
    confronto_punti_cumulati_2026()
    

antonellivsrussel()

confronto_qualifying_kimi_antonelli_2026()
confronto_qualifying_australia_2026()
q1_australia_2026_percentuale()



antonelli_podio_2025()
antonelli_podio_2026()

#confronto_coppie_team_2026_vincite()

