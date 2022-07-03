def creat_loading_bar(number):
    if number == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        print(f"{number}% [{'%' * (number // 10)}{'.' * (10 - number // 10)}]")
        print('Still loading...')


loading_number = int(input())
creat_loading_bar(loading_number)