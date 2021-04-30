#!/usr/bin/env python3
"""
Vapix module to interact with AXIS IP devices more easily.

AXIS API Documentation:
https://www.axis.com/vapix-library/

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


class AxisDevice:
    """Gathering of methods for Axis devices.

    :param host:        IPv4 address of an AXIS device
    :param password:    Password for root user
    """

    def __init__(self, host: str, password: str = "pass"):
        """Initialize Axis device with host and password."""
        self.host = host
        self.password = password
        self.auth = HTTPDigestAuth("root", password)

    def fetch_params(self) -> dict:
        """Fetch parameters from AXIS device via param.cgi.

        :return:            Dictionary containing the device's settings
        """
        # https://docs.python-requests.org/en/latest
        # https://realpython.com/python-requests/
        response = requests.get(
            f"http://{self.host}/axis-cgi/param.cgi?action=list",
            auth=self.auth,
        )
        response.raise_for_status()
        settings = {}
        param_text = response.text
        param_list = param_text.split("\n")
        for line in param_list:
            if line == "":
                continue
            param, value = line.split("=", maxsplit=1)
            settings[param] = value

        return settings

    def fetch_server_report(self) -> str:
        """Fetch server report from an AXIS device.

        :param host:        IPv4 address of an AXIS device
        :param password:    Password for root user
        :return:            Serverreport as string
        """
        response = requests.get(
            f"http://{self.host}/axis-cgi/serverreport.cgi", auth=self.auth
        )

        response.raise_for_status()
        return response.text

    def fetch_info(self) -> str:
        """Fetch basic device info from an AXIS device.

        :return:            Basic device info as string
        """
        # From the VAPIX library we know that we need to send a json
        # which is basically a dictionary (Below is copy pasted for the vapix-library)
        json_data = {"apiVersion": "1.0", "method": "getAllProperties"}

        # Send post request (because we are sending data)
        response = requests.post(
            f"http://{self.host}/axis-cgi/basicdeviceinfo.cgi",
            auth=self.auth,
            json=json_data,
        )

        # Confirm request was successful and return it's content as string/text
        response.raise_for_status()
        return response.text


if __name__ == "__main__":
    fire.Fire(AxisDevice)

