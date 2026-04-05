// Local mTLS proxy for issue.swf.i.mercedes-benz.com
// Listens on localhost:18080, forwards to Jira with client cert

import http from 'http';
import https from 'https';
import fs from 'fs';
import { URL } from 'url';

const TARGET = 'https://issue.swf.i.mercedes-benz.com'\;
const PORT = 18080;
const CERT_FILE = '/lhome/giatran/.ssh/daimler/client.pem';

const pemData = fs.readFileSync(CERT_FILE, 'utf8');
const certMatch = pemData.match(/-----BEGIN CERTIFICATE-----[\s\S]+?-----END CERTIFICATE-----/);
const keyMatch = pemData.match(/-----BEGIN PRIVATE KEY-----[\s\S]+?-----END PRIVATE KEY-----/);

const agent = new https.Agent({
  cert: certMatch[0],
  key: keyMatch[0],
  ca: fs.readFileSync('/etc/ssl/certs/ca-certificates.crt'),
});

const server = http.createServer((req, res) => {
  const targetUrl = new URL(TARGET + req.url);
  const options = {
    hostname: targetUrl.hostname,
    port: 443,
    path: targetUrl.pathname + targetUrl.search,
    method: req.method,
    headers: { ...req.headers, host: targetUrl.hostname },
    agent,
  };

  const proxyReq = https.request(options, (proxyRes) => {
    res.writeHead(proxyRes.statusCode, proxyRes.headers);
    proxyRes.pipe(res);
  });

  proxyReq.on('error', (e) => {
    console.error('Proxy error:', e.message);
    res.writeHead(502);
    res.end(e.message);
  });

  req.pipe(proxyReq);
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`Jira mTLS proxy running on http://localhost:${PORT}`);
});
