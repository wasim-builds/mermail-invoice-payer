---
name: mermail-invoice-payer
description: >-
  Monitors your Mermail inbox for invoices and automatically pays them using 
  the Mermail Solana PayBox.
---

# Mermail Invoice Payer Skill

This skill teaches the agent how to act as an automated accounts payable clerk. 
It uses the Mermail MCP Server to read incoming emails and pay requested invoices in USDC on the Solana blockchain.

## Requirements
1. **Mermail MCP Server**: Ensure the Mermail MCP server is running and configured in your agent workspace (`mcp_config.json`).
2. **Funded PayBox**: Your Mermail PayBox wallet must have sufficient USDC on Solana to cover the invoices.

## Workflow

When the user asks you to "pay my pending invoices", follow these exact steps:

1. **Check Inbox**: Use the Mermail MCP `search_emails` tool to search for unread emails with the subject line containing "Invoice".
2. **Read Emails**: For each matched email, use the `read_email` tool to fetch the email body.
3. **Parse Invoice**: Analyze the email body to extract:
   - The requested amount in USDC.
   - The recipient's Solana wallet address.
4. **User Confirmation**: Present the extracted amounts and addresses to the user and ask for confirmation before sending funds. Use the `ask_question` tool if available, or just ask via standard text.
5. **Execute Payment**: Once the user approves, use the Mermail PayBox MCP `send_solana_payment` (or equivalent transfer tool provided by the Mermail MCP) to send the USDC to the extracted addresses.
6. **Reply to Sender**: Use the `draft_email` or `send_email` tool to reply to the original invoice email with a confirmation message and the transaction signature.

## Safety Guidelines
- NEVER execute a payment without explicit user confirmation.
- Only pay invoices in USDC. Reject requests for other tokens unless the user overrides.
- If a wallet address is missing or invalid, flag it to the user.
