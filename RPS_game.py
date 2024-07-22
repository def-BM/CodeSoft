from tkinter import *
import random

# Function to generate random choice from computer 
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Scissors" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

# Function for game logic
def play(user_choice):
    global rounds_played, user_score, computer_score  # global variables
    if rounds_played < 3:
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        user_label.config(text=f"You chose: {user_choice}")
        computer_label.config(text=f"Computer chose: {computer_choice}")
        
        # Update score
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

        rounds_played += 1
        
        # Declaring final result after 3 rounds
        if rounds_played == 3:
            if user_score > computer_score:
                final_result = "You win!"
            elif computer_score > user_score:
                final_result = "Computer Win!"
            else:
                final_result = "It's a tie."
            final_result_label.config(text=final_result)

# Function to reset the game and play again
def play_again():
    global user_score, computer_score, rounds_played
    user_score = 0
    computer_score = 0
    rounds_played = 0
    user_label.config(text='You chose: ')
    computer_label.config(text='Computer chose: ')
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")
    final_result_label.config(text="")

# Initialize scores and rounds
user_score = 0
computer_score = 0
rounds_played = 0

# Create the main window
root = Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("500x500+300+200")
root.configure(bg='#FFC0CB')
root.resizable(False, False)

rock_button = Button(root, text="Rock", width=10, background='#00008B', activebackground='#00008B', fg='white', activeforeground='white', command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=(10,100), pady=10)

paper_button = Button(root, text="Paper", width=10, background='#00008B', activebackground='#00008B', fg='white', activeforeground='white',command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=(10,100), pady=10)

scissors_button = Button(root, text="Scissors", width=10, background='#00008B', activebackground='#00008B', fg='white', activeforeground='white', command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=(10,100), pady=10)

user_label = Label(root, text='You chose: ', bg='#FFC0CB',font=("Helvetica", 14))
user_label.place(x=50, y=100)

computer_label =Label(root,text='Computer chose: ', bg='#FFC0CB', font=("Helvetica", 14))
computer_label.place(x=250,y=100)

score_label = Label(root, text=f"Score - You: {user_score}, Computer: {computer_score}", bg='#FFC0CB', font=("Helvetica", 14))
score_label.place(x=50, y=200)

final_result_label = Label(root, text="", bg='#FFC0CB',fg='red', font=('Microsoft YaHei UI Light',23,'bold'))
final_result_label.place(x=180, y=300)

play_again_button = Button(root, text="Play again", width=10, background='#00008B', activebackground='#00008B', fg='white', activeforeground='white', command=play_again)
play_again_button.place(x=200, y=400)

root.mainloop()