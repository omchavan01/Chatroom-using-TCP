# Chat room using TCP

This project is a Python-based chat application that enables real-time communication between users through a central server. It features user authentication, admin privileges (kick/ban commands), and a system to manage banned users, ensuring secure and controlled interactions.

## Features

- Real-time Communication: Users can send and receive messages instantly.
- Admin Privileges: Admin can kick or ban users from the chat room.
- User Authentication: Admin login requires a password for verification.
- Ban List: Permanently ban users by adding their nickname to a ban list.
- Dynamic User Interaction: Displays join/leave messages for all users.
- Kick Users: Admin can remove disruptive users from the chat room.
- Simple Interface: Easy-to-use for both admins and regular users.

## Requirements

- Python 3.x (with socket and threading modules, both included in standard Python libraries)
- A text editor or IDE (e.g., VS Code, PyCharm, Sublime Text)

## Run Locally

Clone the project

```bash
  git clone https://github.com/omchavan01/Chatroom-using-TCP.git
```

Go to the project directory

```bash
  cd Chatroom-using-TCP
```

Run the server

```bash
  python server.py
```

Run the client

```bash
  python client.py
```

You can open multiple terminal windows and run the client script (client.py) in each one to simulate different users joining the chat.

