from irr.engine import run_irr_simulation
from irr.visualize import plot_irr_results


if __name__ == "__main__":
    results = run_irr_simulation("./data/data.csv")
    plot_irr_results(results)
    print

