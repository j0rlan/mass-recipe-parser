#!/usr/bin/env python3

# for parsing an xlsx document of multiple recipes and creating a csv file containing the shopping list

import pandas as pd
from sys import argv

def main():
   fn = input("input file name: ")
   xls = pd.ExcelFile(fn)

   print(xls.sheet_names)



if __name__ == '__main__':
   main()
