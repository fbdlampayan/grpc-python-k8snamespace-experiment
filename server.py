import grpc
from concurrent import futures
import time

import hello_pb2_grpc
import hello_pb2

class HelloServicer(hello_pb2_grpc.HelloServiceServicer):

    def Greet(self, request, context):
        print("message from client: " + request.message)
        response = hello_pb2.Request()
        response.message = "Message from server"
        return response


server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

hello_pb2_grpc.add_HelloServiceServicer_to_server(HelloServicer(), server)

print("Starting server. Listening on port 50051")
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
