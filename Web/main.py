from bs4 import BeautifulSoup
import requests


def job_filter():
    wanted_skill = input("Enter the skills that you are familiar with => ")
    print(f"Filtering out {wanted_skill}")
    html_content = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from"
                                "=submit&txtKeywords=java&txtLocation=")
    soup = BeautifulSoup(html_content.content, 'lxml')
    job_list = soup.find_all('ul', class_="list-job-dtl clearfix")
    titles = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    container = soup.find_all('div', class_="applied-dtl clearfix")
    for index, content in enumerate(container):
        published_date = content.find('span', class_="sim-posted").text
        if 'few' in published_date:
            for jobs in job_list:
                for title in titles:
                    company_name = title.h3.text.replace(' ', '')
                    description = jobs.li.text.replace(' ', '')
                    more_info = jobs.li.a["href"]
                    skills = jobs.span.text.replace(' ', '')
                    if wanted_skill in skills:
                        with open(f'jobs/{index}.txt', 'w') as job_file:
                            job_file.write(f"\nCompany Name: {company_name.strip()}")
                            job_file.write(f"\n{description.strip()}")
                            job_file.write(f"\nRequired Skills: {skills.strip()}\n")
                            job_file.write(f"More Info: {more_info}")
                        print(f"File Saved: {index}")

if __name__ == "__main__":
    while True:
        job_filter()