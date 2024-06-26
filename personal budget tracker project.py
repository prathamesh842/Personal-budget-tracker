#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
import pandas as pd

def get_user_expenses():
    expenses = []
    while True:
        date = input("Enter the date(YYYY-MM-DD) or q to quit: ")
        if date.lower()=="q":
            break
        category = input("Enter the category: ")
        amount = int(input("Enter the amount: "))
        expenses.append({"Date":date,"Category":category,"Amount":amount})
    return expenses
def expenses_to_csv(expenses, filename='expenses.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Date", "Category", "Amount"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to {filename}")
def summary_expense(filename = 'expenses.csv'):
    df = pd.read_csv(filename)
    summary = df.groupby("Category")["Amount"].sum()
    print("summary of expenses by category")
    print(summary)
    
def main():
    expenses = get_user_expenses()
    expenses_to_csv(expenses)
    summary_expense()

if __name__ == "__main__":
    main()
    


# In[ ]:




