# Freelancer Project Bidder Bot
This is a Python script that can be used to place bids on projects on the Freelancer.com website. The script logs into the website using the provided credentials and searches for Python projects. It then selects a project based on the number of bids and average bid amount, and places a bid on the project with the provided bid text.

## How to Use
Make sure you have Python 3 and the necessary modules **(beautifulsoup4, selenium, undetected_chromedriver, colorama)** installed.
Replace the email and pswd variables in the script with your Freelancer.com email and password.
Replace the bid_text variable with the text you want to use for your bid.
Run the script using python bot.py
## Configuration
You can modify the following variables in the script to customize its behavior:

**time_delay_hr**: The number of hours to wait before checking for new projects.
**min_bid**: The minimum number of bids a project should have in order for the bot to place a bid.
**max_bid**: The maximum average bid amount a project should have in order for the bot to place a bid.
## Disclaimer
Please use this script responsibly and at your own risk. I am not responsible for any consequences that may happen
