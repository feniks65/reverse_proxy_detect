import socket
import datetime
import argparse

def time_request(host, request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    host = host.split(':')
    s.connect((host[0], int(host[1])))

    time_start = datetime.datetime.now()
    s.send(request)
    s.recv(1024)
    time_end = datetime.datetime.now()

    diff = time_end - time_start
    return diff.total_seconds() * 1000


parser = argparse.ArgumentParser()
parser.add_argument('--host', help="host (ip:port)", required=True)
args = parser.parse_args()

valid_request = "GET /aaaaaa HTTP/1.1\r\nHost: {}\r\n\r\n".format(args.host)
invalid_request = "GET /aaaaaaa HTTP/1.1\r\nMost: {}\r\n\r\n".format(args.host)

valid_time = time_request(args.host, valid_request)
invalid_time = time_request(args.host, invalid_request)

print('valid request took {} ms\ninvalidrequest took {}ms'.format(valid_time, invalid_time))
