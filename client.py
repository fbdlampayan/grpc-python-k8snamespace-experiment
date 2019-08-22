import grpc

import hello_pb2
import hello_pb2_grpc


f = open("/home/fbdl/client.conf", "r")
contents = f.read()

channel = grpc.insecure_channel(contents)

stub = hello_pb2_grpc.HelloServiceStub(channel)

x = 10

while (x != 0):
    request = hello_pb2.Request(message="Message from client")
    response = stub.Greet(request)
    print(response.message)
    x = x - 1
