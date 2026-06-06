from stochastic_em_theory import __version__


def test_version_is_string() -> None:
    assert isinstance(__version__, str)
    assert __version__
