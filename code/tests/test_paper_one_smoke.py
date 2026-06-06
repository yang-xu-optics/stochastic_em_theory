import subprocess
import sys
from pathlib import Path


def test_paper_one_smoke_script_creates_expected_outputs(tmp_path) -> None:
    script = Path("scripts/run_paper_one_smoke.py")
    completed = subprocess.run(
        [sys.executable, str(script), "--output-root", str(tmp_path), "--shots", "2000"],
        cwd=Path(__file__).resolve().parents[1],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "paper-one-smoke" in completed.stdout
    assert (tmp_path / "runs" / "paper-one-smoke-single" / "single_mode_g2.csv").exists()
    assert (tmp_path / "runs" / "paper-one-smoke-multimode" / "multimode_g2.csv").exists()
    assert (tmp_path / "runs" / "paper-one-smoke-hhg" / "proxy_hhg_spectrum.csv").exists()
    assert (tmp_path / "runs" / "paper-one-smoke-hhg" / "shot_records.csv").exists()
    assert (tmp_path / "runs" / "paper-one-smoke-ati" / "ati_statistics.csv").exists()
    assert (tmp_path / "runs" / "paper-one-smoke-emission" / "emission_environment_scan.csv").exists()
    assert (tmp_path / "figures" / "single_mode_g2.png").exists()
    assert (tmp_path / "figures" / "multimode_g2.png").exists()
    assert (tmp_path / "figures" / "proxy_hhg_spectrum.png").exists()
