from src.main import main
from src.monitoring import start_monitoring
from prometheus_client import REGISTRY
import pytest

def test_main_function(capsys):
    """Test if main() prints expected output."""
    main()
    captured = capsys.readouterr()
    assert "Running core logic..." in captured.out

def test_monitoring_startup():
    """Test if Prometheus metrics server starts."""
    start_monitoring(port=8000)
    assert "app_requests_total" in [m.name for m in REGISTRY.collect()[0].samples]

# Optional: Add more test cases as needed.