# Method Number 1
def gettotal(a, b):
    total_sum = sum(range(a, b))
    return total_sum


# Method Number 2
def gettotalmethod2(a, b):
    total = 0
    for num in range(a, b + 1):
        total += num
    return total


if __name__ == "__main__":
    print(f"{gettotal(4212, 18912512 + 1)}")
    print(f"{gettotalmethod2(4212, 18912512 + 1)}")
