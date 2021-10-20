#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import time


start = time.time()


def get_actions_list(data_doc):
    """Load CSV and format data.

    Args:
        data_doc ([.CSV]): [.csv file with invest data]

    Returns:
        [list]: [name, price, profit]
    """
    with open(data_doc) as csv_file:
        csv_list = list(csv.reader(csv_file))
        actions_list = []
        for row in csv_list[1:]:
            if float(row[1]) > 0:
                # Calculate profits
                round_profit = round(float(row[1]) * float(row[2]))
                # Create a list of all actions if data is usable
                actions_list.append([row[0], round(float(row[1])), round_profit])
    return actions_list


def knapSack(money, list_actions):
    new_line = "\n"
    max_money = money
    actions_number = len(list_actions)
    K = [[0 for x in range(max_money + 1)] for y in range(actions_number + 1)]

    # Build table K[][] in bottom up manner
    for i in range(actions_number + 1):
        for w in range(max_money + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif list_actions[i - 1][1] <= w:
                K[i][w] = max(
                    list_actions[i - 1][2] + K[i - 1][w - list_actions[i - 1][1]],
                    K[i - 1][w],
                )
            else:
                K[i][w] = K[i - 1][w]

    profit = K[actions_number][max_money]
    final_list_actions = []
    for i in range(actions_number, 0, -1):
        if profit <= 0:
            break
        if profit == K[i - 1][max_money]:
            continue
        else:
            # This item is included.
            final_list_actions.append(list_actions[i - 1])
            # Since this weight is included
            # its value is deducted
            profit -= list_actions[i - 1][2]
            max_money -= list_actions[i - 1][1]

    new_line = "\n"
    final_combination = (
        f"COMBINATION : {[x[0] for x in final_list_actions]}"
        f"{new_line}PRICE : {sum([x[1] for x in final_list_actions])}€"
        f"{new_line}PROFITS : {sum([x[2] for x in final_list_actions]) / 100}€"
    )

    return final_combination


print(knapSack(500, get_actions_list("dataset2_Python+P7.csv")))
end = time.time()
print(end - start)
