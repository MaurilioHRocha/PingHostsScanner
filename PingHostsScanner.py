import ipaddress
import subprocess
from ping3 import ping, verbose_ping

# Substitua o intervalo de IP pelo seu
ip_range = "172.30.0.0/24"

# Crie um objeto de rede a partir do intervalo de IP
network = ipaddress.IPv4Network(ip_range, strict=False)

# Lista para armazenar os hosts que respondem ao ping
hosts_responding = []

# Loop pelos endereços IP no intervalo
for ip in network.hosts():
    ip = str(ip)
    result = ping(ip, timeout=1)  # Envie um ping para o IP com um timeout de 1 segundo
    if result is not None:
        print(f"{ip} está respondendo ao ping")
        hosts_responding.append(ip)

# Quantidade de hosts que responderam ao ping
print(f"Total de {len(hosts_responding)} hosts respondendo ao ping.")
