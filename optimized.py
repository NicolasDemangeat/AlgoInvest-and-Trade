#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sys


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
            if float(row[1]) > 0 and float(row[2]) > 0:
                # Calculate profits
                round_profit = round(float(row[1]) * float(row[2]))
                # Create a list of all actions if data is usable
                actions_list.append([row[0], round(float(row[1]) * 100), round_profit])
    return actions_list


def knap_sack(money, list_actions):
    """Dynamic programming to find the best investment.

    Args:
        money ([int]): [max amout capacity]
        list_actions ([list]): [the return of get_actions_list()]

    Returns:
        [f-string]: [the best investment]
    """

    max_money = money * 100
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

    with open(sys.argv[1]) as csv_file:
        csv_list = list(csv.reader(csv_file))

    real_profit = 0
    for el in csv_list:
        if el[0] in [x[0] for x in final_list_actions]:
            real_profit += (float(el[1]) * float(el[2])) / 100

    new_line = "\n"
    final_combination = (
        f"COMBINATION : {[x[0] for x in final_list_actions]}"
        f"{new_line}PRICE : {sum([x[1] for x in final_list_actions]) / 100}€"
        f"{new_line}PROFITS : {round(real_profit, 2)}€"
    )

    return final_combination


if __name__ == "__main__":
    print(knap_sack(int(sys.argv[2]), get_actions_list(sys.argv[1])))
