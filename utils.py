from datetime import datetime
from typing import List, Tuple, Dict

def parse_time(time_str: str) -> datetime:
    """Convert HH:MM:SS string to datetime object."""
    return datetime.strptime(time_str.strip(), "%H:%M:%S")


def parse_log_file(filename: str, warn_threshold: int, error_threshold: int) -> List[Tuple[str, str, float, str]]:
    """
    Reads the log file and computes job durations.

    Expected line format:
    HH:MM:SS, job name, START/END, PID
    """
    jobs: Dict[str, Dict] = {}
    results: List[Tuple[str, str, float, str]] = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = [p.strip() for p in line.split(",")]
            if len(parts) != 4:
                print(f"?? Skipping malformed line: {line}")
                continue

            time_str, job_name, event, pid = parts
            timestamp = parse_time(time_str)

            if event.upper() == "START":
                jobs[pid] = {"start": timestamp, "name": job_name}
            elif event.upper() == "END":
                if pid in jobs:
                    start_time = jobs[pid]["start"]
                    duration = (timestamp - start_time).total_seconds() / 60  # minutes

                    if duration > error_threshold:
                        status = "ERROR"
                    elif duration > warn_threshold:
                        status = "WARNING"
                    else:
                        status = "OK"

                    results.append((pid, jobs[pid]["name"], duration, status))
                    del jobs[pid]
                else:
                    print(f"?? END without START for PID {pid}: {line}")
            else:
                print(f"?? Unknown event type: {event}")

    # If any jobs never finished
    for pid, info in jobs.items():
        results.append((pid, info["name"], 0, "INCOMPLETE"))

    return results


def generate_report(results: List[Tuple[str, str, float, str]], output_file: str):
    """Writes results to output file."""
    with open(output_file, "w") as out:
        out.write("PID | Job Name | Duration (min) | Status\n")
        out.write("-" * 60 + "\n")
        for pid, name, duration, status in results:
            out.write(f"{pid} | {name} | {duration:.2f} | {status}\n")
