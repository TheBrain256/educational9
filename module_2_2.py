first = int(input())
second = int(input())
third = int(input())
if first == second and third == first:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

