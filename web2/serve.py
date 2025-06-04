#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys
import mimetypes

PORT = 8000

# Add WASM mime type
mimetypes.add_type('application/wasm', '.wasm')

class WASMHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

if __name__ == "__main__":
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), WASMHandler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        print(f"Open http://localhost:{PORT} in your browser")
        print("Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            sys.exit(0)