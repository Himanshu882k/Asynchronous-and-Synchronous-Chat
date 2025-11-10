# Asynchronous-and-Synchronous-Chat
Asynchronous and Synchronous Messaging app using sockets
📘 Overview

This project demonstrates how real-time chat systems can be implemented using Python’s socket programming in both synchronous (threaded) and asynchronous (asyncio) modes.
It enables multiple clients to connect to a single server over a local network (LAN) and exchange messages — just like a basic chatroom.

The goal is to show how both blocking (multi-threaded) and non-blocking (async) architectures can be used to build scalable messaging systems.
⚙️ Features

💬 Multi-client support (several users can chat at once)

🌐 Works over LAN (Wi-Fi router network)

🧵 Two different architectures:

Synchronous: Uses threads to handle each client

Asynchronous: Uses asyncio for event-driven concurrency

🚫 Handles client disconnections gracefully

🔁 Broadcast system (messages from one user are shared with all)

🧠 Simple chatbot echo logic included in the server

🧱 Architecture Overview
🧵 Synchronous (Threaded) Version

Uses socket + threading

Each client connection runs in its own thread

The main server thread listens for incoming connections

Suitable for smaller apps with limited users

Flow:

Server starts → listens on a port (e.g., 65432)

Client connects → server spawns a new thread

Each client thread waits for messages and broadcasts them

Server handles multiple clients concurrently

Pros:

Easy to understand

Simple debugging

Cons:

Each client uses a separate thread (memory heavy for large scale)

⚡ Asynchronous (AsyncIO) Version

Uses Python’s asyncio library

No threads; uses a single event loop for all clients

Non-blocking I/O: the server can handle thousands of connections efficiently

Flow:

Server starts using asyncio.start_server()

Each connection handled as a coroutine

Messages are received and broadcast without blocking others

The same event loop keeps all clients active simultaneously

Pros:

High scalability

Very lightweight on resources

Perfect for real-time systems (like chat, games, IoT, etc.)

Cons:

Slightly complex to implement and debug

🧠 How It Works (Both Versions)

Server:

Binds to an IP (like 192.168.x.x) and port (e.g., 65432)

Accepts connections from multiple clients

For every message from a client:

Sends a response to the sender

Broadcasts it to all other connected clients

Client:

Connects to the server using its IP and port

Sends messages typed by the user

Displays messages received from the server

Router Connectivity:

Works when devices (PC, phone, etc.) are on the same Wi-Fi

The server runs on the local IP (e.g., 192.168.1.34)

Clients use that IP to connect to the chatroom
🧰 Tech Stack

Language: Python 3.x

Libraries:

socket — for TCP communication

threading — for synchronous server
