"""
LeetCode 359: Logger Rate Limiter (Easy)
Time: O(1) per call, Space: O(M) where M is number of unique messages
"""


class Logger:
    def __init__(self):
        self.next_ok = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.next_ok and timestamp < self.next_ok[message]:
            return False
        self.next_ok[message] = timestamp + 10
        return True


if __name__ == "__main__":
    logger = Logger()
    assert logger.shouldPrintMessage(1, "foo") is True
    assert logger.shouldPrintMessage(2, "bar") is True
    assert logger.shouldPrintMessage(3, "foo") is False
    assert logger.shouldPrintMessage(8, "bar") is False
    assert logger.shouldPrintMessage(10, "foo") is False
    assert logger.shouldPrintMessage(11, "foo") is True
    print("All Logger Rate Limiter tests passed!")

