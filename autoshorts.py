import http.server
import socketserver
import threading

def run_server():
    PORT = 8000
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

def main_task():
    # Place your AutoShortsAI logic here
    print("Running main task...")

if __name__ == "__main__":
    threading.Thread(target=run_server).start()
    main_task()
