from SocketServer import TCPServer, StreamRequestHandler

server_address=xxx
RequestHandlerClass=SocketServer.BaseRequestHandler()
server=SocketServer.TCPServer(server_address, RequestHandlerClass, bind_and_activate=True)