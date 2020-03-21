from collections import defaultdict

T = int(input())
for x in range(1, T + 1):
    N, Q = map(int, input().split())
    characters = input()
    counter = defaultdict(int)
    y = 0
    for i in range(Q):
        count=0
        L, R = map(int, input().split())
        characters1=characters[L-1:R]
        for character in characters1:
            counter[character] += 1
        for letter,val in counter.items():
            if val%2!=0 :
                count+=1
            if(count>=2):
                break
        if(count<2):
            y+=1
        counter.clear()
    print("Case #{}: {}".format(x,y))
