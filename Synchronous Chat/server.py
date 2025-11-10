import socket
import threading

HOST = "192.168.1.34"

PORT = 65432

clients = []
lock = threading.Lock()

def broadcast(message, sender_socket=None):
    """Send a message to all connected Clients except sender."""
    with lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.sendall(message)
                except Exception as e:
                    print(f"Error sending to client: {e}")
                    clients.remove(client)

def handle_client(conn, addr):
    """Handle a message from a single client."""
    print(f"[NEW CONNECTION] {addr} connected")
    conn.sendall(b"Welcome to the multi-client chat server!\n")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print(f"[DISCONNECTED] {addr} closed the connection.")
                break

            message = data.decode("utf-8").strip()
            print(f"[{addr}] {message}")

            if message.lower() in ("quit", "exit", "bye"):
                conn.sendall(b"Goodbye!\n")
                break

            reply = f"Bot to {addr}: You said -> {message}\n"
            conn.sendall(reply.encode("utf-8"))

            # Broadcast to other connected clients
            broadcast(f"[{addr}] {message}\n".encode("utf-8"), sender_socket=conn)

        except ConnectionResetError:
            print(f"[ERROR] {addr} forcibly closed connection.")
            break
        except Exception as e:
            print(f"[EXCEPTION] {addr}: {e}")
            break

    with lock:
        if conn in clients:
            clients.remove(conn)
    conn.close()
    print(f"[CLOSED] Connection with {addr} closed.")

def start_server():
    """Main server loop"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Accept all network interfaces, not just localhost
        server.bind(("", PORT))
        server.listen()
        print(f"[STARTING] Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            with lock:
                clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {len(clients)}")

if __name__ == "__main__":
    start_server()
