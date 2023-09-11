import socket, ssl

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_ssl = ssl.wrap_socket(s,
                        cert_reqs=ssl.CERT_REQUIRED,
                        ca_certs='server_cert.pem')
s_ssl.connect(('10.0.99.100', 20000))
s_ssl.send(b'Hello World?')
s_ssl.recv(8192)

