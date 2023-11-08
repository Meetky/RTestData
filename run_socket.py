import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("0.0.0.0", 8002))
sock.listen(5)

conn, address = sock.accept()  # 获取客户端的socket对象和地址

msg = conn.recv(1024)  # 获取客户端的握手信息
print(msg)