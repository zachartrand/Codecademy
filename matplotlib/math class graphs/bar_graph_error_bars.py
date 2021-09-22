from matplotlib import pyplot as plt

past_years_averages = [82, 84, 83, 86, 74, 84, 90]
x_values = [i for i, _ in enumerate(past_years_averages)]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
plt.figure(figsize=(10, 8))
ax = plt.subplot()
plt.axis([-0.5, 6.5, 70, 95])
plt.bar(x_values, past_years_averages, yerr=error, capsize=5)
ax.set_xticks(x_values)
ax.set_xticklabels(years)
plt.xlabel('Year')
plt.ylabel('Test average')
plt.title('Final Exam Averages')
plt.savefig('my_bar_chart.png')

plt.show()
