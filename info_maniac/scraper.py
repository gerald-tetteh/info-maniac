import requests
import random
from bs4 import BeautifulSoup
from info_maniac.models import JobItem
from info_maniac import db
from requests.compat import quote_plus


job_image_url = "images/job-image-{}.png"

def scrape_from_jobberman():
  jobberman_url = requests.get("https://www.jobberman.com.gh/jobs?sort_by=latest").text
  soup = BeautifulSoup(jobberman_url,'lxml')
  jobsItems_from_jobberman = []

  jobbermab_content = soup.find_all('header', class_="search-result__header")

  for job in jobbermab_content:
    image_number = random.randint(1,16)
    title_ = job.h3.text
    job_type = job.find('span', class_="search-result__job-type").text
    company = job.find('div', class_="if-content-panel padding-lr-20 flex-direction-top-to-bottom--under-lg align--start--under-lg search-result__job-meta").text
    source_url = job.find('a')['href']
    image_url = job_image_url.format(image_number)

    job_item = JobItem(
      title = title_.strip(),
      company = company.strip(),
      job_type = job_type.strip(),
      source_name = "Jobberman",
      source_url = source_url,
      image_url = image_url,
    )

    jobsItems_from_jobberman.append(job_item)
  return jobsItems_from_jobberman
  
def scrape_from_timesjobs():
  timesjobs_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35"
  timesjobs_content = requests.get(timesjobs_url).text
  jobsItems_from_timesjobs = []
  soup = BeautifulSoup(timesjobs_content,'lxml')

  jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

  for job in jobs:
    image_number = random.randint(1,16)
    title_ = job.header.h2.text
    job_type = "Unknown"
    company = job.header.h3.text
    source_url = job.header.h2.a['href']
    image_url = job_image_url.format(image_number)

    job_item = JobItem(
      title = title_.strip(),
      company = company.strip(),
      job_type = job_type.strip(),
      source_name = "TimesJobs",
      source_url = source_url,
      image_url = image_url,
    )

    jobsItems_from_timesjobs.append(job_item)
  return jobsItems_from_timesjobs

def save_jobs(list_of_jobs):
  for job in list_of_jobs:
    try:
      db.session.add(job)
      db.session.commit()
    except Exception as e:
      db.session.rollback()
        
def scrape_and_save():
    print("starting")
    jobs_from_timesjobs = scrape_from_timesjobs()
    jobs_from_jobberman = scrape_from_jobberman()
    print("done scraping")
    save_jobs(jobs_from_jobberman)
    save_jobs(jobs_from_timesjobs)
    print("done saving")

def search_jobberman_scraper(query):
    query = quote_plus(query)
    base_url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={query}&txtLocation="
    site_content = requests.get(base_url).text
    jobsItems_from_timesjobs=[]

    

    soup = BeautifulSoup(site_content, 'lxml')

    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for job in jobs:
        image_number = random.randint(1,16)
        title_ = job.header.h2.text
        job_type = "Unknown"
        company = job.header.h3.text
        source_url = job.header.h2.a['href']
        image_url = job_image_url.format(image_number)

        job_item = JobItem(
        title = title_.strip(),
        company = company.strip(),
        job_type = job_type.strip(),
        source_name = "TimesJobs",
        source_url = source_url,
        image_url = image_url,
        )
    return jobsItems_from_timesjobs