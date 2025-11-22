import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Synthetic realistic customer spending data
np.random.seed(42)

data = pd.DataFrame({
    "Customer_Segment": (
        ["Budget"] * 50 +
        ["Regular"] * 50 +
        ["Premium"] * 50 +
        ["Luxury"] * 50
    ),
    "Purchase_Amount": (
        np.random.normal(50, 15, 50).tolist() +
        np.random.normal(120, 30, 50).tolist() +
        np.random.normal(250, 60, 50).tolist() +
        np.random.normal(500, 120, 50).tolist()
    )
})

# Professional Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Exactly 512x512 pixels → figsize + dpi trick
plt.figure(figsize=(8, 8), dpi=64)  # 8 inches × 64 dpi = 512 px

# Boxplot
sns.boxplot(
    data=data,
    x="Customer_Segment",
    y="Purchase_Amount",
    palette="Set2"
)

# Titles & labels
plt.title("Purchase Amount Distribution by Customer Segment", fontsize=14)
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")

# Save EXACT size
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
