from jobspy import scrape_jobs
import os


wd = os.path.dirname(__file__)
save_as = os.path.join(wd, "jobs.json")

# Scrape jobs and save as json. Early setup so we can get some data and play with it.
# json save is so we don't need to slam the scraper too hard during testing. 
job_data = scrape_jobs(
    site_name=["Indeed"],
    search_term="devops",
    location="Boston, MA",
    hours_old=144,
    results_wanted=60,
    country_indeed="USA"
)

job_data.to_json(save_as, orient="records", lines=False)
