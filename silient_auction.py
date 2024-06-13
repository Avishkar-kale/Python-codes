import os
print("**************Welcome to the silient auction programm***********")
def find_winner(bidder_details):
    heighest_bid=0
    winner=''
    for bidder in bidder_details:
        bidding_price=bidder_details[bidder]
        if bidding_price>heighest_bid:
            heighest_bid=bidding_price
            winner=bidder

    print(f"winnner is {winner} with bid price of {heighest_bid}")
    print(bidder_details)
bidder_data={}
end_of_bidding=False
while not end_of_bidding:
    name = input('what is you name:?')
    price = int(input('enter your bid price?'))
    bidder_data[name] = price
    more_bidders = input('are their more bidder type "yes" or "no"').lower()
    if more_bidders == 'no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')








