FROM python:3

ARG http_proxy=http://87.254.212.120:8080/
ARG https_proxy=http://87.254.212.120:8080

RUN export HTTP_PROXY=$http_proxy && \
    export HTTPS_PROXY=$https_proxy && \
    pip3 install grpcio && \
    pip3 install protobuf

ADD client.py /
ADD hello_pb2_grpc.py /
ADD hello_pb2.py /

CMD ["python", "./client.py"]
