
import socket

# versiyon tarama fonksiyonu
def version_scan(sock):
    
    # Soketten gelen yanıtı al
    response = sock.recv(1024)
    
    print(f"Version: {response.decode('utf-8')}", end="\n")
    
    # yanıtı satırlara bölerek her bir satırı kontrol et
    for line in response.decode("utf-8").splitlines():
        # satırda server veya version geçiyorsa satırı yazdır
         if "Server" in line or "Version" in line:
            return line

# tcp tarama fonksiyonu
def tcp_scan(t_ip, t_port):
    try:
        # soket oluştur
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # hedef IP ve port ile bağlantı kurma denemesi
        connect = sock.connect_ex((t_ip, t_port))

        # bağlantı başarılıysa version_scan fonksiyonu ile versiyonu kontrol et
        if connect == 0:
            print(f"Port {t_port}/TCP is open")
            version = version_scan(sock)
            print(f"Version: {response.decode('utf-8')}")
            

        # soketi kapat
        sock.close()
    except Exception as e:
        pass

# udp tarama fonksiyonu
def udp_scan(t_ip, t_port):
    try:
        # soket oluştur
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1)

        # hedef ip ve porta boş bir udp paketi gönder
        sock.sendto(b'', (t_ip, t_port))
        data, addr = sock.recvfrom(1024)
        print(f"Port {t_port}/UDP is open")

        # soketi kapat
        sock.close()
    except Exception as e:
        pass
 
    

if __name__ == "__main__":
    # kullanıcıdan girişleri al
    ip = input("Hedef IP adresini girin: ")
    s_port = int(input("Başlangıç portunu girin: "))
    e_port = int(input("Bitiş portunu girin: "))
    scan_type = input("TCP taraması için 'tcp', UDP taraması için 'udp' yazın: ")
    print("---------------------------")

    # port aralığını tara
    for port in range(s_port, e_port + 1):
        if scan_type == "tcp":
            tcp_scan(ip, port)
        elif scan_type == "udp":
            udp_scan(ip, port)

        else:
            print("Geçersiz tarama türü. 'tcp' veya 'udp' seçin.")
            break

    print("-----------------------")
    print("-----------------------")
    print("TARAMA TAMAMLANDI")

