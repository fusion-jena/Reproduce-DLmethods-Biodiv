import pandas as pd

df = pd.read_csv("Data_after_inter_annotator_agreement.csv")


resource_columns = [
    "Dataset",
    "Source Code",
    "Open source frameworks or environment",
    "Model architecture",
]
methodological_columns = [
    "Software and Hardware Specification",
    "Methods",
    "Hyper-parameters",
]
statistical_columns = ["Averaging result", "Evaluation metrics"]

df["Resources Information"] = df[resource_columns].apply(
    lambda row: "n" if "n" in row.values else "y", axis=1
)
df["Methodological Information"] = df[methodological_columns].apply(
    lambda row: "n" if "n" in row.values else "y", axis=1
)
df["Statistical Information"] = df[statistical_columns].apply(
    lambda row: "n" if "n" in row.values else "y", axis=1
)
df["Randomness Information"] = df["Randomness"]

df["Level 1"] = df["Resources Information"]
df["Level 2"] = df.apply(
    lambda row: "y"
    if row["Resources Information"] == "y" and row["Methodological Information"] == "y"
    else "n",
    axis=1,
)
df["Level 3"] = df.apply(
    lambda row: "y"
    if row["Resources Information"] == "y"
    and row["Methodological Information"] == "y"
    and row["Statistical Information"] == "y"
    else "n",
    axis=1,
)
df["Level 4"] = df.apply(
    lambda row: "y"
    if row["Resources Information"] == "y"
    and row["Methodological Information"] == "y"
    and row["Randomness Information"] == "y"
    else "n",
    axis=1,
)
df["Level 5"] = df.apply(
    lambda row: "y"
    if row["Resources Information"] == "y"
    and row["Methodological Information"] == "y"
    and row["Randomness Information"] == "y"
    and row["Statistical Information"] == "y"
    else "n",
    axis=1,
)

df.to_csv("Final_data.csv", index=False)
