import Scraping_Glassdoor as sc
import pandas as pd

path ='/home/artem/PycharmProjects/Scraping Indeed/chromedriver'

df = sc.get_jobs('data scientist', 1000, False, path, 3)

df.to_excel('Glassdoor_jobs3000.xlsx', index=False)