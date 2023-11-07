import pandas as pd
from sklearn.metrics import cohen_kappa_score

df_VK = pd.read_csv("Variable_info_VK_v1.csv")
df_WA = pd.read_csv("Variable_info_WA_v1.csv")


columns = ["V1", "V2", "V3", "V4", "V5", "V6", "V7", "R", "S1", "S2"]


iaa_scores = {}

# Iterate through the columns
for column in columns_to_measure_iaa:
    # Extract the binary values for each annotator
    annotator1_values = df_VK[column]
    annotator2_values = df_WA[column]

    # Calculate Cohen's Kappa for the two annotators
    kappa_score = cohen_kappa_score(annotator1_values, annotator2_values)

    # Store the IAA score in the dictionary
    iaa_scores[column] = kappa_score

# Print the IAA scores
for column, iaa_score in iaa_scores.items():
    print(f"IAA for {column}: {iaa_score:.2f}")
