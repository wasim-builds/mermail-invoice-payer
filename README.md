# Mermail Invoice Payer Agent Skill

This repository contains a ready-to-use Agent Skill for **Mermail** that turns your AI agent into an automated Accounts Payable clerk using the Solana blockchain!

Built for the **Superteam Earn: Mermail Agent Skill Bounty**.

## What it does
1. Monitors your agent's Mermail inbox for unread emails containing "Invoice".
2. Uses LLM intelligence to parse the USDC amount and the recipient's Solana wallet address from the email body.
3. Asks you (the user) for approval.
4. Executes the payment on Solana using the Mermail PayBox MCP tools.
5. Replies to the sender with the transaction signature!

## Installation

1. Copy the `skills/mermail-invoice-payer` folder into your agent's `.agents/skills/` directory (e.g. for Antigravity, OpenClaw, or Cursor).
2. Configure the Mermail MCP Server in your `mcp_config.json`:

```json
{
  "mcpServers": {
    "mermail": {
      "command": "npx",
      "args": ["-y", "@mermail/mcp-server"]
    }
  }
}
```

3. Ensure your agent's Mermail PayBox is funded with enough USDC on Solana.

## Usage
Simply prompt your agent:
> "Check my Mermail inbox and pay any pending invoices."

The agent will automatically read its `SKILL.md` instructions and execute the workflow flawlessly.

## Demo Video
*(Link your loom or youtube demo here)*

