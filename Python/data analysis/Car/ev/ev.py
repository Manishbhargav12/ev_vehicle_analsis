import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("ev.csv")
df=data.copy()
# dominting region in 2023 for ev selling
top_region=df["Region"].value_counts()
dt=df["Date"].value_counts()
print(dt)