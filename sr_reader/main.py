"""Analyse server reports from AXIS devices."""
from pathlib import Path
from typing import List
import unittest


# 1. Ensure basic functionality is given
# 2. Write down similarities to analyse server report 
#    Sections to separate (----- **** -----)
#    Certain details to highlight (Keywords to look for)
#    Differentiate priority of log entries (NOTICE, INFO, WARNING, etc.)
# 3. Decide development procedure (Test driven development)
# 4. Write tests to test previous basic functionality
# 5. Write tests, that dictate our codes behaviour


class ServerReport:
    """Read, filter and analyse ServerReport from an AXIS device.
    
    :param report:      Server report as string
    """

    def __init__(self, report: str) -> None:
        """Initialize instance."""
        self.raw_report = report.strip()
        self._is_report()

    def _is_report(self) -> None:
        """Confirm that raw_report is a valid server report."""
        if not self.raw_report.startswith("----- Server Report Start -----"):
            raise TypeError("Not a valid server report.")

    def as_list(self) -> List[str]:
        """Split server report into list of lines."""
        return self.raw_report.split("\n")


class TestServerReport(unittest.TestCase):
    """Test ServerReport class functionality."""

    def test_init_works_with_valid_sr(self):
        """Test that valid ServerReport can be initialized without
        raising an exception and that .raw_report starts with
        specified string.
        """
        valid_sr = Path("sr_reader/valid_report.txt").read_text()
        report = ServerReport(valid_sr)
        self.assertTrue(report.raw_report.startswith("----- Server Report Start -----"))

    def test_init_raises_exception_with_corrupt_sr(self):
        """Test that corrupt ServerReport crashes on initialization."""
        corrupt_sr = Path("sr_reader/corrupt_report.txt").read_text()
        with self.assertRaises(TypeError):
            ServerReport(corrupt_sr)

    def test_sr_is_splitable(self):
        """Test that each line in the server report can be separated."""
        report = ServerReport(Path("sr_reader/valid_report.txt").read_text())
        split_report = report.as_list()
        self.assertTrue(isinstance(split_report, list) and len(split_report) > 1)


if __name__ == "__main__":
    unittest.main()
