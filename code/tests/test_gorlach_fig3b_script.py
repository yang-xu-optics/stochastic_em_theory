import subprocess
import sys
from pathlib import Path


def test_gorlach_fig3b_script_creates_expected_outputs(tmp_path) -> None:
    script = Path("scripts/reproduce_gorlach_2023_fig3b.py")
    completed = subprocess.run(
        [sys.executable, str(script), "--output-dir", str(tmp_path), "--shots", "256", "--max-order", "31"],
        cwd=Path(__file__).resolve().parents[1],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "gorlach_2023_fig3b_proxy.png" in completed.stdout
    assert (tmp_path / "gorlach_2023_fig3b_proxy_spectra.csv").exists()
    assert (tmp_path / "gorlach_2023_fig3b_proxy_summary.json").exists()
    assert (tmp_path / "gorlach_2023_fig3b_proxy.png").exists()
    assert (tmp_path / "manifest.yaml").exists()
