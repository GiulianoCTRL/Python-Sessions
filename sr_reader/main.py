"""Analyse server reports from AXIS devices."""
from pathlib import Path

# 1. Ensure basic functionality is given
# 2. Write down similarities to analyse server report 
# Sections to separate (----- **** -----)
# Certain details to highlight (Keywords to look for)
# Differentiate priority of log entries (INFO, NOTICE, WARNING, etc.)


class ServerReport:
    """Read, filter and analyse ServerReport from an AXIS device.
    
    :param report:      Server report as string
    """

    def __init__(self, report: str):
        """Initialize class."""
        self.raw_report = report.strip()
        self._is_report()

    def _is_report(self):
        """Confirm that raw_report is a valid server report."""
        if not self.raw_report.startswith("----- Server Report Start -----"):
            raise TypeError("Not a valid server report.")


if __name__ == "__main__":
    report = Path("sr_reader/serverreport.txt").read_text()
    sr = ServerReport(report)
    corrupt_report = Path("sr_reader/corrupt_report.txt").read_text()
    fail = ServerReport(corrupt_report)
