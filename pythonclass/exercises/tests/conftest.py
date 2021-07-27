import importlib
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--file", action="store", help="file to import module from",
        default=None
    )
    parser.addoption(
        "--function", action="store", help="function to test",
        default=None
    )
    parser.addoption(
        "--module", action="store", help="module to import",
        default=None
    )

def pytest_configure(config):
    config.addinivalue_line("markers", "function: name of function to test")

@pytest.fixture
def func(request):
    filename = request.config.getoption("--file")
    modname = request.config.getoption("--module")
    funcname = request.config.getoption("--function")

    if filename and not modname:
        modname = filename.rstrip(".py").replace("/", ".")

    if not funcname:
        mark = request.node.get_closest_marker("function")
        funcname = mark.args[0]

    module = importlib.import_module(modname)
    return getattr(module, funcname)
