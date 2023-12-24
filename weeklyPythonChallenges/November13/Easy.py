# Shantel Williams
# 12/26/2023

# Problem Statement: Given a list of monthly sales figures for a year, calculate the month-to-month sales growth in percentage.

# Expected Task: Create a function that calculates the sales growth percentage for each month compared to the previous month 
# and returns a list of these percentages.

# monthly_sales = [1200, 1150, 1300, 1400, 1350, 1500, 1550, 1600, 1650, 1700, 1750, 1800]
# increae formulas = new value - original value , (increase / original value) x 100
# decrease formula =  original value - new value, (decrease / original value) x 100
def sales_growth(sale_list):
    stop = len(sale_list) - 2
    i = 0
    difference = []

    while i != stop:
        if sale_list[i+ 1] > sale_list[i]:
            increase = sale_list[i+ 1] - sale_list[i]
            percent_increase = (increase/ sale_list[i]) * 100
            difference.append(f"{round(percent_increase)}%")
        else:
            decrease =  sale_list[i] - sale_list[i+ 1]
            percent_decrease = (decrease/ sale_list[i]) * 100
            difference.append(f"{round(percent_decrease)}%")
        i +=1

    return difference

def main():
    monthly_sales = [1200, 1150, 1300, 1400, 1350, 1500, 1550, 1600, 1650, 1700, 1750, 1800]
    print(sales_growth(monthly_sales))

main()