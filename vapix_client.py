"""
Vapix module to interact with AXIS IP devices more easily.

Created 2021-04-09
"""
import requests


def get_ips_from_text(filename: str) -> list:
    """Iterate over IP addresses in a given file and return them list.

    :param filename:        Path or name of file to iterate over
    :return:                A list of IP address
    """
    ip_list = []
    with open(filename, mode="r") as file_handle:
        for line in file_handle:
            ip_list.append(line.strip())


    return ip_list


print(get_ips_from_text("ip_list.txt"))