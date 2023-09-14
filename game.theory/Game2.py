import random
import math

# Constants
num_rounds = 7
min_bid = 20
max_bid = 100
num_bidders = 3

# Function to calculate the log2 of a number rounded to the nearest integer
def log2_rounded(number):
    return round(math.log2(number))

# Initialising lists to store bids
bids = [[] for _ in range(num_rounds)]

# Simulating the auction game for each round
for round_num in range(num_rounds):
    print(f"Round {round_num + 1}:")
    
    # Generating random bids for each bidder
    round_bids = [random.randint(min_bid, max_bid) for _ in range(num_bidders)]
    bids[round_num] = round_bids
    
    # Finding the winner based on the bidder with the maximum bid
    winner_index = round_bids.index(max(round_bids))
    winner = chr(ord('A') + winner_index)
    
    print(f"Bids: {round_bids}")
    print(f"Winner of this round: Player {winner}")
    print("-" * 30)

# Calculating the highest bid in the first round
highest_bid_first_round = max(bids[0])

# Calculating the round number for which the payoff is determined
payoff_round = log2_rounded(highest_bid_first_round) // 2

# Calculating the lowest bid in the determined payoff round
lowest_bid_payoff_round = min(bids[payoff_round])

# Calculating the payoff
winner_payoff = lowest_bid_payoff_round + 5

# Printing the payoff round and the winner's payoff
print(f"The payoff round is round {payoff_round + 1}.")
print(f"The lowest bid in this round is ${lowest_bid_payoff_round}.")
print(f"The winner will pay a total of ${winner_payoff}.")
