import re
import time

def mock_search_emails():
    print("[Mermail MCP] Searching inbox for 'Invoice'...")
    time.sleep(1.5)
    return [
        {
            "id": "msg_10924",
            "subject": "Invoice for API Services",
            "body": "Hello,\n\nPlease pay the outstanding invoice of 150 USDC for this month's API usage.\nMy Solana wallet address is: 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJVg6nd\n\nThanks!"
        }
    ]

def parse_invoice(email_body):
    print("[Agent] Analyzing email content using LLM logic...")
    time.sleep(2)
    # Simple regex to simulate what the LLM extracts
    amount_match = re.search(r'(\d+)\s*USDC', email_body)
    wallet_match = re.search(r'([1-9A-HJ-NP-Za-km-z]{32,44})', email_body)
    
    return {
        "amount": amount_match.group(1) if amount_match else None,
        "wallet": wallet_match.group(1) if wallet_match else None
    }

def execute_payment(amount, wallet):
    print(f"\n[Agent] PROMPT: Would you like to pay {amount} USDC to {wallet}? (Y/n)")
    # We simulate user pressing 'Y'
    print("User input: Y")
    time.sleep(1)
    print("[Mermail PayBox MCP] Executing Solana transaction...")
    time.sleep(2.5)
    print("[Mermail PayBox MCP] ✅ Transaction Successful! Signature: 4kKxg...9jP2")

def main():
    print("=== Mermail Invoice Payer Skill Demo ===\n")
    emails = mock_search_emails()
    
    for email in emails:
        print(f"[Agent] Found email: '{email['subject']}'")
        extracted = parse_invoice(email['body'])
        
        if extracted['amount'] and extracted['wallet']:
            execute_payment(extracted['amount'], extracted['wallet'])
            print("[Agent] Replying to email with transaction signature...")
            time.sleep(1.5)
            print("[Mermail MCP] Email sent successfully.")

if __name__ == "__main__":
    main()
