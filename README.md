## Stock Price Scraper & Visualiser
### Overview
This is a Python script that performs web scraping to obtain the real-time stock prices of specified companies. The script then stores the obtained data in a CSV file and visualizes the stock price data using matplotlib.

### Requirements
The following libraries are used in this script and need to be installed in your Python environment:

- pandas
- bs4
- requests
- matplotlib
- datetime



### How to Use the App
The script has two main components: the data scraping component and the data visualization component.

##### Data scraping component

The getData function takes in a stock symbol and returns a dictionary containing the stock price of the company. The function uses the requests library to access the stock's information from https://sg.finance.yahoo.com/. The data is then parsed using the BeautifulSoup library from the bs4 library. The data obtained is then added to a list that is used to create a Pandas DataFrame.

The script then iterates 100 times, and at each iteration, the stock prices of specified companies are obtained and added to the DataFrame. The resulting DataFrame is then saved to a CSV file named "Realtime stock data.csv".

##### Data visualization component
The second component of the script uses the Pandas library to read the data from the CSV file and the Matplotlib library to create a real-time stock price graph. The graph updates every second with new data.


## Troubleshooting
The script was created using a knowledge cut-off of 2021. Some changes in the website's HTML structure or API might affect the functionality of the script. If the script is not working, check the website's structure and make the necessary changes to the code.
If you are unable to install the required libraries, make sure that you have the latest version of pip and try installing the libraries again.
If you encounter any other errors, please check the documentation of the respective libraries for solutions.

### Note:
The script was created using a knowledge cut-off of 2023. Some changes in the website's HTML structure or API might affect the functionality of the script.
