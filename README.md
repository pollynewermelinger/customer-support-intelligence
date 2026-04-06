# Customer Support Intelligence Platform

An end-to-end Analytics + AI portfolio project simulating a real customer support operation for a global hospitality company.

## Overview

This project was designed to simulate how a data professional can build a complete intelligence solution for customer support, from raw data to actionable insights.

The solution combines:
- structured ticket data
- operational KPI monitoring
- automated insight generation
- an executive dashboard for decision-making

The goal is to help support and operations teams identify bottlenecks, prioritize actions, and improve service performance at scale.

---

## Business Problem

Customer support teams often deal with:
- high ticket volume
- recurring issues across channels and regions
- SLA breaches
- slow manual analysis of operational problems
- difficulty identifying the main causes behind customer dissatisfaction

This project addresses that challenge by creating a centralized analytics solution that organizes support data and highlights performance issues with a business-oriented view.

---

## Solution

I developed an end-to-end support intelligence solution that:

- consolidates customer support ticket data
- tracks key support KPIs
- identifies trends and bottlenecks by category, channel, and region
- provides automated insight suggestions inspired by AI workflows
- delivers an interactive dashboard for operational monitoring

---

## Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Plotly**
- **Streamlit**
- **SQL-oriented pipeline logic**
- **LLM-ready / AI-inspired workflow design**

---

## Project Structure

```bash
customer-support-intelligence/
│
├── app/
│   └── dashboard.py
│
├── data/
│   └── support_tickets.csv
│
├── scripts/
│   └── etl.py
│
├── dashboard.html
├── requirements.txt
└── README.md
```

## Main Features
### 1. Data Pipeline

A simple ETL logic was created to simulate ingestion, transformation, and KPI generation from raw support ticket data.

### 2. Operational KPIs

The project tracks key customer support metrics such as:

- total number of tickets
- average first response time
- average resolution time
- CSAT score
- SLA breach rate
### 3. Interactive Dashboard

A dashboard was built to provide a business-friendly view of support performance by:

- day
- category
- channel
- region
### 4. AI-Inspired Insight Layer

The project includes an AI-inspired logic to simulate how automated classification, summaries, and support insights could be generated in a real business environment.

## Example Use Cases

This solution can support teams such as:

- Customer Support
- Operations
- Customer Experience
- Product
- Business Intelligence

Possible decisions supported by this dashboard:

- which support categories generate the most SLA breaches
- which channels require faster triage
- where resolution time is above target
- which operational flows should be reviewed first

## How to Run the Project
1. Clone the repository
```bash
git clone https://github.com/pollynewermelinger/customer-support-intelligence.git
```
2. Access the project folder
```bash
cd customer-support-intelligence
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the dashboard
```bash
streamlit run app/dashboard.py
```
## Static Dashboard

## Dashboard Preview

### Overview
![Dashboard Overview](/dashboard-overview.png)


## Business Impact

This project was designed to demonstrate how data can be used to improve operational visibility and reduce manual effort in support environments.

Expected benefits of this type of solution include:

- faster issue identification
- better prioritization of operational actions
- improved visibility of service performance
- reduced manual analysis effort
- more data-driven support decisions

## Why This Project Matters

This project reflects the type of work required in modern data-driven environments:

- connecting business problems to technical solutions
- building analytics end-to-end
- structuring data for decision-making
- using AI concepts to improve scale and efficiency

It represents my interest in working on practical, high-impact analytics solutions that combine business context, structured data, and intelligent automation.

## Next Steps

Future improvements could include:

- integration with real APIs
- dbt-based modeling layer
- workflow orchestration
- anomaly detection
- LLM integration for ticket clustering and root cause summarization
- deployment in a cloud environment

## Author

Pollyne Wermelinger
Data Analyst | BI | Analytics | AI-driven solutions

LinkedIn: pollyne-wermelinger
