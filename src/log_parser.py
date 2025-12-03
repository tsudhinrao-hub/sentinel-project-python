import re

# Regex pattern for common access logs (like nginx/apache style)
LOG_PATTERN = re.compile(
    r'(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<endpoint>\S+) \S+" (?P<status>\d{3})'
)

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        return match.groupdict()
    return None

if __name__ == "__main__":
    # Test sample
    test_line = '127.0.0.1 - - [24/Nov/2025:12:34:56 +0000] "GET /index.html HTTP/1.1" 200'
    print(parse_log_line(test_line))