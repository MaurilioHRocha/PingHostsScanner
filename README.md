


Network Ping Scanner

## Descrição
Um simples script em Python para escanear hosts em uma rede utilizando o protocolo ICMP (ping).

## Instruções de Uso
1. Clone este repositório:
   ```bash
   git clone https://github.com/mauriliohrocha/BreadcrumbsPingHostsScanner.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd network-ping-scanner
   ```
3. Execute o script Python para escanear hosts em um intervalo de IP (substitua `<seu-ip>` pelo intervalo desejado):
   ```bash
   python ping_scanner.py --range <seu-ip>
   ```
4. Analise a saída para ver os hosts que responderam ao ping.

## Requisitos do Sistema
- Python 3
- Biblioteca ping3
   ```bash
   pip install ping3
   ```

## Exemplos de Uso
- Escanear hosts em uma rede local:
   ```bash
   python ping_scanner.py --range 192.168.0.0/24
   ```

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar solicitações pull.

## Autor
Maurílio H Rocha
```
