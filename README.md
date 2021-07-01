# burp-http-downgrade
Burp Extension to downgrade HTTP/2 responses to HTTP/1.1

## Description

While performing MiTM attacks against Android apps, some HTTP parsing errors were observed. Manually downgrading them from HTTP/2 to HTTP/1.1 seemed to solve the issue, i wrote this simple extension to automate the process.

At the moment, the extension will downgrade *ALL* HTTP responses to HTTP/1.1.
