# Data_Scientist_Jobs_Project
### Created a Project to estimate salaries (MAE around $11K) on Data Scientist Jobs to help understand the workspace landscape
* Scraped about 1000 jobs from Glassdoor utilizing selenium and python
* Created features from the job description to help understand the value companies place on python and excel
* Optimized Lasso, Random Forest and Gradient Boosting Regressor using GridsSearch CV
* Created Client facing API using Flask


## Resources
**Scraper Github:** https://github.com/arapfaik/scraping-glassdoor-selenium  
**Scraper Article:** https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2  


## Code uses:
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle  
**For Web Framework Requirements:** pip install -r requirements.txt

## WEB Scraping:
Edited the webscraper from the github repository listed above to scrape 1000 jobs from Glassdoor.com. With each job recieved the following data:
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
### Here we can see the correlations between a few of the variables:  
![alt text](https://github.com/Artemness/Data_Scientist_Jobs_Project/blob/master/heatmap.png "Correlations")  

### The Top Locations Hiring are located in large metropolitan areas:  
![alt text](https://github.com/Artemness/Data_Scientist_Jobs_Project/blob/master/TopLocationsHiring.png "Top Locations")  

### The Top Companies Hiring are listed below:
![alt text](https://github.com/Artemness/Data_Scientist_Jobs_Project/blob/master/Top20CompaniesHiring.png "Top Companies")  

### The Top Sectors Hiring are listed below:
![alt text](https://github.com/Artemness/Data_Scientist_Jobs_Project/blob/master/Sectors.png "Top Sectors")  
* As expected IT is up near the top and greatly dominates the pool of jobs. However, of interest is that business services is ranked number two in terms of sectors. Of note Finance is ranked third and therefore a number of tasks are likely being accomplished in this field by Data Scientists.

### Average Salaries broken out by Company Revenue:
![alt text](https://github.com/Artemness/Data_Scientist_Jobs_Project/blob/master/CompanyRevenue.png "Company Revenues")  
* If a paycheck is what you're looking for then a startup with under a million dollars in revenue is going to be your best bet, likely due to the instability surrounding job security. However, a close runner up with greater job security would be a massively large company with over $10 Billion in Revenue. Likely more challenging to gain a position in this kind of company and therefore the average salary is quite high.


## Model Building:
Firstly, I transformed the categorial variables into dummy variables. Then I split the data into train and test sets with a test set of 30%.  
I tried out three different models and evaluated their performance based on Mean Absolute Error. I chose MAE because of the ease of interpretation and since it stands up to outliers fairly well.  
The models I used were:  
**Lasso Regression** - Due to the sparse data for many categorical features, a normalized regression like Lasso should prove effective.  
**Random Forest** - Due to the sparsity associated with the data, I expected a decent fit from this model as well.  
**Gradient Boosting** - Gradient Boosting seemed like an effective choice for this data set as well.  

## Model Performance:
The Random Forest Model proved to be the most effective and outperformed the other approaches on both the training and validation sets:
* Lasso Regression = 17.73  
* **Random Forest = 10.58**  
* Gradient Boosting = 14.61  

## Productionization
Here I built a Flask API endpoint that was hosted on a local server by folowing a tutorial referenced in the section above. The API endpoint takes a request with a list of values from a job listing and returns an estimated salary for those values based on the Random Forest Model noted above.

