# find sum of all multiples of 3 and 5:
def sum_multiples_three_five(n):
    print(sum([x for x in range(n) if (x%5==0 or x%3==0)]))

sum_multiples_three_five(1000)
