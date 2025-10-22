from datetime import datetime
import os


def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for entry in log_data:
            f.write(f"{entry}\n")
    print(f"Log file created: {filename}")
    return filename

if __name__ == "__main__":
    sample = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample)