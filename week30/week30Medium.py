# Date: 8/23/2023
# Author: Shantel Williams

# Medium: Create a function that takes three values:
# h hours
# m minutes
# s seconds
# Return the value that’s the longest duration.

# Examples:
# longest_time(1, 59, 3598) ➞ 1
# longest_time(2, 300, 15000) ➞ 300
# longest_time(15, 955, 59400) ➞ 59400

# Notes:
# No two durations will be the same.
def longest_time(h,m,s):
    longest_duration = 0

    second_dict ={"hour": 3600, "minute": 60, "second":1} # convert all time types to seconds
    total_hour_second = h * second_dict.get("hour",0)
    total_minute_second = m * second_dict.get("minute",0)
    total_second = s

    time_list = [total_hour_second,total_minute_second,total_second]  # compare each time to find the greatest number
    max_time = max(time_list)

    for i in range(len(time_list)): # fincing the max time index
        if time_list[i] == max_time:
            max_index = i
                   
    if max_index == 0: # grabbing the right parameter based on ilist index
        longest_duration = h
    if max_index == 1:
        longest_duration = m
    if max_index == 2:
        longest_duration = s

    return longest_duration

def main():
    test =longest_time(1, 59, 3598)
    test2 = longest_time(2, 300, 15000)
    test3 = longest_time(15, 955, 59400)
    print(test)
    print(test2)
    print(test3)

main()
