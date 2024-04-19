
# Financial ChatBot
In this project, I created a conversational financial chatbot to answer questions about various financial metrics like total revenue, net income, total assets, current assets, total liabilities and current liabilities, current stockholder's equity etc. 





## Dataset
The dataset for this project has been manually created using the 10-K documents of Microsoft, Tesla and Apple for the years 2021-2023 based on the information gathered from the SEC EDGAR website:
https://www.sec.gov/edgar/search-and-access



## Run Locally

Clone the project

```bash
  git clone https://github.com/AnshumanTiware/financial_chatbot.git

Go to the project directory

Install dependencies

```bash
  pip install -r requirements.txt
```
Replace the apikey in api_key.py with your own OPENAI_API_KEY 
Start the server

```bash
  streamlit run app.py
```


## Usage Example
The chatbot can be used to answer various questions related to financial metrics of the companies in the dataset once the streamlit app server is up and running. The following are a few examples of the type of questions which can be asked.

Question 1: Which company had the highest mean revenue growth rate over the overall period ?
Question 2: What was tha value (in million dollars) of the Current Assets of TSLA (Tesla) in the year 2021? Note use Abbreviations for the company's name: TSLA -> Tesla; MSFT -> Microsoft; AAPL -> Apple

Question 3: Which company had the maximum profit margin in the year 2022?

Note: You can ask any question related to any column in the dataset for example Operational Cash Flow, net income growth, Return on Equity etc. You can also provide your own financial dataset by replacing the data.csv file in the project directory.


## Screenshots

[![app-interface.png](https://i.postimg.cc/7hQV13JX/app-interface.png)](https://postimg.cc/0KDDPJfJ)

