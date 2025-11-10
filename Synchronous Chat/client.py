import socket
import threading

HOST = "192.168.1.34"
PORT = 65432

def receive_messages(sock):
    """Continuously receive messages from server."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Disconnected from server.")
                break
            print("\n" + data.decode("utf-8"))
        except:
            print("Error receiving data")
            break
        
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except ConnectionRefusedError:
            print("Unable to connect to server. Make sure it's running")
            return
        
        threading.Thread(target=receive_messages, args=(s, ), daemon=True).start()
        
        print("connected to chat server. Type 'quit' to exit")
        while True:
            msg = input("> ")
            if not msg:
                continue
            s.sendall(msg.encode("utf-8"))
            if msg.lower() in ("quit", "exit", "bye"):
                break
            
if __name__ == "__main__":
    main()