import re

command = input()
total_income = 0

while not command == "end of shift":
    pattern = r"^%(?P<name>[A-Z][a-z]+)%[^|$%.]*<(?P<product>\w+)>[^|$%.]*\|(?P<count>\d+)\|[^|$%.0-9]*(?P<price>\d+(\.\d+)?)\$$"
    matches = re.finditer(pattern, command)
    for match in matches:
        current_income = int(match.group('count')) * float(match.group('price'))
        total_income += current_income
        print(f"{match.group('name')}: {match.group('product')} - {current_income:.2f}")
    command = input()

print(f"Total income: {total_income:.2f}")
# r"^%([A-Z][a-z]+)%[^|$%.]*<([^>]+)>([^|$%.]+)?\|(\3)?([0-9]+)(\3)?\|([^|$%.0-9]+)?(\d+(\.\d+)?)\$$"
# ===========================================================================================================
# NOT MINE!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
# import re
#
#
# def customer_order(_customer: str):
#     _order = dict()
#     pattern = re.compile(
#         r'%(?P<name>[A-Z][a-z]+)%([^|$%.]+)?<(?P<product>[\w\d]+)>([^|$%.]+)?\|(?P<count>\d+)\|([^\d|$%.]+)?(?P<cost>\d+(\.\d+)?)\$')
#     match = pattern.search(_customer)
#     if match:
#         _order = match.groupdict()
#     return _order
#
#
# total_income = 0
#
# while True:
#     customer = input()
#     if customer == 'end of shift':
#         break
#
#     order = customer_order(customer)
#     if order:
#         print(order['name'] + ':', order['product'] + ' -', f"{int(order['count']) * float(order['cost']):.2f}")
#         total_income += int(order['count']) * float(order['cost'])
#
# print(f'Total income: {total_income:.2f}')