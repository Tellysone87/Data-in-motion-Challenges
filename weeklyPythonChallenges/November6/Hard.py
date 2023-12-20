# Shantel Williams
# 12/22/2023

# Hard Challenge: Stock Portfolio Analysis
# Background: Portfolio analysis is key in finance, helping investors understand the distribution of their investments.

# Problem Statement: Given a list of stock holdings in a portfolio with their respective values and sectors, 
# write a function that calculates the total value invested in each sector.
# portfolio = [
#     {'name': 'AAPL', 'sector': 'Technology', 'value': 1500},
#     {'name': 'GOOGL', 'sector': 'Technology', 'value': 1000},
#     {'name': 'MSFT', 'sector': 'Technology', 'value': 1200},
#     {'name': 'AMZN', 'sector': 'Consumer Services', 'value': 1800},
#     {'name': 'WMT', 'sector': 'Consumer Goods', 'value': 500},
#     {'name': 'PG', 'sector': 'Consumer Goods', 'value': 300} ]
def sector_total(stock_list):
    sector_amounts = {}

    for dict in stock_list:
        if dict['sector'] in sector_amounts:
            sector_amounts[dict['sector']] = sector_amounts.get(dict['sector'],0) + dict['value']
        else:
            sector_amounts[dict['sector']] = dict['value']
    return sector_amounts

def main():
    portfolio = [
    {'name': 'AAPL', 'sector': 'Technology', 'value': 1500},
    {'name': 'GOOGL', 'sector': 'Technology', 'value': 1000},
    {'name': 'MSFT', 'sector': 'Technology', 'value': 1200},
    {'name': 'AMZN', 'sector': 'Consumer Services', 'value': 1800},
    {'name': 'WMT', 'sector': 'Consumer Goods', 'value': 500},
    {'name': 'PG', 'sector': 'Consumer Goods', 'value': 300}
]
    print(sector_total(portfolio))
    
main()