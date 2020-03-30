# Blackjack
*[Ludivine L. & Mike W.]*

*[Data Analytics, Paris, March 2020]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)

## Project Description
Build the blackjack game using python programmation.

## Rules

A player plays against the dealer. The main goal for the player is to get a total value of their cards above the dealer and under 21 without knowing all the cards of the dealer.

First two cards are distributed to the player and the dealer. Only the second card of the dealer is shown, the first one is faced down. 

Then, the player is allowed to hit (continue to play and draw a card) or stand (stay with the cards received).

If the player is not above 21, the dealer reveals their cards. 
If the total value of the dealer's card is under 17, they'll need to draw a card until they reach a point between 17 and 21.
Then, we compare the results. The winner is the one with the highest value of cards under 21. 

Bonus: if one of the player (player or dealer) gets an Ace and a Head (Queen, Jack, King), it's a BlackJack!

## Workflow

**Materials for the game:**
* List with the deck of 52 cards
* Dictionnary containing the values of cards
* One player and one dealer

A main function to go through the steps of the game:
* 1st step: Beginning of the game. Draw the first 2 cards
* 2nd step: what the player would like to do? if the player hit, he draws a new card.
* 3rd step: if the dealer is under 17, he continues to draw card otherwise we compare the score
* 4th step: comparison of the players scores

Other functions to:
* draw the cards
* manage score
* display results

## Organization
We worked on jupiter notebook.
