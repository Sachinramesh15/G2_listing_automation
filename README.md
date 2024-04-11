# G2 Product Listing Automation

This project automates the fetching of software product data from G2 and Product Hunt, compares the datasets to find unique entries in Product Hunt that are not listed in G2, and outputs these unique product names to a CSV file. It is intended to help users identify new software products on Product Hunt that may be potential candidates for inclusion on the G2 platform.

## Project Structure

- `fetch_and_compare.py`: Main script that integrates fetching data from G2, fetching data from Product Hunt, comparing the data, and saving the results.
- `requirements.txt`: Contains all Python dependencies for the project.
- `output/`: Directory where the output CSV file `unique_names.csv` is stored after script execution.

## Getting Started

### Prerequisites

- Python 3.6+
- pip
- Access to G2 and Product Hunt APIs (API keys required)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sachinramesh15/G2_listing_automation.git
2. **install the packages though requirements.txt**
  - ```bash
     pip install -r requirements.txt
3. **Set up environment variables**
- Ensure you have the necessary API keys for G2 and Product Hunt. Set them as environment variables or directly in the script (not recommended for production).
  ```bash
  export G2_API_KEY='your_g2_api_key'
  export PRODUCTHUNT_TOKEN='your_producthunt_token'
The script will fetch data from both APIs, compare the data sets, and output the unique software names from Product Hunt to the output/unique_names.csv file.

### Contributing
Contributions are welcome! 





