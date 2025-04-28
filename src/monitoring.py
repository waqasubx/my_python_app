from prometheus_client import start_http_server, Counter

# Initialize metrics
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP Requests')

def start_monitoring(port=8000):
    """Start Prometheus metrics server."""
    start_http_server(port)
    print(f"Monitoring started on port {port}")