import requests
from bs4 import BeautifulSoup
from datetime import datetime

from models import JobItem
from server import db


# Jobs from sites
jobsItems_from_jobberman=[]
jobsItems_from_timesjobs=[]


def scrape_from_jobberman():
    jobberman_url = requests.get("https://www.jobberman.com.gh/jobs?sort_by=latest").text
    soup = BeautifulSoup(jobberman_url,'lxml')

    jobbermab_content = soup.find_all('header', class_="search-result__header")

    for job in jobbermab_content:
        title_ = job.h3.text
        job_type = job.find('span', class_="search-result__job-type").text
        company=job.find('div', class_="if-content-panel padding-lr-20 flex-direction-top-to-bottom--under-lg align--start--under-lg search-result__job-meta").text
        source_url=job.find('a')['href']
        image=""

        job_item = JobItem(
            title = title_.strip(),
            company = company.strip(),
            job_type = job_type.strip(),
            source_name = "Jobberman",
            source_url = source_url,
            image = image,
        )

        jobsItems_from_jobberman.append(job_item)
    db.session.add_all(jobsItems_from_jobberman)
  

def scrape_from_timesjobs():
    timesjobs_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35"
    timesjobs_content = requests.get(timesjobs_url).text

    soup = BeautifulSoup(timesjobs_content,'lxml')

    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        title_ = job.header.h2.text
        job_type = "Unknown"
        company= job.header.h3.text
        source_url= job.header.h2.a['href']
        image=""

        job_item = JobItem(
            title = title_.strip(),
            company = company.strip(),
            job_type = job_type.strip(),
            source_name = "TimesJobs",
            source_url = source_url,
            image = image,
        )

        jobsItems_from_timesjobs.append(job_item)
    db.session.add_all(jobsItems_from_timesjobs)
        

scrape_from_timesjobs()
scrape_from_jobberman()
db.commit()