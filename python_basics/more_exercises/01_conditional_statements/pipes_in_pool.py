volume_of_the_pool = int(input())
pipe_one_per_hour = int(input())
pipe_two_per_hour = int(input())
hours_away = float(input())
pipe_one_filled = pipe_one_per_hour * hours_away
pipe_two_filled = pipe_two_per_hour * hours_away
pipes_total = pipe_one_per_hour * hours_away + pipe_two_per_hour * hours_away
liters_more = pipes_total - volume_of_the_pool
if pipes_total <= volume_of_the_pool:
    print (f"The pool is {pipes_total/volume_of_the_pool * 100:.2f}% full. "
           f"Pipe 1: {pipe_one_filled/pipes_total * 100:.2f}%. "
           f"Pipe 2: {pipe_two_filled/pipes_total * 100:.2f}%.")
else:
    print(f"For {hours_away} hours the pool overflows with {liters_more:.2f} liters.")