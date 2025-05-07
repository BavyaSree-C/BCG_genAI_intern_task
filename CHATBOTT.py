import pandas as pd
import datetime

# Load reports
final_report = pd.read_csv('/content/final_BCG_report.csv')
summary_report = pd.read_csv('/content/final_BCG_report.csv')

# Basic preprocessing
final_report['Company'] = final_report['Company'].str.lower()
summary_report['Company'] = summary_report['Company'].str.lower()

# Log function
def log_interaction(company, year, query, response, error=None):
    with open("chatbot_logs.txt", "a") as log_file:
        log_file.write(f"Timestamp: {datetime.datetime.now()}\n")
        log_file.write(f"Company: {company}, Year: {year}, Query: {query}\n")
        log_file.write(f"Response: {response}\n")
        if error:
            log_file.write(f"Error: {str(error)}\n")
        log_file.write("------------------------------------------------------\n")

# Financial Chatbot Function
def financial_chatbot(company_input, fiscal_year, user_query):
    company = company_input.lower()
    year = fiscal_year

    try:
        row_final = final_report[(final_report['Year'] == year) & (final_report['Company'] == company)]
        row_summary = summary_report[summary_report['Company'] == company]

        if row_final.empty or row_summary.empty:
            raise ValueError("Data not found for the provided company/year.")

        if "revenue" in user_query and "growth" not in user_query:
            response = f"The Total Revenue for {company_input} in {year} is $ {row_final['Total Revenue'].values[0]}"
        
        elif "net income" in user_query and "growth" not in user_query:
            response = f"The Net Income for {company_input} in {year} is $ {row_final['Net Income'].values[0]}"
        
        elif "total assets" in user_query:
            response = f"The Total Assets for {company_input} in {year} is $ {row_final['Total Assets'].values[0]}"
        
        elif "total liabilities" in user_query:
            response = f"The Total Liabilities for {company_input} in {year} is $ {row_final['Total Liabilities'].values[0]}"
        
        elif user_query == "What is the total revenue?":
            revenue = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Total_Revenue'].values[0]
            return f"The Total Revenue for {company_input} for fiscal year {fiscal_year} is $ {revenue}"
    
        elif user_query == "What is the Net Income?":
            net_income  = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Net_Income'].values[0]
            return f"The Net Income for {company_input} for fiscal year {fiscal_year} is $ {net_income}"
        
        elif user_query == "What is the sum of total assets?":
            total_assets  = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Total_Assets'].values[0]
            return f"The sum of Total Assets for {company_input} for fiscal year {fiscal_year} is $ {total_assets}"
        
        elif user_query == "What is the sum of total liabilities?":
            total_liabilities  = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Total_Liabilities'].values[0]
            return f"The sum of Total Liabilities for {company_input} for fiscal year {fiscal_year} is $ {total_liabilities}"
        
        elif user_query == "What is cash flow from operating activities?":
            cash_ops = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Cash_Flow'].values[0]
            return f"The Cash Flow from Operating Activities for {company_input} for fiscal year {fiscal_year} is $ {cash_ops}"
        
        elif user_query == "What is the revenue growth(%) ?":
            revenue_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
            return f"The Revenue Growth(%) for {company_input} for fiscal year {fiscal_year} is {revenue_growth}(%)"
        
        elif user_query == "What is the net income growth(%) ?":
            net_income_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
            return f"The Net Income Growth(%) for {company_input} for fiscal year {fiscal_year} is {net_income_growth}(%)"
        
        elif user_query == "What is the assets growth(%) ?":
            assets_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Assets Growth (%)'].values[0].round(4)
            return f"The Assets Growth(%) for {company_input} for fiscal year {fiscal_year} is {assets_growth}(%)"
        
        elif user_query == "What is the liabilities growth(%) ?":
            liabilities_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
            return f"The Liabilities Growth(%) for {company_input} for fiscal year {fiscal_year} is {liabilities_growth}(%)"
        
        elif user_query == "What is the cash flow from operations growth(%) ?":
            cash_ops_growth = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company_Name'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
            return f"The Cash Flow from Operations Growth(%) for {company_input} for fiscal year {fiscal_year} is {cash_ops_growth}(%)"
        
        elif user_query == "What is the year by year average revenue growth rate(%)?":
            year_avg_revenue_growth = summary_report[(summary_report['Company_Name'] == company_input)]['Revenue Growth (%)'].values[0].round(4)
            return f"The Year By Year Average Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_revenue_growth}(%)"
        
        elif user_query == "What is the year by year average net income growth rate(%)?":
            year_avg_net_income_growth = summary_report[(summary_report['Company_Name'] == company_input)]['Net Income Growth (%)'].values[0].round(4)
            return f"The Year By Year Net Income Revenue Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_net_income_growth}(%)"
        
        elif user_query == "What is the year by year average assets growth rate(%)?":
            year_avg_assets_growth = summary_report[(summary_report['Company_Name'] == company_input)]['Assets Growth (%)'].values[0].round(4)
            return f"The Year By Year Average Assets Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_assets_growth}(%)"
        
        elif user_query == "What is the year by year average liabilities growth rate(%)?":
            year_avg_liabilities_growth = summary_report[(summary_report['Company_Name'] == company_input)]['Liabilities Growth (%)'].values[0].round(4)
            return f"The Year By Year Average Liabilities Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_liabilities_growth}(%)"
        
        elif user_query == "What is the year by year average cash flow from operations growth rate(%)?":
            year_avg_cash_ops_growth = summary_report[(summary_report['Company_Name'] == company_input)]['Cash Flow from Operations Growth(%)'].values[0].round(4)
            return f"The Year By Year Average Cash Flow from Operations Growth Rate(%) from 2021 to 2023 for {company_input} is {year_avg_cash_ops_growth}(%)" 
        
        else:
            response = "Sorry, I couldn't understand your question. Please ask about revenue, net income, assets, liabilities, or growth rates."

        log_interaction(company_input, year, user_query, response)
        return response

    except Exception as e:
        error_message = "Data not available or invalid input. Please check the company name, year, or try another query."
        log_interaction(company_input, year, user_query, error_message, error=e)
        return error_message


# Chatbot session
def run_chatbot():
    print("\nWelcome to the AI Financial Chatbot!")
    print("I can answer your financial queries related to Apple, Tesla, or Microsoft (2021-2023).")

    while True:
        print("------------------------------------------------------------------")
        user_input = input("\nType 'hi' to start or 'exit' to quit: ").lower()
        if user_input == 'exit':
            print("Thank you for using the chatbot. Goodbye!")
            break
        elif user_input == 'hi':
            company_input = input("Enter Company Name (Apple, Tesla, Microsoft): ").capitalize()
            if company_input not in ['Apple', 'Tesla', 'Microsoft']:
                print("Invalid company. Please try again.")
                continue

            try:
                fiscal_year = int(input("Enter Fiscal Year (2021, 2022, or 2023): "))
                if fiscal_year not in [2021, 2022, 2023]:
                    print("Invalid year. Please try again.")
                    continue
            except:
                print("Year must be numeric. Try again.")
                continue

            while True:
                user_query = input("\nAsk your financial question (or type 'back' to change company/year): ").lower()
                if user_query == 'back':
                    break
                elif user_query == 'exit':
                    print("Session ended. Thank you.")
                    return
                else:
                    print(financial_chatbot(company_input, fiscal_year, user_query))
        else:
            print("Please type 'hi' to begin or 'exit' to quit.")
