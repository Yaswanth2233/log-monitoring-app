# Log Monitoring App

This Python application monitors log files and measures how long each job takes from start to finish. It generates warnings or errors if a job exceeds defined duration thresholds.

---

## Features

- Parses CSV-style log files
- Tracks job start and end times using PID
- Calculates job duration in minutes
- Generates a report with status:
  - `OK` if duration ≤ 5 minutes
  - `WARNING` if duration > 5 minutes
  - `ERROR` if duration > 10 minutes
  - `INCOMPLETE` if a job never finished

---

## Log File Format

The application expects logs in the following CSV format:

HH:MM:SS, job name, START/END, PID

Example:

11:35:23, scheduled task 032, START, 37980
11:35:56, scheduled task 032, END, 37980
11:36:11, scheduled task 796, START, 57672
11:36:18, scheduled task 796, END, 57672
11:36:58, background job wmy, START, 81258

---

## Project Structure

log-monitoring-app/
├── logs.log              # Input log file
├── main.py               # Main program
├── utils.py              # Helper functions
├── tests/                # Test files
│   └── test_logs.py
├── output/               # Store generated reports
│   └── report.txt
├── requirements.txt      # Python dependencies
└── README.md             # This file

---

## Installation

1. Make sure you have Python 3 installed.
2. (Optional) Create a virtual environment:
   python -m venv venv
   venv\Scripts\activate
3. Install dependencies (if any):
   pip install -r requirements.txt

---

## How to Run

1. Open Command Prompt or PowerShell and navigate to the project folder:
   cd C:\Users\yassu\log-monitoring-app
2. Run the program:
   python main.py
3. Check the generated report in:
   output\report.txt

---

## Running Tests

Automated tests are included in the tests/ folder. Run them using pytest:

pytest tests/

Tests cover scenarios for:
- OK jobs (≤ 5 minutes)
- WARNING jobs (> 5 minutes)
- ERROR jobs (> 10 minutes)
- INCOMPLETE jobs (missing END entry)

---

## Output Example

PID    | Job Name            | Duration (min) | Status
-------------------------------------------------------
37980  | scheduled task 032  | 0.55           | OK
57672  | scheduled task 796  | 0.12           | OK
81258  | background job wmy  | 0.00           | INCOMPLETE

---

## Notes

- Ensure the logs.log file matches the expected CSV format.
- Jobs without an END event are marked as INCOMPLETE.
- Duration thresholds for warnings and errors can be modified in main.py.

---

## Author

- Created by [Your Name]
- GitHub: https://github.com/yourusername/log-monitoring-app
