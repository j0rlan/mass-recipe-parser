#!/usr/bin/env python3

# for parsing an xlsx document of multiple recipes and creating a csv file containing the shopping list

import pandas as pd
import csv

def main():
   #fn = input("input file name: ")
   fn = "food.xlsx"
   xls = pd.ExcelFile(fn)
   shoppingList = {}

   for sheet in xls.sheet_names:
      df = xls.parse(sheet, skiprows=6)
      rows = df.iterrows()
      while True:
         try:
            ser = next(rows)[1]
            ser[0] = ser[0].lower()
            ser[4] = ser[4].lower()
            ser[3] = ser[3].lower()
         except StopIteration:
            break
         except AttributeError:
            pass
         except IndexError:
            continue
         try:
            if type(ser[0]) != str:
               continue
            if ser[0] not in shoppingList:
               shoppingList[ser[0]] = {ser[4]: ser[3]}
            elif ser[4] not in shoppingList[ser[0]]:
               shoppingList[ser[0]][ser[4]] = ser[3]
            else:
               shoppingList[ser[0]][ser[4]] += ser[3]
         except:
            continue

   with open('list.txt', 'w+') as f:
      for ingredient in shoppingList:
         f.write(f'{ingredient}: {shoppingList[ingredient]}\n')


if __name__ == '__main__':
   main()
