def read_file(filename):
    infile = open(filename,'r')
    infile.readline()
    dates = []; prices = []
    for line in infile:
        columns = line.split(',')
        date = columns[0]
        date = date[:-3]
        price = columns[-1]
        dates.append(date)
        prices.append(float(price))
    infile.close()
    dates.reverse()
    prices.reverse()
    return dates, prices

dates = {}; prices={}
d, p = read_file('IBM.csv')
dates['IBM'] = d; prices['IBM'] = p
d, p = read_file('GOOG.csv')
dates['GOOG'] = d; prices['GOOG'] = p

# Normalizing prices
norm_price = prices['IBM'][0]
prices['IBM'] = [p/norm_price for p in prices['IBM']]




