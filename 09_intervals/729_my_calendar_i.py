"""
LeetCode 729: My Calendar I (Medium)
Time: O(n) per book call, Space: O(n)
"""


class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.bookings:
            if startTime < e and s < endTime:
                return False
        self.bookings.append((startTime, endTime))
        return True


if __name__ == "__main__":
    cal = MyCalendar()
    assert cal.book(10, 20) is True
    assert cal.book(15, 25) is False
    assert cal.book(20, 30) is True
    print("All My Calendar I tests passed!")

