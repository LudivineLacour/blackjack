#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:53:48 2020

@author: ludivinelacour
"""

import random
import time

card_values = {"one":1,"two":2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten":10, "jack": 10, "queen": 10, "king": 10, "ace": 11} 
cards = 4*[ "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
ten_cards = [keys for keys,values in card_values.items() if values == 10]


def draw_cards(player, player_cards, deck_cards):

    """ This function allow to draw a random card for the dealer or the player.
        The card is removed from the deck once distributed.
        
        Input: 
        - player: the type of player either the player or the dealer
        - player_cards: the list containing the cards of the player
        - deck_cards: the list containing all the cards 
        
        Output:
        - player_cards: the list of cards for the player who just draw the card
        - deck_card: the initial deck with the removed card
    """
    
    # Random card picker
    random_card = random.choice(deck_cards)
    deck_cards.remove(random_card)

    # Print initial state
    if player == "dealer" and player_cards == []:    
        print('The dealer has been served. The card is faced down.')
    else:
        print(f'The {player} card is: {random_card}')
    
    # Add the new to the player's list of cards
    player_cards.append(random_card)
    
    return


def score(player_cards):
    
    """ The function calculates the score of the cards.
        If there is at least one ace, there are several scores depending on the value of the ace (1 or 11)
    
        Input: the list of cards
        Output: list of score(s)
    """
    
    score = [0]
    global card_values 
    
    for card in player_cards:
        if card != "ace":
            for i in range(len(score)):
                score[i]+=card_values[card]
        else:
            score1 = score[:]
            score11 = score[:]
            for i in range(len(score)):
                score1[i] += 1
                score11[i] += 11
            score = score1 + score11
    
    return set(score)


def max_score(player_cards):
    
    """ The function go through the score of the player and if the player got an ace, takes the best score below 21. 
        If no score below 21, it takes the minimum score.
        
        Input: the list of the cards of the player
        Output: integer
    """
    
    score_list = score(player_cards)
    result = 0
    
    for s in score_list:
        if s <= 21:
            result=max(s,result)
    
    if result==0:
        result=min(score_list)
        
    return result


def print_cards(player, player_cards):    
    
    """ The function prints a sentence to display the cards of the player
    
        Input: 
        - player: the type of player whom we'd like to display the cards
        - player_cards: the list of cards for the chosen player
        
        Output: no output, it only prints a sentence
    """
    
    sentence=f"{player}'s cards:"  
    
    for card in player_cards:
        sentence+=" "+str(card)+","
    
    print(sentence[:-1])
    
    
def display_result(dealer_score, dealer_cards, player_score, player_cards):
    
    print("Dealer score is", dealer_score, ", Player score is", player_score)  
    
    if dealer_score > 21:
        print ("Dealer busts. You win!\n") 
        
    elif ((len(player_cards) == 2) and (player_score == 21)) or player_score > dealer_score:
            if (len(dealer_cards) == 2) and (dealer_score == 21):
                print("You both have a Blakjack! No winner.\n")
            else:
                print("Congratulations. You win\n")
             
    elif ((len(dealer_cards) == 2) and (dealer_score == 21)) or player_score < dealer_score:
        print ("Sorry. You lose.\n")

    elif dealer_score == player_score:
        print("Same score! No winner.\n")  
        
    else:
        print("unknown case")
        

def game():
    
    global cards
    global ten_cards

    player_cards=[]
    dealer_cards=[]
    
    print("""          ==================================================================
          ==================================================================
          =============== Welcome to the Blackjack game ====================
          ==================================================================
          ==================================================================""")
    
    ### 1st step: Beginning of the game. Draw the first 2 cards
    time.sleep(1)
    print(f"\n == Start drawing ==")
    for i in range(2):
        print(f"Drawing tour number {i+1}")
        draw_cards("player", player_cards, cards)
        time.sleep(1.5)
        draw_cards("dealer", dealer_cards, cards)
        time.sleep(1.5)
    
    player_score = max_score(player_cards)
    
    ### 2nd step: what the player would like to do? if the player hit, he draws a new card.
    print(f"\n == Player to go ==")
    
    while player_score <= 21:
        print_cards("Player",player_cards)
        time.sleep(1.5)
        
        if len(player_cards) == 2 and ('ace' in player_cards) and list(filter(lambda x: x in player_cards, ten_cards)):
            print("Congrats! You've got a Blackjack.")
            break
            
        usr_inp = input('What do you want to do? hit or stand >> ')# The player is able to hit unlimited until he reach more than 21 or stand 
        if usr_inp == 'hit':
            draw_cards("player", player_cards, cards)
            player_score = max_score(player_cards)
        else:
            break

        
    if player_score > 21:
        return f"You're score is {player_score}. You're out. End of the game."
    
    ### 3rd step: if the dealer is under 17, he continues to draw card otherwise we compare the score
    print(f"\n == Dealer to go ==")   
    
    print_cards("Dealer", dealer_cards)
    time.sleep(1.5)
    
    dealer_score = max_score(dealer_cards)
   
    while dealer_score < 17:
        # dealer keeps playing and draw cards
        print(f'The dealer is under 17. New card draw.')
        draw_cards("dealer", dealer_cards, cards)
        dealer_score = max_score(dealer_cards)
        time.sleep(1.5)

    if len(dealer_cards) == 2 and ('ace' in dealer_cards) and list(filter(lambda x: x in dealer_cards, ten_cards)):
        print("That's a Blackjack for the Dealer!")        
            
    ### 4th step: if no Blackjack, comparison of the players scores
    print(f"\n == Let's check the winner ==")
    return display_result(dealer_score, dealer_cards, player_score, player_cards)


if __name__ == '__main__':
    game()