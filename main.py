from utils import parse_log_file, generate_report

LOG_FILE = "logs.log"
OUTPUT_FILE = "output/report.txt"

WARNING_THRESHOLD = 5     # minutes
ERROR_THRESHOLD = 10      # minutes


def main():
    results = parse_log_file(LOG_FILE, WARNING_THRESHOLD, ERROR_THRESHOLD)
    generate_report(results, OUTPUT_FILE)
    print(f"✅ Log monitoring complete. Report saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
