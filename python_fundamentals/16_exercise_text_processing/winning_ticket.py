def is_winning(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    symbols = ['@', '#', '$', '^']
    first_half = ticket[:10]
    second_half = ticket[10:]
    for symbol in symbols:
        for reps in range(10, 0, -1):
            total_reps = reps * symbol
            if total_reps in first_half and total_reps in second_half:
                if reps == 10:
                    return f'ticket "{ticket}" - {reps}{symbol} Jackpot!'
                elif 6 <= reps <= 9:
                    return f'ticket "{ticket}" - {reps}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets_input = [s.strip() for s in input().split(", ")]

for ticket in tickets_input:
    print(is_winning(ticket))

# ====================================
# def is_valid_ticket(ticket):
#     if len(ticket) == 20:
#         return True
#     return False
#
#
# def winning_half(symbols, ticket):
#     winning_symbols_in_ticket = []
#     last_symbol = None
#     for i in range(len(ticket)):
#         current_char = ticket[i]
#         if current_char in symbols:
#             if len(winning_symbols_in_ticket) > 0:
#                 if not current_char == last_symbol:
#                     if len(winning_symbols_in_ticket) < 6:
#                         winning_symbols_in_ticket = []
#                     else:
#                         break
#             winning_symbols_in_ticket.append(current_char)
#             last_symbol = current_char
#         else:
#             if len(winning_symbols_in_ticket) < 6:
#                 winning_symbols_in_ticket = []
#             else:
#                 break
#     if len(winning_symbols_in_ticket) >= 6:
#         return winning_symbols_in_ticket
#     return False
#
#
# given_tickets = [s.strip() for s in input().split(", ")]
# winning_symbols = ['@', '#', '$', '^']
#
# for ticket in given_tickets:
#     if is_valid_ticket(ticket):
#         left_half = ticket[:10]
#         right_half = ticket[10:]
#         left_symbols = winning_half(winning_symbols, left_half)
#         right_symbols = winning_half(winning_symbols, right_half)
#         if left_symbols and right_symbols:
#             if left_symbols[0] == right_symbols[0]:
#                 if len(left_symbols) == 10 and len(right_symbols) == 10:
#                     print(f'ticket "{ticket}" - {len(left_symbols)}'
#                           f'{left_symbols[0]} Jackpot!')
#                 else:
#                     print(f'ticket "{ticket}" - {min(len(right_symbols), len(left_symbols))}'
#                           f'{right_symbols[0]}')
#             else:
#                 print(f'ticket "{ticket}" - no match')
#         else:
#             print(f'ticket "{ticket}" - no match')
#     else:
#         print("invalid ticket")
