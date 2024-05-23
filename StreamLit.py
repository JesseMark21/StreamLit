import streamlit as st
import math

types = [25, 10, 5, 1]

total_sales = 5.43
cash_in = 6

# finds the minimum # of types needed to
# make change for some number of cents
def get_coins(cash, sale):
    numCoins = { "Quarters": 0, "Nickels": 0, "Dimes": 0, "Cents": 0 }
    totalCoins = 0
    change = cash - sale
    
    
    cash *= 100
    sale *= 100

    cents = cash - sale

    while(cents > 0):

        for x in range(0,3):
            num = math.floor(cents/types[x])
            cents -= num * types[x]

            numCoins[0] = num
            totalCoins += num


    return totalCoins, numCoins, change


st.write(get_coins(cash_in, total_sales))