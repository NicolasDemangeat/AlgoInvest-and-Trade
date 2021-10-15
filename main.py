#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import itertools


def get_actions_list(data_doc):
    """
    Description: Open CSV and organise data.
    :param data_doc: .csv.
    :return elements_once: list of data checked [action_name, price, profits].
    """
    with open(data_doc) as csv_file:
        csv_list = list(csv.reader(csv_file))
        actions_list = []
        for row in csv_list[1:]:
            if float(row[1]) > 0:
                # Calculate profits
                round_profit = round((float(row[1])*float(row[2]))/100, 2)
                # Create a list of all actions if data is usable
                actions_list.append(
                    [row[0], float(row[1]), int(round_profit)])
    return actions_list

