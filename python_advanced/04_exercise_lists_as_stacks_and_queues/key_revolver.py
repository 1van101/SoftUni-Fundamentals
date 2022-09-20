from collections import deque

price_per_bullet = int(input())
size_of_the_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
bullets_at_beginning = len(bullets)

for i in range(1, max(len(bullets), len(locks)) + 1):
    if not bullets or not locks:
        break
    bullet = bullets.pop()
    current_lock = locks[0]
    if bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    if i % size_of_the_barrel == 0 and bullets:
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = intelligence - ((bullets_at_beginning - len(bullets)) * price_per_bullet)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
# ================================================================================================
# price_per_bullet = int(input())
# size_of_the_barrel = int(input())
# bullets = [int(x) for x in input().split()]
# locks = deque([int(x) for x in input().split()])
# intelligence = int(input())
#
# fired_bullets = []
# shots = 0
# while bullets and locks:
#     if bullets and (shots == size_of_the_barrel):
#         print("Reloading!")
#         shots = 0
#     current_bullet = bullets.pop()
#     fired_bullets.append(current_bullet)
#     if current_bullet <= locks[0]:
#         print('Bang!')
#         locks.popleft()
#     else:
#         print('Ping!')
#     shots += 1
# if bullets and (shots == size_of_the_barrel):
#     print(f'Reloading!')
#
# if locks:
#     print(f"Couldn't get through. Locks left: {len(locks)}")
# else:
#     money_earned = len(fired_bullets) * price_per_bullet
#     print(f"{len(bullets)} bullets left. Earned ${intelligence - money_earned}")
