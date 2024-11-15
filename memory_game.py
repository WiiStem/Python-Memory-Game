# William Stempka

import json
import random
import os
import time


def get_high_scores():
    """access the file for the high scores"""
    with open("high_scores.json", "r") as file:
        high_scores = json.load(file)
    return high_scores


def print_high_scores(high_scores):
    """prints the high scores"""
    print("High Scores")
    for i in range(0, len(high_scores)):
        print(f"{i + 1}. {high_scores[i]["name"]} - {high_scores[i]["score"]}")


def player_turn():
    """has the player enter the number that was on screen"""
    while True:
        start_time = time.time()
        resp = input("Enter the number you just saw: ")
        try:
            resp = int(resp)
            response_time = time.time() - start_time
            return resp, response_time
        except:
            ("Response includes a letter. Try again")


def append_score(name, high_scores, current_score):
    """if the players score is a new high score it will add it to high scores"""
    if current_score > high_scores[0]["score"]:
        high_scores.insert(0, {"name": name, "score": current_score})
        high_scores.pop()
    elif current_score > high_scores[1]["score"]:
        high_scores.insert(0, {"name": name, "score": current_score})
        high_scores.pop()
    elif current_score > high_scores[2]["score"]:
        high_scores.insert(0, {"name": name, "score": current_score})
        high_scores.pop()
    elif current_score > high_scores[3]["score"]:
        high_scores.insert(0, {"name": name, "score": current_score})
        high_scores.pop()
    elif current_score > high_scores[4]["score"]:
        high_scores.insert(0, {"name": name, "score": current_score})
        high_scores.pop()
    with open("high_scores.json", "a") as file:
        json.dumps(high_scores, indent=4)
    return high_scores


def main():
    """plays the game then prints if you had a new high score"""
    start_num = [100, 999]
    current_score = 0
    rounds = 1
    print("Welcome to the Number Memory Game!")
    name = input("Enter your name: ").strip()
    high_scores = get_high_scores()
    print_high_scores(high_scores)
    start_game = input(
        "Press Enter to start the game or 'q' to quit:").lower().strip()
    if start_game == "q":
        quit()
    while True:
        rand_num = random.randint(start_num[0], start_num[1])
        start_num[0] *= 10
        start_num[1] *= 10
        print(f"Remember the following numbers: {rand_num}")
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        resp = player_turn()
        rounds += 1
        if resp[0] == rand_num:
            current_score += int(100 / resp[1])
            print(f"Good job! \n Current Score: {current_score}")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Too bad!")
            break
    end_results(rounds, current_score)
    append_score(name, high_scores, current_score)
    print_high_scores(high_scores)


def end_results(rounds, current_score):
    """prints your score and how many rounds you made it"""
    print(f"You completed {
          rounds} rounds with a final score of {current_score}")


if __name__ == "__main__":
    while True:
        main()
        play_again = input(
            "Do you want to play again? (y/n): ").lower().strip()
        if play_again == "n":
            break
