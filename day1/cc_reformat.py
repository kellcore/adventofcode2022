# p1: find the elf carrying the most calories. how many total calories is that elf carrying?
# p2: find the top three elves carrying the most calories. how many calories are those elves carrying in total?

import functools
import operator

def get_input(txt_doc):
    with open(txt_doc) as cc_input:
        data = cc_input.read()
        # remove whitespaces and split at double newlines
        data_split = data.strip().split("\n\n")
        # map over list of strings to turn them into sums
        data_map = map(mapper, data_split)
        return data_map

def mapper(item):
    # num_list = [int(num) for num in item.split("\n")]
    # return functools.reduce(operator.add, num_list)
    return functools.reduce(operator.add, [int(num) for num in item.split("\n")])

def most_calories():
    data = get_input('./input.txt')
    max_cals = max(data)
    return max_cals

def top_three():
    data = get_input('./input.txt')
    data_list = list(data)
    # sort list of sums in descending order
    data_list.sort(reverse=True)
    # sum the slice of first 3 values
    top_three_total = functools.reduce(operator.add, [int(num) for num in data_list[:3]])
    return top_three_total

def main():
    print("Max calories:", most_calories())
    print("Total calories of top 3 elves:", top_three())

main()