# 1st step install and import modules
  #-- pip install lxml
  #-- pip install requests
  #-- pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company = []
location = []
skills = []
links = []

# 2nd step use requests to fetch the url
result = requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# 3rd step save page content/markup
src = result.content
#print(src)

# 4th step create soup object to parse content
soup = BeautifulSoup(src, "lxml")
#print(soup)

# 5th step find the elemenents containing info we need
  #-- job titles, company names, location_names, job_skills
job_titles = soup.find_all("h2", {"class":"css-m604qf"})
company_names = soup.find_all("a", {"class":"css-17s97q8"})
locations_names = soup.find_all("span", {"class":"css-5wys0k"})
job_skills = soup.find_all("div", {"class":"css-y4udm8"})


# 6th step loop over returned lists to extract needed info into other lists
for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company.append(company_names[i].text)
    location.append(locations_names[i].text)
    skills.append(job_skills[i].text)
    links.append(job_titles[i].find("a").attrs["href"])
    

#print(job_title, company, location, skills)


# 7th step create csv file and fill it with values
file_list = [job_title, company, location, skills, links]
exported = zip_longest(*file_list)    #unpacking file_list
############################################################
# x = [1, 2, 3]        y = ["a", "b", "c"]       z = [x, y]
# zip_longest(*z) ---> [[1, 2, 3], ["a", "b", "c"]]
# ---> [1, a][2, b][3, c]
############################################################
with open("c:/Users\esraa\Desktop\Python_Projects\Scraping\pythonjobs.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Title", "Company", "Location", "Skills", "Link"])
    wr.writerows(exported)
    

