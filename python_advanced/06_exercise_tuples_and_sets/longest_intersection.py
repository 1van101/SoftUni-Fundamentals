def get_set(start, end):
    return {x for x in range(start, end + 1)}


n = int(input())
intersections = []

for i in range(n):
    first_range, second_range = input().split("-")
    first_start, first_end = first_range.split(",")
    second_start, second_end = second_range.split(",")

    first_set = get_set(int(first_start), int(first_end))
    second_set = get_set(int(second_start), int(second_end))
    current_intersection = first_set.intersection(second_set)
    intersections.append(current_intersection)

longest_intersection = max(intersections, key=len)

print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}]"
      f" with length {len(longest_intersection)}")

#======================================================================================
# def get_set(start, end):
#     return {x for x in range(start, end + 1)}
#
#
# def get_intersection(set1, set2):
#     return set1.intersection(set2)
#
#
# n = int(input())
#
# all_intersections = {}
# for _ in range(n):
#     first, second = input().split("-")
#     first_start, first_end = first.split(",")
#     second_start, second_end = second.split(",")
#     first_set = get_set(int(first_start), int(first_end))
#     second_set = get_set(int(second_start), int(second_end))
#     intersection = get_intersection(first_set, second_set)
#     if not len(intersection) in all_intersections:
#         all_intersections[len(intersection)] = intersection
#
# longest = max(all_intersections)
#
# print(f"Longest intersection is [{', '.join([str(x) for x in all_intersections[longest]])}] with length {longest}")