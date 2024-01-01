# You are a financial analyst working for a retail company. Your task is to evaluate the financial performance of the company for the last fiscal year. You have the total revenue and net profit figures available. To assess how well the company is converting its revenue into profit, you decide to calculate the Net Profit Margin. This metric will provide insights into the percentage of revenue that remains as profit after all expenses have been deducted.

# user input
total_revenue = float(input("The total revenue: "))
net_profit = float(input("The net profit: "))

# profit percentage
net_profit_margin = (net_profit / total_revenue) * 100

print("Net Profit Margin: {:.2f}%".format(net_profit_margin))
