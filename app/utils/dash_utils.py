from math import floor


def range_to_marks(start, end, count):
    step = (end - start) / count
    marks = [start]
    for i in range(count):
        marks.append(marks[-1] + step)
    marks[-1] = end
    return {
        mark: str(mark) for mark in map(lambda x: round(x), marks)
    }
