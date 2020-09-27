n = int(input())
set1 = set()
set2 = set()
longest_intersection = set()

for i in range(n):
    ranges = input().split('-')
    first = ranges[0].split(',')
    second = ranges[1].split(',')
    start1 = int(first[0])
    end1 = int(first[1])
    start2 = int(second[0])
    end2 = int(second[1])
    for i in range(start1, end1+ 1):
        set1.add(i)
    for j in range(start2, end2+ 1):
        set2.add(j)
    if len(set1.intersection(set2)) > len(longest_intersection):
        longest_intersection = set1.intersection(set2)
    set1 = set()
    set2 = set()

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")
