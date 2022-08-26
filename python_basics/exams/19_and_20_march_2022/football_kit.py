shirt_price = float(input())
goal_sum = float(input())
ball_is_won = False
shorts_price = 0.75 * shirt_price
socks_price = 0.2 * shorts_price
shoes_price = 2 * (shirt_price + shorts_price)
total_sum = (shirt_price + shorts_price + socks_price + shoes_price) * 0.85
if total_sum >= goal_sum:
    ball_is_won = True


diff = abs(total_sum - goal_sum)
if ball_is_won:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_sum:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")