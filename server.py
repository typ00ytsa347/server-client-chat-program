import socket
import threading


class Server(object):
    def __init__(self):
        self.clients = {}

        # create server socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('127.0.0.1', 0))
        self.server.listen()

        HOST = self.server.getsockname()
        print(f"[INFO] Server running on {HOST}")

        while True:
            connection, address = self.server.accept()
            nickname = connection.recv(1024)
            nickname = nickname.decode()
            self.clients[nickname] = connection

            # start a thread for the client
            threading.Thread(target=self.receive_message, args=(connection, nickname), daemon=True).start()

            print("[INFO] Connection from {}:{} AKA {}".format(address[0], address[1], nickname))


    def receive_message(self, connection, nickname):
        print("[INFO] Waiting for messages")
        while True:
            try:
                msg = connection.recv(1024)

                self.send_message(msg, nickname)
                print(nickname + ": " + msg.decode())
            except:
                connection.close()

                #remove user from users list
                del(self.clients[nickname])

                break

        print(nickname, " disconnected")


    def send_message(self, message, sender):
        if len(self.clients) > 0:
            for nickname in self.clients:
                if nickname != sender:
                    msg = sender + ": " + message.decode()
                    self.clients[nickname].send(msg.encode())


if __name__ == "__main__":
    chat_server = Server()