#!/usr/bin/env python3

import time
import random
from http.server import HTTPServer, BaseHTTPRequestHandler

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/metrics':
            cpu_load = random.uniform(10.0, 90.0)
            
            metrics = f"""cpu_load_percent {cpu_load:.2f}
cpu_load_timestamp {int(time.time())}
"""
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(metrics.encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), MetricsHandler)
    print("Metrics server running on http://0.0.0.0:8080/metrics")
    server.serve_forever()