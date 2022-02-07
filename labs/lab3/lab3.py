"""
<Mena Hakim>
<Lab 3>
<Department of Transportation Lab. This program calculates the average of cars traveled on different days and then
at the very end calculates the total number of cars traveled and the average vehicles per road.
"""
def traffic():
    roads = eval(input("How many roads were surveyed?"))
    total_acc = 0

    for i in range(roads):
        road_acc = 0
        print("How many days was road", i + 1, "surveyed?")
        days = eval(input(" "))
        for j in range(days):
            print("How many cars traveled on day", j + 1, "?")
            cars = eval(input(" "))
            road_acc = road_acc + cars
        avg = road_acc / days
        print("Road", i + 1, "average vehicles per day:", avg)
        total_acc = total_acc + road_acc
    print("Total numbers of vehicles traveled on all roads:", total_acc)
    total_avg = total_acc / roads
    print("Average number of vehicles per road:", round(total_avg, 2))


traffic()



