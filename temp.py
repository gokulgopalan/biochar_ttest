import numpy as np
from scipy.stats import f_oneway
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

# Data for three groups
group1 = np.array([116.04,119.90,114.07])
group2 = np.array([90.32,79.89,110.08])
group3 = np.array([101.77,108.99,150.30])

# Calculate means, standard deviations, and number of observations
mean1 = np.mean(group1)
mean2 = np.mean(group2)
mean3 = np.mean(group3)

std1 = np.std(group1, ddof=1)  # Using Bessel's correction
std2 = np.std(group2, ddof=1)
std3 = np.std(group3, ddof=1)

n1 = len(group1)
n2 = len(group2)
n3 = len(group3)

# Perform ANOVA test
f_statistic, p_value = f_oneway(group1, group2, group3)

print("ANOVA Results:")
print("F-statistic:", f_statistic)
print("p-value:", p_value)

# Decide whether to reject the null hypothesis based on the p-value
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: Means are not equal across groups.")
else:
    print("Fail to reject the null hypothesis: Means are equal across groups.")


data = [group1, group2, group3]

# Create a box plot
plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3'])
plt.title('Box Plot of Three Variables')
plt.ylabel('Value')
plt.text(0.5, -0.15, f'ANOVA p-value: {p_value:.4f}', ha='center', transform=plt.gca().transAxes)
plt.show()

