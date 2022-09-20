boxes_with_clothes = [int(x) for x in input().split()]
capacity_per_rack = int(input())

current_sum_of_boxes = 0
racks_counter = 1

while boxes_with_clothes:
    current_box = boxes_with_clothes[-1]
    if current_sum_of_boxes + current_box <= capacity_per_rack:
        current_sum_of_boxes += current_box
        boxes_with_clothes.pop()
    else:
        current_sum_of_boxes = 0
        racks_counter += 1

print(racks_counter)