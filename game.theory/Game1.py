import random

# Constants
num_rounds = 10
min_bid = 10
max_bid = 100
num_bidders = 3

# Function to calculate the root mean square of a list of values
def calculate_rms(values):
    return (sum(x ** 2 for x in values) / len(values)) ** 0.5

# Initialising lists to store bids and winners
bids = [[] for _ in range(num_rounds)]
winners = []

# Simulating the auction game for each round
for round_num in range(num_rounds):
    print(f"Round {round_num + 1}:")
    
    # Generating random bids for each bidder
    round_bids = [random.randint(min_bid, max_bid) for _ in range(num_bidders)]
    bids[round_num] = round_bids
    
    # Calculating the RMS of all bids in this round
    rms = calculate_rms(round_bids)
    print(f"RMS of all bids: {rms}")
    
    # Finding the winner based on the bidder with the closest average to RMS
    winner_index = min(range(num_bidders), key=lambda i: abs((round_bids[i] + round_bids[(i + 1) % num_bidders]) / 2 - rms))
    winner = chr(ord('A') + winner_index)
    winners.append(winner)
    
    print(f"Winner of this round: Player {winner}")
    print("-" * 30)

# Calculating the payoff for the winner
winner_payoff = sum(max(bids[i]) for i in range(num_rounds)) / num_rounds

# Printing the winner and payoff
print(f"Player {winners.count('A')} wins {winners.count('A')} rounds.")
print(f"Player {winners.count('B')} wins {winners.count('B')} rounds.")
print(f"Player {winners.count('C')} wins {winners.count('C')} rounds.")
print(f"The winner is Player {max(winners, key=winners.count)}.")

print(f"The winner will pay a total of ${winner_payoff:.2f}.")
