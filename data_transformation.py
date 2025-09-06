import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate
import logging
import os

from datetime import datetime


os.makedirs("logs", exist_ok=True)
log_file = f"logs/pipeline_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def log(message):
    """Write logs to both console and log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] {message}"
    print(formatted_message)  # show on screen
    with open(log_file, "a") as f:
        f.write(formatted_message + "\n")

log("Starting pipeline...")



data = pd.read_csv("C:/Users/konda/Downloads/Bank Branches.csv")
log(f"Loaded dataset with {len(data)} rows and {len(data.columns)} columns.")
data

data.describe()
log("Discription of dataset.")

#Standardize

data.columns = [c.strip().lower().replace(" ", "_") for c in data.columns]
log("Standardizing the data.")
data

data = data.drop_duplicates() 
log("Removed duplicate rows.")
data

data.loc[data["nationalized_banks"] < 0, "nationalized_banks"] = None 
data.loc[data["private_banks"] < 0, "private_banks"] = None 
data.loc[data["regional_rural_banks"] < 0, "regional_rural_banks"] = None 
data.loc[data["cooperative_banks"] < 0, "cooperative_banks"] = None 
data.loc[data["atms"] < 0, "atms"] = None 
log("Any district as 0 bank those are replaced with NaN .")
data

data["total_branches"] = (
    data["nationalized_banks"] +
    data["private_banks"] +
    data["regional_rural_banks"] +
    data["cooperative_banks"]
)
log("Added new column: total_branches.")

data["atm_per_branch"] = data["atms"] / (data["total_branches"] )
log("Added new column: atm_per_branches.")
data


data["nationalized_share"] = (data["nationalized_banks"] / (data["total_branches"])) * 100
data["private_share"] = (data["private_banks"] / (data["total_branches"])) * 100
data["rrb_share"] = (data["regional_rural_banks"] / (data["total_branches"])) * 100
data["cooperative_share"] = (data["cooperative_banks"] / (data["total_branches"])) * 100

log("Added new column: nationalized_share.")
log("Added new column: private_share.")
log("Added new column: rrb_share.")
log("Added new column: cooperative_share.")
data

#insights


least_branches = data.sort_values(by="total_branches").head(5)[["districts", "total_branches"]]
log("Generated insights for least branches")
print("Districts with least branches:\n", least_branches, "\n")


low_atm_coverage = data.sort_values(by="atm_per_branch").head(5)[["districts", "atm_per_branch"]]
log("Generated insights for low ATMs at districts.")
print("Districts with lowest ATM coverage:\n", low_atm_coverage, "\n")

high_atm_coverage = data.sort_values(by="atm_per_branch", ascending=False).head(5)[["districts", "atm_per_branch"]]
log("Generated insights for high ATMs at districts.")
print("Districts with highest ATM coverage:\n", high_atm_coverage, "\n")


high_nationalized_share = data.sort_values(by="nationalized_share", ascending=False).head(5)[["districts", "nationalized_share"]]
log("Generated insights for nationalized bank shares")
print("Districts with highest Nationalized Bank share:\n", high_nationalized_share, "\n")

high_private_share = data.sort_values(by="private_share", ascending=False).head(5)[["districts", "private_share"]]
log("Generated insights for private bank shares")
print("Districts with highest Private Bank share:\n", high_private_share, "\n")

high_rrb_share = data.sort_values(by="rrb_share", ascending=False).head(5)[["districts", "rrb_share"]]
log("Generated insights for regional rural bank shares.")
print("Districts with highest Regional Rural Bank (RRB) share:\n", high_rrb_share, "\n")

high_cooperative_share = data.sort_values(by="cooperative_share", ascending=False).head(5)[["districts", "cooperative_share"]]
log("Generated insights for Cooperative Bank share:\n")
print("Districts with highest Cooperative Bank share:\n", high_cooperative_share, "\n")


plt.figure(figsize=(12,6)) 
plt.title("Total Bank Branches by District")
plt.xticks(rotation=60)
plt.ylabel("branches")
plt.bar(data["districts"], data["total_branches"])

plt.savefig("branches_chart.png")
print("Chart saved as branches_chart.png")

