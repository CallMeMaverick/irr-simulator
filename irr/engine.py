import pandas


def run_irr_simulation(data_path: str):
    df = pandas.read_csv(data_path)

    shock_bps = [-0.01, 0.0, 0.01]  # -100bps, base, +100bps
    results = {}

    for shock in shock_bps:
        df["Shocked_Rate"] = df["Rate"] + shock
        df["Shocked_Interest"] = df["Amount"] * df["Shocked_Rate"]

        assets = df[df["Type"] == "Asset"]["Shocked_Interest"].sum()
        liabilities = df[df["Type"] == "Liability"]["Shocked_Interest"].sum()

        nii = assets - liabilities
        label = f"{int(10000 * shock)}bps NII" if shock != 0 else "Base NII"
        results[label] = round(nii, 2)

    delta_up = results["100bps NII"] - results["Base NII"]
    delta_down = results["-100bps NII"] - results["Base NII"]

    results["Delta NII (+100bps)"] = round(delta_up, 2)
    results["Delta NII (-100bps)"] = round(delta_down, 2)

    for shock in [-0.01, 0.01]:
        df["Base_PV"] = df["Amount"] / (1 + df["Rate"]) ** df["Maturity (years)"]
        df["Shocked_PV"] = df["Amount"] / (1 + df["Rate"] +shock) ** df["Maturity (years)"]
        df["Delta_PV"] = df["Shocked_PV"] - df["Base_PV"]

        delta_asset_pv = df[df["Type"] == "Asset"]["Delta_PV"].sum()
        delta_liability_pv = df[df["Type"] == "Liability"]["Delta_PV"].sum()
        delta_eve = delta_asset_pv - delta_liability_pv

        results[f"Delta EVE ({int(10000 * shock)}bps)"] = round(delta_eve, 2)

    return results
