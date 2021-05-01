import socket as s
host = input("Enter Host:")
print(f'IP of {host} is {s.gethostbyname(host)}')