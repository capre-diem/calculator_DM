class Natural:
    data: list[1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0]

    def __init__(self, value: str):
        data = []
        length = 0
        for digit in value:
            data = [digit] + data
            length += 1
        pass