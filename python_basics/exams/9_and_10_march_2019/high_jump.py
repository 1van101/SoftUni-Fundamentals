goal = int(input())
failed = False
jumps_counter = 0
for jump in range(goal - 30, goal + 1, 5):
    fails_jumps_counter = 0
    current_jump = int(input())
    jumps_counter += 1
    if current_jump <= jump:
        current_height = jump
        fails_jumps_counter += 1
        for j in range(1, 3):
            current_fail_jump = int(input())
            fails_jumps_counter += 1
            jumps_counter += 1

            if current_fail_jump > jump:
                fails_jumps_counter = 0
                break
            if fails_jumps_counter == 3:
                failed = True
                break
    if failed:
        break
if failed:
    print(f"Tihomir failed at {current_height}cm after {jumps_counter} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {goal}cm after {jumps_counter} jumps.")
