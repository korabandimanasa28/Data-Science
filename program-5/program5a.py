import matplotlib.pyplot as plt
months = ["Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [200, 170, 240, 210, 280, 320]
expenses = [130, 120, 150, 140, 180, 200]
fig, ax = plt.subplots(2, 1, figsize=(10, 8))
ax[0].plot(months, sales, marker="o", linewidth=2, label="Sales")
ax[0].set_title("Monthly Sales")
ax[0].set_xlabel("Month")
ax[0].set_ylabel("Sales")
ax[0].set_xticks(range(len(months)))
ax[0].set_xticklabels(months)
ax[0].annotate(
    "Highest Sales",
    xy=(5, 320),
    xytext=(3.5, 340),
    arrowprops=dict(arrowstyle="->")
)
ax[0].legend()
ax[0].grid(True)
ax[1].plot(months, expenses, marker="s", linewidth=2, label="Expenses")
ax[1].set_title("Monthly Expenses")
ax[1].set_xlabel("Month")
ax[1].set_ylabel("Expenses")
ax[1].set_xticks(range(len(months)))
ax[1].set_xticklabels(months)
ax[1].annotate(
    "Highest Expense",
    xy=(5, 200),
    xytext=(3.5, 220),
    arrowprops=dict(arrowstyle="->")
)
ax[1].legend()
ax[1].grid(True)
fig.suptitle("Monthly Sales and Expenses Analysis", fontsize=16)
plt.tight_layout()
plt.savefig("monthly_sales_expenses.png", dpi=300, bbox_inches="tight")
plt.show()