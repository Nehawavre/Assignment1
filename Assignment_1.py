import random


class Message:
    msg = """
    Welcome to Snake and Ladder Game.

    Rules:
      1. Initially both the players are at starting position 0. 
      2. You have to choose how many players.
      3.You can choose 2 or 3 or 4.
      4.Then play your game when it's your turn just enter player number there.
      5. The first player to get to the FINAL position is the winner.
    """
    print(msg)


class SnakeLadder(Message):
    pos1 = 0
    pos2 = 0
    pos3 = 0
    pos4 = 0
    def Game(pos) :
        ladder = {1: 38, 4: 14, 8: 31, 21: 42, 28: 84, 51: 67, 71: 91, 80: 100}
        snake = {17: 7, 54: 34, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 79}

        snake_bite = ["boohoo", "bummer", "snake bite", "oh no", "dang"]
        ladder_jump = ["woohoo", "woww", "nailed it", "oh my God...", "yaayyy"]
        dice = random.randint(1, 6)
        print("dice throw value:", dice)
        pos = pos + dice
        if pos in ladder:
            pos = ladder[pos]
            print(random.choice(ladder_jump))
            print("It is a ladder BRAVO..")
            print("position:", pos)
            print("\n")
        elif pos in snake:
            pos = snake[pos]
            print(random.choice(snake_bite))
            print("It is a snake...")
            print("position:", pos)
            print("\n")
        else:
            print("Moved to position:", pos)
            print("\n")
        return pos

    while True:
        a = int(input("Choose how many Player:"))
        while a == 2:
            b = int(input(f"Player 1 or 2:"))
            if b == 1:
                pos1 = Game(pos1)
                if pos1 == 100:
                    print("Congrats Player 1")
                    break
            if b == 2:
                pos2 = Game(pos2)
                if pos2 == 100:
                    print("Congrats Player 2")
                    break
        while a == 3:
            c = int(input("Player 1 or 2 or 3:"))
            if c == 1:
                pos1 = Game(pos1)
                if pos1 == 100:
                    print("Congrats Player 1")
                    break
            if c == 2:
                pos2 = Game(pos2)
                if pos2 == 100:
                    print("Congrats Player 2")
                    break
            if c == 3:
                pos3 = Game(pos3)
                if pos3 == 100:
                    print("Congrats Player 3")
                    break
        while a == 4:
            d = int(input("Player 1 or 2 or 3 or 4:"))
            if d == 1:
                pos1 = Game(pos1)
                if pos1 == 100:
                    print("Congrats Player 1")
                    break
            if d == 2:
                pos2 = Game(pos2)
                if pos2 == 100:
                    print("Congrats Player 2")
                    break
            if d == 3:
                pos3 = Game(pos3)
                if pos3 == 100:
                    print("Congrats Player 3")
                    break
            if d == 4:
                pos4 = Game(pos4)
                if pos4 == 100:
                    print("Congrats Player 4")
                    break


obj = SnakeLadder()
obj.Game()
