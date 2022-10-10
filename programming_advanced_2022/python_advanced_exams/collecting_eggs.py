from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
papers_stack = [int(x) for x in input().split(", ")]

count_boxes = 0
size_box = 50

while True:
    if not eggs or not papers_stack:
        break

    egg = eggs.popleft()
    paper = papers_stack.pop()

    if egg <= 0:
        papers_stack.append(paper)
        continue

    if egg == 13:
        papers_stack.append(paper)
        papers_stack[0], papers_stack[-1] = papers_stack[-1], papers_stack[0]
        continue

    sum_element = egg + paper
    if sum_element <= size_box:
        count_boxes += 1

if count_boxes > 0:
    print(f"Great! You filled {count_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")
if papers_stack:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers_stack])}")