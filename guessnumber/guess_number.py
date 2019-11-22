import random


def get_player_answer():
    return '1234'


class GuessNumberGame:
    ROUND_COUNT = 6

    def __init__(self, answer=None):
        self.answer = answer

    def play(self, numbers):
        player_numbers = list(numbers)
        answer_numbers = list(self.answer)
        allCorrectCount = 0
        numbersCorrectCount = 0
        for number in player_numbers:
            if number in answer_numbers:
                if answer_numbers.index(number) == player_numbers.index(number):
                    allCorrectCount += 1
                else:
                    numbersCorrectCount += 1
        return '%sA%sB' % (allCorrectCount, numbersCorrectCount)

    def run(self):
        isSuccess = False
        for index in range(GuessNumberGame.ROUND_COUNT):
            player_answer = get_player_answer()
            answer = self.play(player_answer)
            if answer == '4A0B':
                isSuccess = True
                break
            else:
                print(answer)
        print('Game Over! You Win!' if isSuccess else 'Game Over! You Lose!')


class AnswerGenerator:
    def generate(self):
        answer = set()
        while len(answer) < 4:
            answer.add(str(random.randint(0, 9)))
        return ''.join(answer)
