import subprocess
import sys
import os
import shutil
from pathlib import Path

import pytest


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


def test_gorlach_fig3b_script_default_output_is_repo_results_even_from_other_cwd(tmp_path) -> None:
    repo_root = Path(__file__).resolve().parents[2]
    code_root = repo_root / "code"
    script = code_root / "scripts" / "reproduce_gorlach_2023_fig3b.py"
    default_output = repo_root / "results" / "gorlach-2023-fig3b-proxy"
    if default_output.exists():
        pytest.skip(f"default output path already exists: {default_output}")

    env = dict(os.environ)
    env["PYTHONPATH"] = str(code_root / "src")
    try:
        completed = subprocess.run(
            [sys.executable, str(script), "--shots", "64", "--max-order", "9"],
            cwd=tmp_path,
            env=env,
            check=True,
            capture_output=True,
            text=True,
        )

        assert str(default_output / "gorlach_2023_fig3b_proxy.png") in completed.stdout
        assert (default_output / "gorlach_2023_fig3b_proxy_spectra.csv").exists()
    finally:
        if default_output.exists():
            shutil.rmtree(default_output)
