#G2 Product Comparison Automation
This project automates the process of fetching data about new software products from the G2 website and Product Hunt API, compares the two datasets, and identifies products that are listed on Product Hunt but not on G2.

Overview
The script performs several key functions:

Data Fetching: It retrieves data from the G2 API and Product Hunt API.
Data Comparison: Compares the fetched data to find unique new software listings on Product Hunt that are not present on G2.
Reporting: Outputs the unique listings to a CSV file.
Setup and Configuration
Prerequisites
Python 3.x

Install required Python libraries: requests and fuzzywuzzy. Install these using pip:

bash
Copy code
pip install requests fuzzywuzzy python-Levenshtein
Files
main_script.py: The main Python script that handles data fetching, comparison, and output.
G2_extracted_data.json: JSON file for storing the data fetched from G2.
producthunt.json: JSON file for storing the data fetched from Product Hunt.
unique_names.csv: Output file that lists unique software products found on Product Hunt but not on G2.
Environment Variables
Ensure you have set the following environment variables for the script to authenticate properly with the APIs:

G2_API_KEY: Your G2 API key.
PRODUCTHUNT_TOKEN: Your Product Hunt API token.
You can set these variables in your environment or directly in the script (not recommended for production).

Usage
To run the script, simply execute the following command in your terminal or command prompt:

bash
Copy code
python main_script.py
Automation
To automate this script on a Windows system, use the Task Scheduler:

Open Task Scheduler and create a new task.
Set the trigger to the desired time for the script to run (e.g., daily at 3 AM).
Set the action to start the program, pointing to your Python executable and providing the path to main_script.py as an argument.
For Unix-based systems, set up a cron job as described in the script documentation.

Output
The script will generate a unique_names.csv file containing the names of software products that are listed on Product Hunt but not on G2. This file is saved in the project directory and can be used for further analysis or reporting.

Contributions
Contributions are welcome. Please fork the repository and submit a pull request with your enhancements.
