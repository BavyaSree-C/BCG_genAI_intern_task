# **📊 Financial Performance Chatbot**

This project is a data-driven chatbot designed to assist users in querying the financial performance of major companies (Microsoft, Tesla, and Apple) across different fiscal years. The chatbot is powered by a structured dataset manually created from financial reports, including key metrics such as revenue, net income, total assets, liabilities, and cash flow.

# 🔁 Workflow Overview
- **Data Collection & Preparation:**

Financial data was manually gathered for three companies over a span of three years. Calculations were performed to derive growth rates for each financial metric.

- **Data Processing:**

The dataset was cleaned, missing values were filled, and summary statistics (mean, max, min) were computed per company to create a comprehensive financial report.

- **CSV Export:**

Both the detailed dataset and a summarized version were exported as CSV files for use in chatbot responses.

- **Chatbot Development:**

A custom chatbot script (CHATBOTT.py) was developed in Python. It reads the CSV files, understands natural language queries using keyword matching, and returns precise financial data based on user input.

- **User Interaction:**

Users input a company name, fiscal year, and a financial query (e.g., "What is the revenue growth in 2022?"). The chatbot processes the query and provides an accurate response, while logging all interactions.

- **Testing & Validation:**

The chatbot was tested through interactive queries to ensure that it correctly interprets and responds to a variety of financial questions.

**BCG GenAI Job Simulation on Forage - May 2025**
- Completed a job simulation involving AI-powered financial chatbot development for BCG's GenAI Consulting team.
- Gained experience in Python programming, including the use of libraries such as pandas for data manipulation.
- Integrated and interpreted complex financial data from 10-K and 10-Q reports, employing rule-based logic to create a chatbot that provides user-friendly financial insights and analysis.
