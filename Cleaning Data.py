import pandas as pd

df = pd.read_excel('Glassdoor_jobs3000.xlsx')

#Cleaning up Company Name, Removing Ratings:
df['CompanyName'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis=1)
df['CompanyName'] = df['CompanyName'].apply(lambda x: x.replace('\n',''))

#Cleaning up Salary Data:
df = df.fillna('-1')
df = df[df['Salary Estimate'] != '-1']
df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: str(x))
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

#Playing with Hourly & Employer Provided Salaries

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary' in x.lower() else 0)

#Removing Dollar Signs and Thousands Mark:
sub_dollarK = salary.apply(lambda x: x.replace('K', '').replace('$', ''))
sub_dollarK = sub_dollarK.apply(lambda x: x.replace('\n', ''))
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)

min_hr = sub_dollarK.apply(lambda x: x.lower().replace('per hour', '').replace('employer provided salary:', ''))

df['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df['min_salary'] + df['max_salary'])/2
df['avg_salary'] = round(df['avg_salary'], 2)

#Removing the State from a location:
df['State'] = df['Location'].apply(lambda x: x.split(',')[1])

#Age of Company:
df['agecompany'] = df['Founded'].apply(lambda x: x if x<1 else 2020-x)

#Requirements of Job:
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['R'] = df['Job Description'].apply(lambda x: 1 if 'r-studio' in x.lower() or 'r studio' in x.lower() else 0)
df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower()else 0)

#Senior Positions?
df['Senior'] = df['Job Title'].apply(lambda x: 1 if 'senior' in x.lower() or 'sr' in x.lower() else 0)

df.to_excel('CleanedData.xlsx', index=False)