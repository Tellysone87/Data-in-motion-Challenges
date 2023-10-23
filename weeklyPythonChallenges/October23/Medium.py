# 10/25/2023
# Shantel Williams

# Problem Statement:
# Given a list of prices, create a function to categorize them into price bands: Low, Medium, and High. 
# Prices up to 50 are Low, between 51 and 200 are Medium, and above 200 are High.

def banding(list):
    cate_dict = {}

    # for loop
    for num in list:
        # check each number to category
        if num < 50:
            if "low" not in cate_dict:
                cate_dict["low"] = []
                cate_dict["low"].append(num)
            else:
                cate_dict["low"].append(num)
        if num > 51 and num < 200:
            if "Medium" not in cate_dict:
                cate_dict["Medium"] = []
                cate_dict["Medium"].append(num)
            else:
                cate_dict["Medium"].append(num)
        if num > 200:
            if "high" not in cate_dict:
                cate_dict["high"] = []
                cate_dict["high"].append(num)
            else:
                cate_dict["high"].append(num)
    return cate_dict

def main():
    prices = [10, 75, 30, 250, 150, 300]
    print(banding(prices))

main()