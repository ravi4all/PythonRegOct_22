import bs4
import urllib.request as url
path = "https://www.freshersworld.com/jobs/jobsearch/python-jobs"

response = url.urlopen(path)
page = bs4.BeautifulSoup(response,"html.parser")

job = page.find("div", {"class" : "job-container"})
company = job.find("h3", {"class" : "latest-jobs-title"})
jobTitle = job.find("a").find_next_sibling("div")
qualification = job.find("div", {"class" : "qualification-block"})
skills = job.find("span", {"class" : "eligibility-skills"})
desc = job.find("span", {"class" : "desc"})

print("Company :",company.text)
print("Job :",jobTitle.text)
print("Qualification :",qualification.text)
print("Skills :",skills.text)
print("Job Description :",desc.text)

