from p1_random import P1Random

rng = P1Random() # outside of the loop

# print(rng.next_int(13)+1)


game_continue = True
game_num = 0
player_wins = 0
dealer_wins = 0
tie_games = 0
total_games = 0

# The while loop will control the number of games the player will play.
while game_continue:

    # 1. This will print the game number message.
    game_num = game_num + 1
    print(f"START GAME #{game_num}")
    print("")
    player_hand = 0
    # the set of if elif statements is how you deal a card to the player.
    card = rng.next_int(13) + 1    # [0,12] + 1 => [1,13]
    if card == 1:
        print(f"Your card is a ACE!")
        card = 1
    elif card == 2:
        print(f"Your card is a 2!")
        card = 2
    elif card == 3:
        print(f"Your card is a 3!")
        card = 3
    elif card == 4:
        print(f"Your card is a 4!")
        card = 4
    elif card == 5:
        print(f"Your card is a 5!")
        card = 5
    elif card == 6:
        print(f"Your card is a 6!")
        card = 6
    elif card == 7:
        print(f"Your card is a 7!")
        card = 7
    elif card == 8:
        print(f"Your card is a 8")
        card = 8
    elif card == 9:
        print(f"Your card is a 9!")  # There are easier ways to print these statements, but I chose to lay them out so I can examine each individial line of code.
        card = 9
    elif card == 10:
        print(f"Your card is a 10!")
        card = 10
    elif card == 11:
        print(f"Your card is a JACK!")
        card = 10
    elif card == 12:
        print(f"Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print(f"Your card is a KING!")
        card = 10
    player_hand += card  # This adds the card value to the player hand.


    print(f"Your hand is: {player_hand}")
    print("")
    print("1. Get another card")
    print("2. Hold hand")
    print("3. Print statistics")
    print("4. Exit")
    print("")

    no_winner = True

    while no_winner:

        option = int(input("Choose an option: "))   # This prompts the user to input whether they want another card, hold hand, print stats, or exit the program.
        print("")

        if option == 1:

            card = rng.next_int(13) + 1

            if card == 1:
                print(f"Your card is a ACE!")
                card = 1
            elif card == 2:
                print(f"Your card is a 2!")
                card = 2
            elif card == 3:
                print(f"Your card is a 3!")
                card = 3
            elif card == 4:
                print(f"Your card is a 4!")
                card = 4
            elif card == 5:
                print(f"Your card is a 5!") # Needed to reprint the set of if elif statements inside the inner while loop.
                card = 5
            elif card == 6:
                print(f"Your card is a 6!")
                card = 6
            elif card == 7:
                print(f"Your card is a 7!")
                card = 7
            elif card == 8:
                print(f"Your card is a 8!")
                card = 8
            elif card == 9:
                print(f"Your card is a 9!")
                card = 9
            elif card == 10:
                print(f"Your card is a 10!")
                card = 10
            elif card == 11:
                print(f"Your card is a JACK!") # Even though the card is a Jack the value is still considered a 10.
                card = 10
            elif card == 12:
                print(f"Your card is a QUEEN!") # Still considered a 10.
                card = 10
            elif card == 13:
                print(f"Your card is a KING!") # Still considered a 10.
                card = 10
            player_hand += card

            print(f"Your hand is: {player_hand}")

            if player_hand != 21 and player_hand < 21:  # Needed to reprint the menu option before the input, so I added this if statement.
                print("")
                print("1. Get another card")
                print("2. Hold hand")
                print("3. Print statistics")
                print("4. Exit")
                print("")

            if player_hand == 21:
                    print("")
                    print("BLACKJACK! You win!") # If the player gets 21, they automatically win.
                    print("")
                    player_wins += 1
                    total_games += 1
                    break
            elif player_hand > 21:     # If the player exceeds 21 they lose.
                    print("")
                    print("You exceeded 21! You lose.")
                    print("")
                    dealer_wins += 1
                    total_games += 1
                    break



        elif option == 2:

            dealer_hand = rng.next_int(11)+16 # deal a card to the dealer.

            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            print("")

            if dealer_hand > player_hand and dealer_hand <= 21:
                print("Dealer wins!")
                print("")
                dealer_wins += 1      # If the dealer_hand == 21, print losing message, increment dealer hand by 1.
                total_games += 1       # Update the number of games and the number of player/dealer wins.
                break
            if player_hand > dealer_hand and player_hand <= 21:
                print("BLACKJACK! You win!")
                print("")
                player_wins += 1
                total_games += 1
                break
            if dealer_hand > 21:
                print("You win!")  # If the dealer exceeds 21 they lose.
                print("")
                player_wins += 1
                total_games += 1
                break
            if player_hand == dealer_hand:
                print("It's a tie! No one wins!")
                print("")
                tie_games += 1
                total_games += 1
                break


        elif option == 3:
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {dealer_wins}")
            print(f"Number of tie games: {tie_games}")
            print(f"Total # of games played is: {total_games} ")
            percentage_wins = (player_wins / total_games) * 100             # Operation to get percentage
            print(f"Percentage of Player wins: {percentage_wins:0.1f}%")    # Needed one decimal place
            print("")
            print("1. Get another card")
            print("2. Hold hand")
            print("3. Print statistics")            # Reprint the menu before the operation input
            print("4. Exit")
            print("")
            continue


        elif option == 4:
            no_winner = False # get outside the inner while loop
            game_continue = False # get outside of outer while loop
        else:
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")
            print("")
            print("1. Get another card")
            print("2. Hold hand")
            print("3. Print statistics")
            print("4. Exit")
            print("")
            continue
            # print invalid message if the user inputs a number outside of the range.



