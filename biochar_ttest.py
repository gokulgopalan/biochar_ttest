import numpy as np
from scipy.stats import f_oneway
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('biochar.xlsx')

grouped = df.groupby('Assay')
scaled = ['Transfer 0', 'Transfer 1', 'Transfer 2', 'Transfer 3']

colors = ['blue', 'lime', 'red','blue', 'lime', 'red']
variables = ['BEB 450', 'BEB 550', 'BEB 700']
variables_s = ['BEB 450_S', 'BEB 550_S', 'BEB 700_S']
variables_t = ['BEB 450', 'BEB 550', 'BEB 700','BEB 450_S', 'BEB 550_S', 'BEB 700_S']

for category, group_df in grouped:
    print(f"Assay: {category}")
    data =  [group_df[var] for var in variables]

    statistic, p_value = f_oneway(*data)

    print("ANOVA Results:")
    print("F-statistic:", statistic)
    print("p-value:", p_value)

    # Interpret the results based on the p-value
    alpha = 0.05  # significance level
    if p_value < alpha:
        print("Reject null hypothesis: There is a significant difference among at least one pair of groups.")
    else:
        print("Fail to reject null hypothesis: There is no significant difference among the groups.")
    print("")

    plt.figure(figsize=(10, 6))
    box = plt.boxplot(data, labels=variables, patch_artist=True)

    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
    plt.ylabel('Degradation Half-Life (hours)')
    plt.title(f'Biologically Enhanced Biochar for Batch Assay {category}',fontsize=14)

    # Display the p-value at the bottom of the plot
    plt.text(0.5, -0.15, f'ANOVA p-value: {p_value:.4f}', fontsize=14, ha='center', transform=plt.gca().transAxes)
    filename = f'images/box_{category}.tiff'
    plt.savefig(filename)
    plt.show()

    if category in scaled:
        print(f"Assay for Scaled up: {category}")
        data =  [group_df[var] for var in variables_s]

        statistic, p_value = f_oneway(*data)

        print("ANOVA Results:")
        print("F-statistic:", statistic)
        print("p-value:", p_value)

        # Interpret the results based on the p-value
        alpha = 0.05  # significance level
        if p_value < alpha:
            print("Reject null hypothesis: There is a significant difference among at least one pair of groups.")
        else:
            print("Fail to reject null hypothesis: There is no significant difference among the groups.")
        print("")

        plt.figure(figsize=(10, 6))
        box = plt.boxplot(data, labels=variables_s, patch_artist=True)

        for patch, color in zip(box['boxes'], colors):
            patch.set_facecolor(color)
        plt.ylabel('Degradation Half-Life (hours)')
        plt.title(f'Biologically Enhanced Biochar for Scaled-up Assay {category}',fontsize=14)

        # Display the p-value at the bottom of the plot
        plt.text(0.5, -0.15, f'ANOVA p-value: {p_value:.4f}', fontsize=14, ha='center', transform=plt.gca().transAxes)
        filename = f'images/box_scaled_{category}.tiff'
        plt.savefig(filename)
        plt.show()

        ##Comparison across 6 groups

        print(f"Assay for all groups: {category}")
        data =  [group_df[var] for var in variables_t]

        statistic, p_value = f_oneway(*data)

        print("ANOVA Results:")
        print("F-statistic:", statistic)
        print("p-value:", p_value)

        # Interpret the results based on the p-value
        alpha = 0.05  # significance level
        if p_value < alpha:
            print("Reject null hypothesis: There is a significant difference among at least one pair of groups.")
        else:
            print("Fail to reject null hypothesis: There is no significant difference among the groups.")
        print("")

        plt.figure(figsize=(10, 6))
        box = plt.boxplot(data, labels=variables_t, patch_artist=True)

        for patch, color in zip(box['boxes'], colors):
            patch.set_facecolor(color)
        plt.ylabel('Degradation Half-Life (hours)')
        plt.title(f'Biologically Enhanced Biochar for All Assay {category}',fontsize=14)

        # Display the p-value at the bottom of the plot
        plt.text(0.5, -0.15, f'ANOVA p-value: {p_value:.4f}', fontsize=14, ha='center', transform=plt.gca().transAxes)
        filename = f'images/box_total_{category}.tiff'
        plt.savefig(filename)
        plt.show()



    


    







