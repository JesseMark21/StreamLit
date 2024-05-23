import streamlit as st
import math

types = [1,5,10,25]
d = {} # stores tuples of the form (# of types, [coin list])

total_sales = 5.43
cash_in = 6


# finds the minimum # of types needed to
# make change for some number of cents
def get_coins(cash, sale):
    cash *= 100
    sale *= 100

    change = cash - sale

    cents = change
    
    numQuarters = math.floor(cents/types[3])

    cents -= numQuarters * types[3]

    if(cents > 0):
        numDimes = math.floor(cents/types[2])
        cents -= numDimes * types[2]
    
    if(cents > 0):
        numNickels = math.floor(cents/types[1])
        cents -= numNickels * types[1]

    if(cents > 0):
        numCents = math.floor(cents/types[0])
        cents -= numCents * types[0]
    
    numCoins = [ numCents, numNickels, numDimes, numQuarters ]

    totalCoins = numCents + numNickels + numDimes + numQuarters

    return totalCoins, numCoins, change


st.write(get_coins(cash_in, total_sales))