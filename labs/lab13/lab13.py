from graphics import Rectangle, Point


def is_in_binary(search_val, values):
    lowest = 0
    highest = len(values) - 1
    while lowest <= highest:
        middle = (highest + lowest) // 2
        if values[middle] < search_val:
            lowest = middle + 1
        elif values[middle] > search_val:
            highest = middle - 1
        else:
            return True
    return False


def selection_sort(values):
    for i in range(len(values)):
        lowest = i
        for j in range(i+1, len(values)):
            if values[lowest] > values[j]:
                lowest = j
        values[i], values[lowest] = values[lowest], values[i]
    return values


my_rect = [Rectangle(Point(1.0, 1.0), Point(25.0, 25.0)),
           Rectangle(Point(1.0, 1.0), Point(5.0, 5.0)),
           Rectangle(Point(1.0, 1.0), Point(25.0, 25.0))]


def calc_area(rect):
    x1 = rect.getP1().getX()
    x2 = rect.getP2().getX()
    y1 = rect.getP1().getY()
    y2 = rect.getP2().getY()
    area = (x2 - x1) * (y2 - y1)
    return int(area)


def rect_sort(rectangles):
    for i in range(len(rectangles)):
        lowest = calc_area(rectangles[i])
        for j in range(i + 1, len(rectangles)):
            k = calc_area(rectangles[j])
            if lowest > k:
                lowest = j
        rectangles[i], rectangles[i] = rectangles[i], rectangles[i]
    return rectangles


def trade_alert(file_name):
    f = open(file_name, "r")
    line = f.readline()
    line_split = "".join(line.split(',')[0:])
    numbers = line_split.split()
    for volume in range(len(numbers)):
        if volume > 830:
            print("Warning, maximum trading volume has been reached!")
        elif volume == 500:
            print("Pay attention, trading volume has reached 500!")
        print(volume)


if __name__ == '__main__':
    print(is_in_binary(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(selection_sort([10, 5, 7, 9, 3]))
    print(rect_sort(my_rect))
    trade_alert("trades.txt")
