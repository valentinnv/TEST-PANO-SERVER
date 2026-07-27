import http.server
import socketserver
import json
import os

PORT = 8000

class AutoDiscoveryHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # API endpoint that scans the assets folder automatically
        if self.path == '/api/discover-assets':
            assets_dir = os.path.join(os.getcwd(), 'assets')
            valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.avif')
            files = []
            
            if os.path.exists(assets_dir):
                files = [f for f in os.listdir(assets_dir) 
                         if f.lower().endswith(valid_extensions)]
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(files).encode('utf-8'))
        else:
            super().do_GET()

if __name__ == '__main__':
    with socketserver.TCPServer(("", PORT), AutoDiscoveryHandler) as httpd:
        print(f"\n==================================================")
        print(f" 360° Panorama Server Running!")
        print(f" Open your browser to: http://localhost:{PORT}")
        print(f"==================================================\n")
        httpd.serve_forever()