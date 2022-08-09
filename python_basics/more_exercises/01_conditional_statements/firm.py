import math

hours_needed = int(input())
days_company_has = int(input())
employees_working_extra = int(input())

working_hours = days_company_has * 8
hours_total = working_hours * 0.9 + employees_working_extra * days_company_has * 2
hours_total = math.floor(hours_total)
difference = abs(hours_needed - hours_total)
if hours_total >= hours_needed:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")