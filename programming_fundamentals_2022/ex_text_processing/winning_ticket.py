def count_symbols(part_ticket, win_symbol):
    count_repeats = 0
    max_repeat = 0
    for current_chr in part_ticket:
        if current_chr == win_symbol:
            count_repeats += 1
        else:
            if count_repeats > max_repeat:
                max_repeat = count_repeats
                count_repeats = 0
    if max_repeat == 0:
        max_repeat = count_repeats
    return max_repeat


collection_of_tickets = input().split(", ")
winning_symbols = ["@", "#", "$", "^"]
for ticket in collection_of_tickets:
    ticket_is_not_winning = True
    ticket = ticket.strip()
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    for symbol in winning_symbols:
        left_part = ticket[:10]
        right_part = ticket[10:]
        if symbol in ticket and ticket.count(symbol) == 20:
            ticket_is_not_winning = False
            print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
            continue
        elif symbol * 6 in left_part and symbol * 6 in right_part:
            count_symbol_left_part = count_symbols(left_part, symbol)
            count_symbol_right_part = count_symbols(right_part, symbol)
            match_length = min(count_symbol_left_part, count_symbol_right_part)
            ticket_is_not_winning = False
            print(f'ticket "{ticket}" - {match_length}{symbol}')
            continue
    if ticket_is_not_winning:
        print(f'ticket "{ticket}" - no match')


