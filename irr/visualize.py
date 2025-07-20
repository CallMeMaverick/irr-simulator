import matplotlib.pyplot as plt


def plot_irr_results(results: dict):
    nii_keys = [k for k in results if "NII" in k and "Delta" not in k]
    eve_keys = [k for k in results if "EVE" in k]

    nii_values = [results[k] for k in nii_keys]
    eve_values = [results[k] for k in eve_keys]

    plt.figure(figsize=(8, 5))
    plt.bar(nii_keys, nii_values)
    plt.title("Net Interest Income under Rate Shocks")
    plt.ylabel("NII")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.bar(eve_keys, eve_values, color="orange")
    plt.title("Change in Economic Value of Equity (ΔEVE)")
    plt.ylabel("ΔEVE")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


