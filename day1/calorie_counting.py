# p1: find the elf carrying the most calories. how many total calories is that elf carrying?
# p2: find the top three elves carrying the most calories. how many calories are those elves carrying in total?

import functools
import operator

def get_input():
    with open('./input.txt') as cc_input:
        data = cc_input.read()
        # data_list = [int(num) for num in data.split("\n\n")]
        data_split = data.strip().split("\n\n")
        # map over list of strings to turn them into sums
        # cleaned_data = [ele.replace("\n", ', ') for ele in data_split]
        # data_list = [eval(i) for i in cleaned_data]
        data_map = map(mapper, data_split)
        # max_cals = max(data_map)
        # print(max(data_map))
        # sort list of sums in descending order, then sum the slice of first 3 values
        data_list = list(data_map)
        data_list.sort(reverse=True)
        top_three = functools.reduce(operator.add, [int(num) for num in data_list[:3]])


    print(top_three)
    

def mapper(item):
    # num_list = [int(num) for num in item.split("\n")]
    # return functools.reduce(operator.add, num_list)
    return functools.reduce(operator.add, [int(num) for num in item.split("\n")])


def main():
    get_input()

main()