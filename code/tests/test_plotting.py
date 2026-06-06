import csv

from stochastic_em_theory.plotting import plot_multimode_g2, plot_single_mode_g2


def test_single_mode_plot_writes_png(tmp_path) -> None:
    csv_path = tmp_path / "single_mode_g2.csv"
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "r",
                "shots",
                "analytic_n",
                "estimated_n",
                "analytic_g2",
                "g2_corrected",
                "g2_naive",
                "abs2_wigner",
                "abs4_wigner",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "r": 0.5,
                "shots": 1000,
                "analytic_n": 0.27,
                "estimated_n": 0.27,
                "analytic_g2": 6.7,
                "g2_corrected": 6.8,
                "g2_naive": 2.2,
                "abs2_wigner": 0.77,
                "abs4_wigner": 1.3,
            }
        )

    output_path = plot_single_mode_g2(csv_path=csv_path, output_path=tmp_path / "single.png")

    assert output_path.exists()
    assert output_path.stat().st_size > 1000


def test_multimode_plot_writes_png(tmp_path) -> None:
    csv_path = tmp_path / "multimode_g2.csv"
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["r", "modes", "shots", "analytic_g2", "g2_corrected", "n_total_corrected"],
        )
        writer.writeheader()
        writer.writerow({"r": 0.7, "modes": 1, "shots": 1000, "analytic_g2": 4.2, "g2_corrected": 4.1, "n_total_corrected": 0.5})
        writer.writerow({"r": 0.7, "modes": 4, "shots": 1000, "analytic_g2": 1.8, "g2_corrected": 1.9, "n_total_corrected": 2.0})

    output_path = plot_multimode_g2(csv_path=csv_path, output_path=tmp_path / "multi.png")

    assert output_path.exists()
    assert output_path.stat().st_size > 1000
