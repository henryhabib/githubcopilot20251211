# Prompts and Links Used in "Mastering GitHub Copilot Session"

## Example 1
- *def calculate_area_of_rectangle*
- *def calculate_date_difference*
- *def scrape_wikipedia_page*
- *remove rows where any column value is beyond 3 standard deviations*
- *# Test clean_data function to ensure it removes outliers correctly*

## Example 2
- *additionally, log an anomaly if temperature is below 70 and volt is under 0.8*
- *what happens if the temp is 86 and voltage is 0.2?*
- *explain, put it into a table*
- *generate unit tests*
- *add a test if the amount is negative*
- *generate docs*
- *this is not returning the discount price*

## Example 3
- *add a "very large expense" category if the expense amount > 10000*
```python
discounted_price = price
for _ in range(int(discount_rate)):
    discounted_price -= price * 0.01
return discounted_price 
```
- *summarize the change made, is this the most efficient way to do this?*
- *what's the impact of this logic?*

## Example 4
- create a real-time python flask application that retrieves and shows the price of bitcoin
- activate .venv, install all the necessary libraries in .venv, and run the app
- create a new repo, add the files (ignore .venv), commit, push to origin (private repo). Call the repo agent-example-20251211

## Example 5
- *add a password prompt so the user has to type in a password (password = "test") before the user can see the price of bitcoin*
- *The password "test 2" should also provide access*
- Use coding agents and get the best results: [Link](https://docs.github.com/en/enterprise-cloud@latest/copilot/tutorials/coding-agent/get-the-best-results)

## Example 6
- MCP Registry: [Link](https://github.com/mcp)
- Top MCP Server List: [Link](https://github.com/modelcontextprotocol/servers)
- *Check linear for what issues are outstanding that are tagged to me*

## Example 7
- About custom agents: [Link](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)
```code
---
# Fill in the fields below to create a basic custom agent for your repository.
# The Copilot CLI can be used for local testing: https://gh.io/customagents/cli
# To make this agent available, merge this file into the default repository branch.
# For format details, see: https://gh.io/customagents/config

name: JokeAgent
description: An agent that tells jokes on your code after reading your codebase
---

# My Agent

Read the codebase and tell a relevant joke on it. Do not produce any code.
```
- List of Custom Agents: [Link](https://github.com/github/awesome-copilot/tree/main/agents)