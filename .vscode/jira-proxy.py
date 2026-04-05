#!/usr/bin/env python3
import ssl, http.server, http.client, socketserver

TARGET_HOST = 'issue.swf.i.mercedes-benz.com'
LISTEN_PORT = 18080
CERT = '/lhome/giatran/.ssh/daimler/client.pem'
KEY  = '/lhome/giatran/.ssh/daimler/client.key'
CA   = '/etc/ssl/certs/ca-certificates.crt'

class ProxyHandler(http.server.BaseHTTPRequestHandler):
    def proxy(self):
        ctx = ssl.create_default_context(cafile=CA)
        ctx.load_cert_chain(certfile=CERT, keyfile=KEY)
        conn = http.client.HTTPSConnection(TARGET_HOST, 443, context=ctx)
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length else None
        hdrs = {k: v for k, v in self.headers.items()
                if k.lower() not in ('host', 'connection', 'transfer-encoding')}
        try:
            conn.request(self.command, self.path, body=body, headers=hdrs)
            r = conn.getresponse()
            data = r.read()
            self.send_response(r.status)
            for k, v in r.getheaders():
                if k.lower() not in ('transfer-encoding', 'connection'):
                    self.send_header(k, v)
            self.send_header('Content-Length', str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            self.wfile.flush()
        except Exception as e:
            self.send_error(502, str(e))
        finally:
            conn.close()
    def log_message(self, fmt, *a): print(f'[jira-proxy] {fmt % a}')
    do_GET = do_POST = do_PUT = do_DELETE = do_PATCH = proxy

if __name__ == '__main__':
    class ThreadedServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
        daemon_threads = True
    s = ThreadedServer(('127.0.0.1', LISTEN_PORT), ProxyHandler)
    print(f'Jira mTLS proxy on http://localhost:{LISTEN_PORT} -> {TARGET_HOST}', flush=True)
    s.serve_forever()
