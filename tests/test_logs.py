from utils import parse_log_file

def test_short_job(tmp_path):
    log_file = tmp_path / "short_job.log"
    log_file.write_text(
        "12:00:00, PID 1, JobX, START\n"
        "12:02:00, PID 1, JobX, END\n"
    )
    result = parse_log_file(log_file, 5, 10)
    assert result[0][3] == "OK"


def test_warning_job(tmp_path):
    log_file = tmp_path / "warn_job.log"
    log_file.write_text(
        "12:00:00, PID 2, JobY, START\n"
        "12:07:00, PID 2, JobY, END\n"
    )
    result = parse_log_file(log_file, 5, 10)
    assert result[0][3] == "WARNING"


def test_error_job(tmp_path):
    log_file = tmp_path / "error_job.log"
    log_file.write_text(
        "12:00:00, PID 3, JobZ, START\n"
        "12:12:00, PID 3, JobZ, END\n"
    )
    result = parse_log_file(log_file, 5, 10)
    assert result[0][3] == "ERROR"
