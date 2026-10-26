import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    ip_privado = s.getsockname()[0]
finally:
    s.close()

print(f"Seu IP privado atual é: {ip_privado}")
