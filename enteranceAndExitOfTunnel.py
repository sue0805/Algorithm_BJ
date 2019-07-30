N = int(input())
cars = int(input())
max_car = 0
for i in range(0, N):
    enter, out = map(int, input().split())
    cars = cars + enter - out
    if cars < 0:
        max_car = 0
        break
    max_car = max(max_car, cars)
print(max_car)