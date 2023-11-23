import socket

from socket_demo import return_msg as res


class SocketServer():
    def __init__(self):
        # 创建 socket对象
        self.socket_server = socket.socket()
        # 绑定 socket_server到指定的ip地址
        self.socket_server.bind(("0.0.0.0", 7071))
        # 监听端口, listen()内书写数字，表示可以接受链接的数量
        self.socket_server.listen(1)
        while True:
            # 等待客户端连接，接收到的 result是一个二元元组, accept()是一个阻塞的方法，如果没有连接不会往下执行
            result = self.socket_server.accept()
            conn = result[0]  # 客户端连接对象
            address = result[1]  # 客户端地址信息
            print(f"接收到的客户端连接信息为{address}")
            # 接收客户端信息，recv接受的参数是缓冲区大小，一般1024即可，返回的是一个字节数组，bytes对象，不是字符串，再将其decode解码为字符串对象
            data = conn.recv(1024).decode("UTF-8")

            print(f"客户端发来的消息是:{data}")
            # 回复消息
            # msg = input("请输入回复的消息:")
            # msg = "hello client!"
            msg = res.return_msg(data)
            if msg == 'exit':
                break

            conn.send(msg.encode("UTF-8"))
            print(f"回复内容是：{msg}")
            # 关闭连接
            conn.close()

    def main(self):
        try:
            self.interactive()
        except Exception as e:
            raise e
        finally:
            print("连接异常，重新等待连接")
            return self.main()

    def __del__(self):
        self.socket_server.close()



# 创建 socket对象
socket_server = socket.socket()
# 绑定 socket_server到指定的ip地址
socket_server.bind(("0.0.0.0", 7071))
# 监听端口, listen()内书写数字，表示可以接受链接的数量
socket_server.listen(5)
while True:
    # 等待客户端连接，接收到的 result是一个二元元组, accept()是一个阻塞的方法，如果没有连接不会往下执行
    result = socket_server.accept()
    conn = result[0]  # 客户端连接对象
    address = result[1]  # 客户端地址信息
    print(f"接收到的客户端连接信息为{address}")
    while True:
        # 接收客户端信息，recv接受的参数是缓冲区大小，一般1024即可，返回的是一个字节数组，bytes对象，不是字符串，再将其decode解码为字符串对象
        data = conn.recv(1024).decode("UTF-8")
        print(f"客户端发来的消息是:{data}")
        # 回复消息
        # msg = input("请输入回复的消息:")
        # msg = "hello client!"
        msg = res.return_msg(data)
        if msg == 'exit':
            break

        conn.send(msg.encode("UTF-8"))
        print(f"回复内容是：{msg}")
    # 关闭连接
    conn.close()
socket_server.close()

if __name__ == '__main__':
    SocketServer().main()
