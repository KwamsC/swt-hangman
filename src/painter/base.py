class BasePainter:
    def __init__(self, maxNumFails):
        self.maxNumFails = maxNumFails

    def draw_current_state(self, guess, word, numFails):
        if numFails == 0:
            print()
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('...........')
            print('The word: \n\t', end = '')
            for i, c in enumerate(word):
                if guess[i]:
                    print(c, end = '')
                else:
                    print('_', end = '')
            print()
            print()
        elif numFails == 1:
            print()
            print('..-------..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('The word: \n\t', end = '')
            for i, c in enumerate(word):
                if guess[i]:
                    print(c, end = '')
                else:
                    print('_', end = '')
            print()
            print()
        elif numFails == 2:
            print()
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('........|..')
            print('The word: \n\t', end = '')
            for i, c in enumerate(word):
                if guess[i]:
                    print(c, end = '')
                else:
                    print('_', end = '')
            print()
            print()
        elif numFails == 3:
            print()
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('....|...|..')
            print('....|...|..')
            print('........|..')
            print('........|..')
            print('The word: \n\t', end = '')
            for i, c in enumerate(word):
                if guess[i]:
                    print(c, end = '')
                else:
                    print('_', end = '')
            print()
            print()
        elif numFails == 4:
            print()
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('....|/..|..')
            print('....|...|..')
            print('........|..')
            print('........|..')
            print('The word: \n\t', end = '')
            for i, c in enumerate(word):
                if guess[i]:
                    print(c, end = '')
                else:
                    print('_', end = '')
            print()
            print()
        elif numFails == 5:
            print()
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('...\\|/..|..')
            print('....|...|..')
            print('........|..')
            print('........|..')
            print('The word: \n\t', end = '')
            for i, c in enumerate(word):
                if guess[i]:
                    print(c, end = '')
                else:
                    print('_', end = '')
            print()
            print()
        elif numFails == 6:
            print()
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('...\\|/..|..')
            print('....|...|..')
            print('.....\\..|..')
            print('........|..')
            print('The word: \n\t', end = '')
            for i, c in enumerate(word):
                if guess[i]:
                    print(c, end = '')
                else:
                    print('_', end = '')
            print()
            print()
        elif numFails == 7:
            print()
            print('..-------..')
            print('........|..')
            print('....O...|..')
            print('...\\|/..|..')
            print('....|...|..')
            print('.../.\\..|..')
            print('........|..')
            print('The word: \n\t', end = '')
            for i, c in enumerate(word):
                if guess[i]:
                    print(c, end = '')
                else:
                    print('_', end = '')
            print()
            print()

    def draw_win_state(self, word, numFails):
        print()
        print('Congratulations! You win!')
        print('The word is:\n\t', end = '')
        print(word)
        print()
        print()
        print('...........')
        print('....YOU....')
        print('....ARE....')
        print('.....A.....')
        print('...CHAMP...')
        print('...........')
        print()

    def draw_lose_state(self, guess, word):
        print()
        print('..-------..')
        print('....|...|..')
        print('....X...|..')
        print('...\\|/..|..')
        print('....|...|..')
        print('.../.\\..|..')
        print('........|..')
        print('You Lose!')
        print('The word is:\n\t', end = '')
        print(word)
        print()

    def get_new_guess(self):
        return input('Please guess a new character: ')
