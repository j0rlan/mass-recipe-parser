#!/usr/bin/env python3

# for parsing an xlsx document of multiple recipes and creating a csv file containing the shopping list

import pandas as pd

def main():
   #fn = input("input file name: ")
   fn = "food.xlsx"
   xls = pd.ExcelFile(fn)
   shoppingList = {}

   print("processing sheets:")
   for sheet in xls.sheet_names:
      #print(sheet)
      df = xls.parse(sheet, skiprows=6)
      rows = df.iterrows()
      while True:
         try:
            ser = next(rows)[1]
         except StopIteration:
            break
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

   for line in shoppingList:
      print(line, shoppingList[line])



if __name__ == '__main__':
   main()
