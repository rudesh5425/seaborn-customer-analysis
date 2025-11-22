import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image, ImageOps

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

# Step 1 — Create figure
plt.figure(figsize=(8, 8), dpi=64)

# Step 2 — Boxplot
sns.boxplot(
    data=data,
    x="Customer_Segment",
    y="Purchase_Amount",
    palette="Set2"
)

plt.title("Purchase Amount Distribution by Customer Segment", fontsize=14)
plt.xlabel("Customer Segment")
plt.ylabel("Purchase Amount ($)")

# Step 3 — Save image (required bbox_inches='tight')
plt.savefig("chart_temp.png", dpi=64, bbox_inches='tight')
plt.close()

# Step 4 — FORCE final image to EXACT 512×512 using padding
img = Image.open("chart_temp.png")
final_img = ImageOps.pad(img, (512, 512), color="white")
final_img.save("chart.png")
