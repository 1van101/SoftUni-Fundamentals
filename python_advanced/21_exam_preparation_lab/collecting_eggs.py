from collections import deque


box_capacity = 50
filled_boxes = 0

eggs = deque([int(x) for x in input().split(", ")])
papers = [int(x) for x in input().split(", ")]

while eggs and papers:
    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue

    if current_egg == 13:
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    current_paper = papers.pop()
    result = current_egg + current_paper

    if result <= box_capacity:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")

if papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")