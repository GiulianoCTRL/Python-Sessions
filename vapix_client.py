#!/usr/bin/env python3
"""
Vapix module to interact with AXIS IP devices more easily.

Created 2021-04-09
"""
import fire
import requests
from requests.auth import HTTPDigestAuth


def get_ips_from_text(filename: str) -> list:
    """Iterate over IP addresses in a given file and return them  as a list.

    :param filename:        Path or name of file to iterate over
    :return:                A list of IP address
    """
    ip_list = []
    with open(filename, mode="r") as file_handle:
        for line in file_handle:
            ip_list.append(line.strip())

    return ip_list


def fetch_params(host: str, password: str = "pass") -> dict:
    """Fetch parameters from AXIS device via param.cgi.

    :param host:        IPv4 address of an AXIS device
    :param password:    Password for root user
    :return:            Dictionary containing the device's settings
    """
    # https://docs.python-requests.org/en/latest
    # https://realpython.com/python-requests/
    response = requests.get(
        f"http://{host}/axis-cgi/param.cgi?action=list",
        auth=HTTPDigestAuth("root", password),
    )
    # Does request succeed?
    response.raise_for_status()

    settings = {}
    # Get response content as text
    param_text = response.text
    # split string after each newline symbol (\n) into a list of strings
    param_list = param_text.split("\n")
    for line in param_list:
        # Check that param is not empty, continue to next item in loop
        if line == "":
            continue
        # Initialize two variables at the same time, as we split each line
        # into a list of two strings, the left side of the = and the right side
        # of it
        param, value = line.split("=", maxsplit=1)
        # Add a key (name of the parameter) with the value of the parameter
        settings[param] = value

    # Return the freshly populated settings dict!
    return settings


def fetch_server_report(host: str, password: str = "pass") -> str:
    """Fetch server report from an AXIS device.

    :param host:        IPv4 address of an AXIS device
    :param password:    Password for root user
    :return:            Serverreport as string
    """
    # Send request
    response = requests.get(
        f"http://{host}/axis-cgi/serverreport.cgi",
        auth=HTTPDigestAuth("root", password),
    )

    # Confirm request was successful and return it's content as string/text
    response.raise_for_status()
    return response.text


def fetch_info(host: str, password: str = "pass") -> str:
    """Fetch basic device info from an AXIS device.

    :param host:        IPv4 address of an AXIS device
    :param password:    Password for root user
    :return:            Basic device info as string
    """
    # https://www.axis.com/vapix-library/subjects/t10037719/section/t10132180/display
    # https://docs.python-requests.org/en/latest/api/#requests.post

    # From the VAPIX library we know that we need to send a json
    # which is basically a dictionary (Below is copy pasted for the vapix-library)
    json_data = {"apiVersion": "1.0", "method": "getAllProperties"}

    # Send post request (because we are sending data)
    response = requests.post(
        f"http://{host}/axis-cgi/basicdeviceinfo.cgi",
        auth=HTTPDigestAuth("root", password),
        json=json_data,
    )

    # Confirm request was successful and return it's content as string/text
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    fire.Fire(fetch_info)
