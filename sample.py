# Method Number 1
def gettotal(a,b):
    total_sum=sum(range(a,b))
    return(total_sum)

print(gettotal(4212,18912512+1))

# Method Number 2
def gettotalmethod2(a,b):
    total=0
    for num in range(4212,18912512+1):
        total+=num
    return total

print(gettotalmethod2(4212,18912512+1))