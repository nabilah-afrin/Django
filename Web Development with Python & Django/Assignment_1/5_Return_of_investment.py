# You are an investor considering putting money into a business project. To make an informed decision, you need to evaluate the potential return on investment. You have the estimated net profit and the total investment cost for the project. By calculating the Return on Investment (ROI), you can assess the percentage return relative to the initial investment.

# user inputs
net_profit = float(input("Net profit: "))
total_investment = float(input("Total investment cost: "))

# the Return on Investment (ROI)
roi = (net_profit / total_investment) * 100

# result
print("The Return on Investment (ROI) is {:.3f}%".format(roi))
