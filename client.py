import socket
import threading

nickname = input("Choose an alias: ")

if nickname == "admin":
    password = input("Enter password for admin: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(("127.0.0.1", 9999))
except ConnectionRefusedError:
    print("Failed to connect to the server.")
    exit()

stop_thread = False


def receive():
    global stop_thread
    while not stop_thread:
        try:
            message = client.recv(1024).decode("ascii")

            if message == "NICK":
                client.send(nickname.encode("ascii"))
                next_message = client.recv(1024).decode("ascii")

                if next_message == "PASS":
                    client.send(password.encode("ascii"))
                    response = client.recv(1024).decode("ascii")
                    if response == "REFUSE":
                        print("Connection refused! Wrong password!")
                        stop_thread = True

                elif next_message == "BAN":
                    print("Connection refused due to a ban.")
                    client.close()
                    stop_thread = True

            else:
                print(message)

        except (ConnectionAbortedError, ConnectionResetError):
            print("Connection was closed by the server.")
            stop_thread = True
            break
        except Exception as e:
            print(f"Error: {e}")
            client.close()
            stop_thread = True
            break


def write():
    global stop_thread
    while not stop_thread:
        try:
            message = f'{input("")}'

            if message.lower() == "/quit":
                client.send(f"{nickname} has left the chat.".encode("ascii"))
                print("You have left the chat.")
                stop_thread = True
                client.close()
                break

            elif message.startswith("/") and not message.lower().startswith("/quit"):
                if nickname == "admin":
                    command = message.split()
                    if command[0] == "/kick" and len(command) > 1:
                        client.send(f"KICK {command[1]}".encode("ascii"))
                    elif command[0] == "/ban" and len(command) > 1:
                        client.send(f"BAN {command[1]}".encode("ascii"))
                else:
                    print("Only the admin can use this command.")
            else:
                client.send(f"{nickname}: {message}".encode("ascii"))

        except:
            print("Error while sending the message.")
            client.close()
            stop_thread = True
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
