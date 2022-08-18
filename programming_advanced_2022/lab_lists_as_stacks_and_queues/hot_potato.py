from collections import deque

kids = deque(input().split())
toss = int(input())
while len(kids) > 1:
    kids.rotate(-toss)
    removed_kid = kids.pop()
    print(f"Removed {removed_kid}")
print(f"Last is {kids.pop()}")