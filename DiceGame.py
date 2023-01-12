# --------------------------------------------------------------------------------- 
# ----------------------------- Description / Rules ------------------------------- 

# This programme is just for Dice Game.

# => Here I use two class instance for storing point. One is human and another one is for computer. So, for this programme, our total player is two.
# => Initially both of this two players point is equal, which is 10.

# ● The point of the player who wins a round will be decremented by 1.
# ● The point of the player who loses a round will be incremented by 1.
# -> How do we determine in each round which player is winning or losing?
# Ans: If the dice number of Human > the dice number of computer, then the human wins in each round. Otherwise, the computer wins in each round.
# ---> One thing, if the dice number of both players is equal, then no point will be decremented or incremented. So at that time, there is a tie and no winners for that round.

# ● The point will determine who wins the game. So, the player whose point reaches the value 0 first, wins the game.

# => The whole programme works using OOP.
# => Language of this programme is PYTHON.

# ----------------------------------------------------------------------------------
# ----------------------------- Let's Enjoy the Game -------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------



##############################################################################
################################# Class ######################################
##############################################################################

import random

class DiceGame:

  human = 10
  computer = 10

  def __init__(self):
    print("="*58)
    print("Welcome to the Dice Game")
    print("---")
    print("Initially, the score of both YOU and COMPUTER is equal.")
    print("Your INITIAL score: 10")
    print("Computer INITIAL score: 10")
    print("="*58)
    self.roll()
  
  def roll(self):
    print()
    x = int(input("Human: "))
    if x > 6:
      print("=> Put a VALID(1-6) dice number.")
      return
    y = random.randint(1,6)
    print("Computer:", y)
    if x == y:
      pass
    elif x > y:
      DiceGame.computer +=1
      DiceGame.human -=1
    else:
      DiceGame.computer -=1
      DiceGame.human +=1
    self.compare()
    
  def compare(self):
    print()
    print("Current Point of HUMAN:",DiceGame.human)
    print("Current Point of COMPUTER:",DiceGame.computer)
    if DiceGame.computer == 0:
      print()
      print()
      print("="*34)
      print("Computer won the game.")
      print("-")
      print("Don't worry. Carry on.")
      print("Insha'Allah, you will win the next match.")
      print("="*34)
      return 
    elif DiceGame.human == 0:
      print()
      print()
      print("="*34)
      print("Congratulations! You wins the game.")
      print("="*34)
      return
    print("="*30)
    self.roll()


##############################################################################
################################# Driver code ################################
##############################################################################


d=DiceGame()


# OUTPUT is like this, 

# ==========================================================
# Welcome to the Dice Game
# ---
# Initially, the score of both YOU and COMPUTER is equal.
# Your INITIAL score: 10
# Computer INITIAL score: 10
# ==========================================================

# Human: 5
# Computer: 2

# Current Point of HUMAN: 9
# Current Point of COMPUTER: 11
# ==============================

# Human: 6
# Computer: 6

# Current Point of HUMAN: 9
# Current Point of COMPUTER: 11
# ==============================

# Human: 6
# Computer: 3

# Current Point of HUMAN: 8
# Current Point of COMPUTER: 12
# ==============================

# Human: 6
# Computer: 4

# Current Point of HUMAN: 7
# Current Point of COMPUTER: 13
# ==============================

# Human: 6
# Computer: 4

# Current Point of HUMAN: 6
# Current Point of COMPUTER: 14
# ==============================

# Human: 6
# Computer: 2

# Current Point of HUMAN: 5
# Current Point of COMPUTER: 15
# ==============================

# Human: 6
# Computer: 1

# Current Point of HUMAN: 4
# Current Point of COMPUTER: 16
# ==============================

# Human: 6
# Computer: 4

# Current Point of HUMAN: 3
# Current Point of COMPUTER: 17
# ==============================

# Human: 6
# Computer: 5

# Current Point of HUMAN: 2
# Current Point of COMPUTER: 18
# ==============================

# Human: 6
# Computer: 3

# Current Point of HUMAN: 1
# Current Point of COMPUTER: 19
# ==============================

# Human: 6
# Computer: 1

# Current Point of HUMAN: 0
# Current Point of COMPUTER: 20


# ==================================
# Congratulations! You won the game.
# ==================================


