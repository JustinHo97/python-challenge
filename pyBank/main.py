# %%
import pandas as pd
#import data into dataframe
budget_data_df = pd.read_csv("Resources/budget_data.csv")
#print(budget_data_df)

# %%
#total months in dataset
total_months = len(budget_data_df)
#print(total_months)

# %%
#net_total amount
total_amount = budget_data_df["Profit/Losses"].sum()
#print(total_amount)

# %%
#average changes in Profit/Losses, retrieve index of greatest loss & profit
profit_change = budget_data_df
profit_change["Change in Profit"] = budget_data_df["Profit/Losses"].diff()
#print(profit_change)
average_change = profit_change["Change in Profit"].mean()
lowest_profit = profit_change["Change in Profit"].idxmin()
greatest_profit = profit_change["Change in Profit"].idxmax()
#print(profit_change[["Date", "Change in Profit"]].iloc[greatest_profit])

# %%
#output message

message = f''' Financial Analysis
------------------------------
Total Monts: {total_months}
Total: ${total_amount}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {profit_change["Date"].iloc[greatest_profit]} (${profit_change["Change in Profit"].iloc[greatest_profit]})
Greatest Decrease in Profits: {profit_change["Date"].iloc[lowest_profit]} (${profit_change["Change in Profit"].iloc[lowest_profit]})'''
print(message)

#create analysis file
with open("Analysis/Analysis.txt", "w") as f:
    f.write(message)