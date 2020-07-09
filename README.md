# Data_Scientist_Jobs_Project
Project on Data Scientist Positions and their respective salaries
### Created a Project to estimate salaries on Data Scientist Jobs to help understand the workspace landscape
* Scraped about 1000 jobs from Glassdoor utilizing selenium and python
* Created features from the job description to help understand the value companies place on python and excel
* Optimized Lasso, Random Forest and Gradient Boosting Regressor using GridsSearch CV
* Created Client facing API using Flask


## Resources
https://github.com/arapfaik/scraping-glassdoor-selenium
Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium
Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905
Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2


## Code uses:
**Python Version:** 3.7
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
**For Web Framework Requirements:** pip install -r requirements.txt

## WEB Scraping:
Edited the webscraper from the github repository listed aboce to scrape 1000 jobs from Glassdoor.com. With each job recieved the following data:
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company Name
* Location
* Headquarters
* Size
* Founded
* Type of ownership
* Industry
* Sector
* Revenue
* Competitors

## Data Cleaning:
After scraping the data I needed to clean it up for use in the model. Made the following changes:
* Parsed numeric data out of salary
* Created columns for hourly wages and employer provided salary
* Parsed rating out of company name
* Changed foundation date into age of company
** Created columns if the following skills were in the job description:
    * Python
    * R
    * Excel
* Created Column for Simplified Job Title
* Created Columns for Seniority if it was listed in the Job Title

## Exploratory Data Analysis:
