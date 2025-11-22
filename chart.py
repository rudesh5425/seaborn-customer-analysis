import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ------------------------------
#  Synthetic data generation
# ------------------------------

np.random.seed(42)

segments = ["Budget", "Regular", "Premium", "Luxury"]

data = {
    "Customer_Segment": np.repeat(segments, 200),
    "Purchase_Amount": np.concatenate([
        np.random.normal(50, 10, 200),    # Budget customers
        np.random.normal(120, 20, 200),   # Regular customers
        np.random.normal(250, 40, 200),   # Premium
        np.random.normal(500, 80, 200)    # Luxury
    ])
}

df = pd.DataFrame(data)

# ------------------------------
#  Styling
# ------------------------------

sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 8in × 8in → 512×512 px at dpi=64

# ------------------------------
#  Boxplot
# ------------------------------

sns.boxplot(
    data=df,
    x="Customer_Segment",
    y="Purchase_Amount",
    palette="Set2"
)

plt.title("Purchase Amount Distribution by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")

# ------------------------------
#  Save Output (exact 512×512 px)
# ------------------------------

plt.savefig("chart.png", dpi=64, bbox_inches="tight")
