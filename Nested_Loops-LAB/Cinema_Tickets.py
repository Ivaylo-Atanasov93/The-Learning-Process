movie = ''
free_seats = 0
ticket_type = ''
sold_seats = 0
student = 0
standard = 0
kids = 0
total_tickets = 0
flag = False

while not flag:
    movie = input()
    if movie == 'Finish':
        break
    free_seats = int(input())
    while ticket_type != 'End':

        ticket_type = input()
        if ticket_type == 'student':
            student += 1
            sold_seats += 1
            total_tickets += 1
        elif ticket_type == 'standard':
            standard += 1
            sold_seats += 1
            total_tickets += 1
        elif ticket_type == 'kid':
            kids += 1
            sold_seats += 1
            total_tickets += 1
        elif ticket_type == 'End':
            print(f'{movie} - {(sold_seats / free_seats) * 100:.2f}% full.')
        elif ticket_type == 'Finish':
            print(f'{movie} - {(sold_seats / free_seats) * 100:.2f}% full.')
            flag = True
            break
        if sold_seats == free_seats:
            print(f'{movie} - {(sold_seats / free_seats) * 100:.2f}% full.')
            break


    sold_seats = 0
    ticket_type = ''
    if flag:
        break


print(f'Total tickets: {total_tickets}')
print(f'{(student / total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kids / total_tickets) * 100:.2f}% kids tickets.')
