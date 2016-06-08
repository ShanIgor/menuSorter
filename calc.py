import numpy as np
import json

class MenuItem:
    def __init__(self, item):
        self.item = item

    def by_attribute(self, attributeName):
        if attributeName in list(self.item[0].keys()):
            def sorting(listItem):
                return listItem[attributeName]
            return sorting
        if attributeName == 'priceToMass':
            def sorting(listItem):
                return float(listItem['price']) / float(listItem['mass'])
            return sorting
        if attributeName == 'kcalToMass':
            def sorting(listItem):
                return float(listItem['kcal']) / float(listItem['mass'])
            return sorting

    def sort_by(self, attributeName):
        return sorted(self.item, key=self.by_attribute(attributeName))

def filter_by_attribute_value(attributeName, listToSlice, minValue, maxValue):
    return [element for element in listToSlice
            if (float(element[attributeName]) >= float(minValue) and
                float(element[attributeName]) < float(maxValue))]

def get0Value(element):
    return element[0]

def get1Value(element):
    return element[1]

def get_menu(menuJSON):
    with open(menuJSON) as data:
        return json.load(data)

def sort_data(options):
    menu = get_menu('menu.json')
    numAttrs = ['price','mass','kcal','proteins','carbohydrates','fats']

    result = menu[get0Value(options['menu'])]
    menuItem = MenuItem(menu[get0Value(options['menu'])])

    if options['sortBy'] is not None:
        result = menuItem.sort_by(get0Value(options['sortBy']))
    for attribute in numAttrs:
        if options[attribute] is not None:
            result = filter_by_attribute_value(attribute, result,
                                            get0Value(options[attribute]),
                                            get1Value(options[attribute]))
    return result
