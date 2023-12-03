

def solve(fn):
    with open(fn) as f:
        games = f.readlines()
    total=0
    for game_number, game in enumerate(games):
        rounds = game.replace(';',',').replace(':', ',').split(',')[1:]
        # print(rounds)
        is_valid = True
        #no part of game has violated the limits
        #assume valid game, look for things to invalidate and then disregard
        for round in rounds:
            numbers = "".join([char for char in round if char.isnumeric()])
            text = "".join([char for char in round if char.isalpha()])
            # result = [int(numbers), text]
            if 'red' in text and int(numbers)>12:
                is_valid=False                
            elif 'green' in text and int(numbers)>13:
                is_valid=False
            elif 'blue' in text and int(numbers)>14:
                is_valid=False
        # print(game_number+1,is_valid)
        if is_valid:
            total+=(game_number+1)   
    return total 

def solve_two(fn):
    with open(fn) as f:
        games = f.readlines()
        power_sum=[]
        total=0
    for game_number, game in enumerate(games):
        rounds = game.replace(';',',').replace(':', ',').split(',')[1:]
        print(rounds)
        red_list=[]
        blue_list=[]
        green_list=[]
        for round in rounds:
            numbers = "".join([char for char in round if char.isnumeric()])
            text = "".join([char for char in round if char.isalpha()])
            if 'red' in text:
                red_list.append(int(numbers))
                
            elif 'blue' in text:
                blue_list.append(int(numbers))
                
            elif 'green' in text:
                green_list.append(int(numbers))       

        print('red', red_list)
        print('blue', blue_list)
        print('green', green_list)  

        red_list.sort()
        blue_list.sort()
        green_list.sort()

        red_min = red_list[-1]
        blue_min = blue_list[-1]
        green_min = green_list[-1]

        power_sum = red_min * blue_min * green_min
        total += power_sum
        print(power_sum)
        
    return total

def main():
    # assert solve('test.txt') == 8
    # print(solve('input.txt'))
    assert solve_two('test.txt') == 2286
    print(solve_two('test.txt'))
    print(solve_two('input.txt'))

if __name__ == '__main__':
    main()
        
