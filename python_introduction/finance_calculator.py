#Personal Finance Calculator

def ProjectedSavings(monthlysavings):('projectedSavings = monthlysavings * 12 + (monthlysavings * 12 * 0.05)')
                                     
monthlyincome = int(input('Enter your monthly income:'))
monthlyExpenses = int(input("Enter your total monthly expenses:"))
monthlysavings = monthlyincome - monthlyExpenses
ProjectedSavings = monthlysavings * 12 + (monthlysavings * 12 * 0.05)

print('Your monthly savings are $',monthlysavings)
print('Projected savings after one year, with interest, is:',ProjectedSavings,)

