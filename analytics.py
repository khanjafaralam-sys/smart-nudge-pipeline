import pandas as pd

print("\n--- Markytics Nudge Campaign Analytics ---")

# 1. Load the spreadsheet data into a Pandas "DataFrame"
df = pd.read_csv("nudge_history.csv")

# 2. Perform the Analytics (The Math)
total_nudges = len(df)

# Filter the data to only count people who paid ("Yes")
successful_payments = len(df[df["payment_received"] == "Yes"])

# Calculate the conversion rate percentage
conversion_rate = (successful_payments / total_nudges) * 100

# 3. Print the Actionable Insights
print(f"Total Nudges Sent: {total_nudges}")
print(f"Successful Payments Collected: {successful_payments}")
print(f"Campaign Success Rate: {conversion_rate:.1f}%")

print("\nBusiness Insight:")
if conversion_rate > 50:
    print("Insight: The current nudge copy is highly effective. Continue current campaign.")
else:
    print("Insight: Success rate is low. Recommend A/B testing a different WhatsApp message.")
print("------------------------------------------\n")