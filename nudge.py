from fastapi import FastAPI
import sqlite3
import requests

app = FastAPI()

# IMPORTANT: Paste your copied Webhook.site URL right here:
WEBHOOK_URL = "https://webhook.site/f6ec1dcf-a313-4b20-8c66-8c1b293a5c89"

@app.get("/trigger-nudges")
def run_nudge_job():
    nudged_customers = []
    
    # 1. Get the data from our SQL Database
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    # We are now selecting the amount too, so we can send it in the message
    cursor.execute("SELECT name, amount_due FROM customers WHERE status = 'overdue'")
    overdue_records = cursor.fetchall()
    conn.close()
    
    # 2. Send the data over the internet!
    for row in overdue_records:
        name = row[0]
        amount = row[1]
        
        # This is the "payload" - the actual data package we are sending to the webhook
        payload = {
            "customer": name,
            "amount_pending": amount,
            "automated_message": f"Hello {name}, your payment of ₹{amount} is overdue."
        }
        
        # Fire the data across the internet using a POST request
        try:
            requests.post(WEBHOOK_URL, json=payload)
            nudged_customers.append(name)
        except Exception as e:
            print(f"Error sending data for {name}: {e}")
            
    return {
        "status": "success",
        "integration": "Live Webhook API",
        "message": f"Live nudges fired across the internet for {len(nudged_customers)} customers.",
        "customers_alerted": nudged_customers
    }