destination = ''
money_needed = 0
installment = 0
savings = 0


while destination != 'End':
    destination = input()
    if destination == 'End':
        break
    money_needed = float(input())
    while savings < money_needed:
        installment = float(input())
        savings += installment
    if savings >= money_needed:
        print(f'Going to {destination}!')
        savings = 0