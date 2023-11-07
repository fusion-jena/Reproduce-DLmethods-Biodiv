import pandas as pd


df_VK = pd.read_csv("Variable_info_VK_v1.csv")
df_WA = pd.read_csv("Variable_info_WA_v1.csv")


columns = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "R", "S1", "S2"]


diff_list = []

# Iterate through the columns
for column in columns:
    vk_values = df_VK[column]
    wa_values = df_WA[column]
    differences = df_VK['no'][(vk_values != wa_values)]
    diff_list.extend(differences)

    print('Changes in', column, 'are', differences.tolist())

# Calculate the total number of differences
total_diff_count = len(diff_list)

# calculate unique differences:
unique_diff_list = list(set(diff_list))
unique_diff_count = len(unique_diff_list)

print('Total differences:', total_diff_count)
print('Unique differences:', unique_diff_count)
