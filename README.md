# nmap-socket

Bu Python betiği, belirli bir port aralığı içindeki bir hedef IP adresinde TCP ve UDP port taramalarını gerçekleştirmenize olanak tanır. Açık portlar hakkında bilgi sağlar ve sunucu sürümlerini belirlemeye çalışır.

## Gereksinimler

- Python 3.x

## Kullanım

1. Proje deposunu klonlayın:

    ```bash
    git clone https://github.com/bilgenurt/nmap-socket.git
    cd nmap-socket
    ```

2. Betiği çalıştırın:

    ```bash
    python3 nmap-socket.py
    ```

3. İstenilen IP adresini, başlangıç ve bitiş portlarını girmek ve TCP ile UDP tarama arasında seçim yapmak için yönergeleri izleyin.

## Özellikler

- **TCP Taraması**: Açık TCP portlarını belirler ve sunucu sürümlerini almayı dener.
- **UDP Taraması**: Açık UDP portlarını belirler.

## Nasıl Çalışır

- `tcp_scan` fonksiyonu, belirtilen aralıktaki her porta bir TCP bağlantısı kurar ve sunucu sürümlerini almaya çalışır.
- `udp_scan` fonksiyonu, belirtilen aralıktaki her porta boş bir UDP paketi gönderir ve açık UDP portlarını belirler.

## Kullanım Örneği

```bash
Hedef IP adresini girin: 192.168.1.1
Başlangıç portunu girin: 1
Bitiş portunu girin: 100
TCP taraması için 'tcp', UDP taraması için 'udp' yazın: tcp
---------------------------
Port 80/TCP açık
Sürüm: Apache/2.4.29 (Ubuntu)
Port 22/TCP açık
Sürüm: OpenSSH/7.2p2 Ubuntu
-----------------------
-----------------------
TARAMA TAMAMLANDI
