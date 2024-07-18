import random

def print_instructions():
    print("Winning rules of the game ROCK PAPER SCISSORS are :\n"
          "Rock vs Paper -> Paper wins\n"
          "Rock vs Scissors -> Rock wins\n"
          "Paper vs Scissors -> Scissors wins\n")

def get_user_choice():
    while True:
        print("Enter your choice:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        choice = input("Your choice: ")
        if choice in ('1', '2', '3'):
            return int(choice)
        else:
            print("Please enter a valid choice (1, 2, or 3)")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "Draw"
    elif (user_choice == 1 and comp_choice == 3) or \
         (user_choice == 2 and comp_choice == 1) or \
         (user_choice == 3 and comp_choice == 2):
        return "User"
    else:
        return "Computer"

def print_result(winner):
    if winner == "Draw":
        print("It's a Draw!")
    else:
        print(f"{winner} wins!")

def play_again():
    return input("Do you want to play again? (Y/N): ").strip().lower() == 'y'

def main():
    print_instructions()
    
    while True:
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()
        
        print(f"User choice: {'Rock' if user_choice == 1 else 'Paper' if user_choice == 2 else 'Scissors'}")
        print(f"Computer choice: {'Rock' if comp_choice == 1 else 'Paper' if comp_choice == 2 else 'Scissors'}")
        
        winner = determine_winner(user_choice, comp_choice)
        print_result(winner)
        
        if not play_again():
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
