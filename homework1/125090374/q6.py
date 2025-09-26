from typing import List, Tuple
def area(x1, x2, x3, x4, y1, y2, y3, y4):
    base1 = ( (x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    base2 = ( (x3 - x4) ** 2 + (y3 - y4) ** 2) ** 0.5
    if x1 == x2:
        height = x3 - x1
    else:
        k = (y2 - y1) / (x2 - x1)
        b1 = y1 - k * x1
        b2 = y2 - k * x2
        height = abs(b1 - b2) / (k ** 2 + 1)**0.5
    return (base1 + base2) * height /2

def trapezoid(arr: List[Tuple[float, float]]) ->float:
    x1 = arr[0][0]
    y1 = arr[0][1]
    x2 = arr[1][0]
    y2 = arr[1][1]
    x3 = arr[2][0]
    y3 = arr[2][1]
    x4 = arr[3][0]
    y4 = arr[3][1]
    if (x1 - x2) * (y3 - y4) == (x3 - x4) * (y1 - y2):
        return area(x1, x2, x3, x4, y1, y2, y3, y4)
    if (x1 - x3) * (y2 - y4) == (x2 - x4) * (y1 - y3):
        return area(x1, x3, x2, x4, y1, y3, y2, y4)
    if (x1 - x4) * (y2 - y3) == (x2 - x3) * (y1 - y4):
        return area(x1, x4, x3, x2, y1, y4, y3, y2)
