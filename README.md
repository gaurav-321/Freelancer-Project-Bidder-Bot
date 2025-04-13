# Freelancer Project Bidder Bot 🚀

✨ **Description**  
The Freelancer Project Bidder Bot is a Python script designed to automate the process of bidding on projects on Freelancer.com. It specifically targets Python projects based on certain criteria, making it an efficient tool for freelancers looking to maximize their earnings.

🚀 **Features**
- **User Authentication:** Handles user login to access Freelancer.com.
- **Project Search:** Searches for Python projects on the platform.
- **Project Selection:** Chooses a project based on bid count and average bid amount.
- **Bid Placement:** Submits a bid on the selected project using customizable text.

🛠️ **Installation**
To get started with the Freelancer Project Bidder Bot, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/gag3301v/Freelancer-Project-Bidder-Bot.git
   ```

2. Install the required dependencies using pip:
   ```bash
   pip install beautifulsoup4 selenium undetected_chromedriver colorama
   ```

📦 **Usage**
Here’s how you can use the script:

```python
# Replace 'email', 'password', and 'bid_text' with your actual values
email = 'your_email@example.com'
password = 'your_password'
bid_text = 'Your custom bid text here'

from bot import login, search_projects, select_project, place_bid

# Login to Freelancer
login(email, password)

# Search for Python projects
projects = search_projects()

# Select a project based on criteria
selected_project = select_project(projects)

# Place a bid on the selected project
place_bid(selected_project, bid_text)
```

🔧 **Configuration**
You can configure the script by setting environment variables or modifying the script directly:

- **time_delay_hr**: Delay between project checks (default: 1 hour).
- **min_bid**: Minimum number of bids a project must have to be considered (default: 5).
- **max_bid**: Maximum average bid amount for a project (default: 200).

Example environment variables:
```bash
export TIME_DELAY_HR=1
export MIN_BID=5
export MAX_BID=200
```

🧪 **Tests**
The script includes basic tests to ensure functionality. To run the tests, execute:

```bash
python -m unittest test_bot.py
```

📁 **Project Structure**
```
Freelancer-Project-Bidder-Bot/
├── README.md
├── bot.py
└── test_bot.py
```

🙌 **Contributing**
Contributions are welcome! If you have any ideas, bug fixes, or improvements, please submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

📄 **License**
This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.