types = [1,5,10,25]
d = {} # stores tuples of the form (# of types, [coin list])

total_sales = 5.43
cash_in = 6


# finds the minimum # of types needed to
# make change for some number of cents
def get_coins(cash, sale):
    cash
    if cents in d.keys():
        return d[cents]
    elif cents > 0:
        choices = [(m(cents - x)[0] + 1, m(cents - x)[1] + [x]) for x in types if cents >= x]

        # given a list of tuples, python's min function
        # uses the first element of each tuple for comparison
        d[cents] = min(choices)
        return d[cents]
    else:
        d[0] = (0, [])
        return d[0]

print (get_coins(cash_in, total_sales))
