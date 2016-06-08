import json
import argparse
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from calc import get0Value, sort_data

def parse_args():
    parser = argparse.ArgumentParser()
    output = parser.add_mutually_exclusive_group()

    parser.add_argument('--menu',
                        nargs=1,
                        choices=['pizzas','soups','drinks'],
                        help='sets a menu item to analise')
    parser.add_argument('--mass',
                        nargs=2,
                        type=float,
                        metavar=('MIN','MAX'),
                        help='cuts out the range from MIN to MAX')
    parser.add_argument('--kcal',
                        nargs=2,
                        type=float,
                        metavar=('MIN','MAX'),
                        help='cuts out the range from MIN to MAX')
    parser.add_argument('--proteins',
                        nargs=2,
                        type=float,
                        metavar=('MIN','MAX'),
                        help='cuts out the range from MIN to MAX')
    parser.add_argument('--carbohydrates',
                        nargs=2,
                        type=float,
                        metavar=('MIN','MAX'),
                        help='cuts out the range from MIN to MAX')
    parser.add_argument('--fats',
                        nargs=2,
                        type=float,
                        metavar=('MIN','MAX'),
                        help='cuts out the range from MIN to MAX')
    parser.add_argument('--price',
                        nargs=2,
                        type=float,
                        metavar=('MIN','MAX'),
                        help='cuts out the range from MIN to MAX')
    parser.add_argument('--sortBy',
                        nargs=1,
                        choices=['name','mass','price','kcal','proteins','carbohydrates','fats','priceToMass','kcalToMass'],
                        help='does sorting by parameter')
    output.add_argument('--table',
                        nargs='+',
                        choices=['name','mass','price','kcal','proteins','carbojudrates','fats'],
                        help='prints out a table of items with the specified attributes')
    output.add_argument('--plot',
                        nargs=1,
                        choices=['price','mass','kcal','proteins','carbohydrates','fats'],
                        help='plots sorted data with the x axis set to')

    return parser.parse_args()

def display_plot(listOfItems, attributeName):
    names = [element['name'] for element in listOfItems]
    y_pos = np.arange(len(names))
    attributeValues = [element[attributeName] for element in listOfItems]
    plt.barh(y_pos, attributeValues, align='center', alpha=0.7, color='green')
    plt.yticks(y_pos, names)
    plt.xlabel(attributeName)
    plt.show()

def display_table(columnNames, sortedData):
    formatedData = [{name:element[name] for name in columnNames}
                    for element in sortedData]

    print(tabulate(formatedData, headers="keys"))

def display_processed_data(options):
    args = vars(options())
    sortedData = sort_data(args)

    if args['plot'] is not None:
        display_plot(sortedData, get0Value(args['plot']))
    if args['table'] is not None:
        display_table(args['table'], sortedData)
