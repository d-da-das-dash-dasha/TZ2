data = []
with open("data.txt", "r") as file:
    line = file.readline()
    for x in line.split():
        data.append(float(x))


def _max(arr):
    mx = arr[0]
    for x in arr:
        if mx < x:
            mx = x
    return mx


def _min(arr):
    mn = arr[0]
    for x in arr:
        if mn > x:
            mn = x
    return mn


def _sum(arr):
    sum_arr = 0
    for x in arr:
        sum_arr += x
    return sum_arr


def _mult(arr):
    mult = 1
    for x in arr:
        mult *= x
    return mult
