import http.server
import socketserver
import os
import psycopg2


db_config = {
    "host": "docker-scrapy-database-1",
    "port": "5432",
    "database": "flats_db",
    "user": "postgres",
    "password": "ardit33",
}
host = "0.0.0.0"
port = 8080

curr_dir = os.path.dirname(os.path.abspath(__file__))
rel_dir = os.path.join(curr_dir, "templates", "index.html")


def get_data_from_db():
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM apartments")
    data = cursor.fetchall()

    conn.close()
    return data


class ReqHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            data = get_data_from_db()

            response = "<!DOCTYPE html><html><head><title>Flats</title></head><body><h1>Flats</h1><table><tr><th>Id</th><th>Name</th><th>Image Example</th><th>Images</th></tr>"

            for row in data:
                response += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td><img src='{row[2].split(';')[0]}'></img></td><td>{row[2]}</td></tr>"

            response += "</table></body></html>"

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(response.encode("utf-8"))
        else:
            super().do_GET()


with socketserver.TCPServer((host, port), ReqHandler) as httpd:
    print(f"Serving on {host}:{port}")
    httpd.serve_forever()
