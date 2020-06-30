def hangman_game(text,answers):
    total_answer = 1
    for character in text:
        if answers.count(character) == 0:
            return False
        elif total_answer == len(text)+1:
            return True
        else:
            total_answer +=1
    return True

print(hangman_game("a",["abcdef"]))