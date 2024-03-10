# manager.py

import argparse
from system_info import SystemInfo

def main():
    parser = argparse.ArgumentParser(description="Generate a system report for Linux.")
    args = parser.parse_args()

    # Generate system report
    report = SystemInfo.generate_report()
    print(report)

if __name__ == "__main__":
    main()
