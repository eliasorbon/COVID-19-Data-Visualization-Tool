# COVID-19 Data Visualization Tool

This Python script fetches real-time COVID-19 data from a public API and creates a bar chart showing the top 10 countries by total cases. It also displays some basic statistics about the top 5 countries.

## Features

- Fetches real-time COVID-19 data from the disease.sh API
- Creates a bar chart of the top 10 countries by total cases
- Saves the chart as a PNG file
- Prints statistics for the top 5 countries

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or later installed on your system
- pip package manager

## Installation

1. Clone this repository or download the script file.

2. Install the required Python libraries using pip:

   ```
   pip install requests pandas matplotlib
   ```

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing the script.

3. Run the script using Python:

   ```
   python covid_data_viz.py
   ```

4. The script will generate a bar chart image named 'covid_cases_by_country.png' in the same directory.

5. Check the console output for statistics on the top 5 countries by total cases.

## Sample Output

The script will generate a bar chart image and print statistics to the console. For example:

```
Plot saved as 'covid_cases_by_country.png'

Top 5 countries by total cases:
       country      cases
0  United States  32346970
1         India   24046809
2        Brazil   15359397
3        France    5780379
4        Turkey    5044936
```

## Contributing

Contributions to this project are welcome. Feel free to open an issue or submit a pull request.
