n = int(input())
odd = set()
even = set()
summ = 0

for i in range(1,n + 1):
    name = input()
    for n in name:
        summ += ord(n)
    summ = int(summ / i)
    if summ % 2 == 0:
        even.add(summ)
    else:
        odd.add(summ)
    summ = 0

even_sum  = sum(even)
odd_sum  = sum(odd)

if even_sum == odd_sum:
    print(', '.join(map(str, odd.union(even))))
elif even_sum < odd_sum:
    print(', '.join(map(str,odd.difference(even))))
elif even_sum > odd_sum:
    print(', '.join(map(str,odd.symmetric_difference(even))))



