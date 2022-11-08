import bs4
import urllib.request as url
path = "https://www.freshersworld.com/jobs/jobsearch/java-jobs"

response = url.urlopen(path)
page = bs4.BeautifulSoup(response,"html.parser")

jobs = page.find_all("div", {"class" : "job-container"})

for job in jobs:
    company = job.find("h3", {"class" : "latest-jobs-title"})
    jobTitle = job.find("a").find_next_sibling("div")
    qualification = job.find("div", {"class" : "qualification-block"})
    skills = job.find("span", {"class" : "eligibility-skills"})
    if not skills:
        skills = "Skills Not Defined..."
    else:
        skills = skills.text
    desc = job.find("span", {"class" : "desc"})

    print("Company :",company.text)
    print("Job :",jobTitle.text)
    print("Qualification :",qualification.text)
    print("Skills :",skills)
    print("Job Description :",desc.text)

    print("*" * 50)

