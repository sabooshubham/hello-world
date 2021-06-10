# cook your dish here
t = int(input())
w = l = tp1 = tp2 = 0 
for i in range(t):
    p1, p2 = map(int, input().split())
    tp1 += p1
    tp2 += p2
    diff = abs(tp1 - tp2)
    if l < diff:
        l = diff
        w = 1 if tp1 > tp2 else 2
print(w,l)