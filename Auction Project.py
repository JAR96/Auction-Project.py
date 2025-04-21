import time

print("🏁 Welcome to the Auction!")
print("Press ENTER to start bidding...")
input()

highest_bid = 0
highest_bidder = ""

bidders = ["Alice", "Bob", "Charlie"]
bids = {}

for bidder in bidders:
    print(f"{bidder}'s turn to bid.")
    try:
        bid = int(input(f"Enter bid amount for {bidder}: $"))
        bids[bidder] = bid
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder
    except ValueError:
        print("Invalid bid. Skipping...")

print("\n🏆 Auction Ended!")
time.sleep(1)
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")
