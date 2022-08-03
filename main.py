import time
import undetected_chromedriver as uc
import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.by import By
from colorama import init, Fore

init()

RED, BLUE, WHITE, GREEN = Fore.RED, Fore.BLUE, Fore.WHITE, Fore.GREEN
email = ""
pswd = ""
bid_text = """
Hi,
I have read your project description very carefully and I am confident I can complete the project.
I have 4 years of experience in python and worked on a lot of automation bots, scraping scripts, web and API development, etc.
Also, I worked in the field of Image Processing, Machine Learning, and data processing
I understand your requirement and I am sure you would be happy with my work. You can check my portfolio at "https://github.com/gaurav-321" and all the 5-star reviews in my profile.

If interested we can further discuss the project.

Thanks, & Regards
Gaurav Verma
"""


def login():
    link = "https://www.freelancer.com/login"
    options = uc.ChromeOptions()
    options.headless = True
    browser = uc.Chrome(options=options)
    browser.get(link)
    if browser.current_url == "https://www.freelancer.com/dashboard":
        return browser
    browser.find_element(By.ID, "emailOrUsernameInput").send_keys(email)
    browser.find_element(By.ID, "passwordInput").send_keys(pswd)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    while browser.current_url != "https://www.freelancer.com/dashboard":
        pass
    return browser


def get_projects():
    browser.get("https://www.freelancer.com/jobs/python/1/?ngsw-bypass=&w=f")
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    trs = soup.find_all("tr", {'class': 'project-details'})
    projects = []
    for tr in trs:
        try:
            if " / hr" not in tr.text and " - ₹" not in tr.text:
                temp = {}
                temp['href'] = tr.find("a")['href']
                temp['title'] = tr.find("a").text
                temp['bid'] = int(tr.find("div", {'class': 'bids-col-inner'}).text)
                temp['avg_bid'] = int(tr.find("span", {'class': 'average-bid'}).text.replace("₹", ""))
                temp['bid_link'] = "https://www.freelancer.com" + tr.find("a", {'class': 'bid-now'})['href']
                projects.append(temp)
        except:
            pass
    return projects


def place_bid(project):
    link = project['bid_link']
    print(f"{GREEN}[+]{WHITE} Placing bid on {project['title']} of ₹{project['avg_bid']}")
    browser.get(link)
    if "Great! Your bid has been placed successfully! Good job!" in browser.page_source:
        return "Already bid"
    browser.find_element(By.ID, "proposalDescription").send_keys(bid_text)
    time.sleep(2)
    browser.find_element(By.ID, "place-bid").click()
    time.sleep(2)


if __name__ == "__main__":
    projects_done = []
    browser = login()
    print(f"{GREEN}[+]{WHITE} Logged in successfully")
    browser.maximize_window()
    while True:
        browser.get("https://freelancer.com/dashboard")
        browser.implicitly_wait(10)
        current_bid = int(browser.find_element(By.XPATH,
                                               "/html/body/app-root/app-logged-in-shell/div/fl-container/div/div/ng-component/app-dashboard-home/fl-page-layout/main/fl-container/fl-grid/fl-col[2]/fl-page-layout-secondary/app-dashboard-widget/fl-bit/app-insights-bid-summary-widget/fl-card/fl-bit/fl-bit[2]/fl-bit/fl-text/span/fl-text/span").text.split(
            " ")[0])
        projects = get_projects()[:20]
        print(f"{GREEN}[+]{WHITE} Found {len(projects)} projects")
        for project in projects:
            if 10000 > project['avg_bid'] > 700 and current_bid > 10 and project not in projects_done and project[
                'bid'] < 25:
                if place_bid(project):
                    projects_done.append(project['bid_link'])
                    current_bid -= 1
                    print(f"{WHITE}Bid left: {current_bid}")
                else:
                    projects_done.append(project['bid_link'])
                    print(f"{WHITE}Bid left: {current_bid}")
        print(f"{GREEN}[+]{WHITE} Sleeping for 2 minutes")
        time.sleep(60 * 2)
