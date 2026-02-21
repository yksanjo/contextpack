import importlib


def test_main_exists():
    mod = importlib.import_module("contextpack.cli")
    assert hasattr(mod, "main")
