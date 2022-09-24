#!/usr/bin/env python3
import os
import socket
import json
import yaml

hosts = [
    "drive.google.com",
    "mail.google.com",
    "google.com",
]
prev_data_file_name = "prev_ips.txt"


def main():
    services = get_services()
    for host in hosts:
        ip = socket.getaddrinfo(host, 0)[0][4][0]

        if services.get(host) and services.get(host) != ip:
            message = f"[ERROR] {host} IP mismatch: {services[host]} {ip}"
        else:
            message = f"{host} - {ip}"

        services[host] = ip
        print(message)
    update_stored_ips(services)
    write_json(services)
    write_yaml(services)


def write_json(services):
    with open("services.json", "w") as file:
        json.dump(services_to_array(services), file)


def write_yaml(services):
    with open("services.yml", "w") as file:
        yaml.dump(services_to_array(services), file)


def services_to_array(services):
    return [{host: ip} for host, ip in services.items()]


def read_prev_ips(file_handle):
    entries = dict()

    for line in file_handle.read().split("\n"):
        [host, ip] = line.split(":")
        entries[host] = ip

    return entries


def get_services():
    if not os.path.exists(prev_data_file_name):
        return dict([(host, "") for host in hosts])

    with open(prev_data_file_name) as file:
        return read_prev_ips(file)


def update_stored_ips(services: dict):
    lines = []

    for (host, ip) in services.items():
        lines.append(f"{host}:{ip}")

    with open(prev_data_file_name, "w") as file:
        file.write('\n'.join(lines))


if __name__ == "__main__":
    main()
