import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data from the API
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
data = response.json()

# Create a DataFrame
df = pd.DataFrame(data)

# Sort by total cases and get top 10 countries
top_10 = df.sort_values('cases', ascending=False).head(10)

# Create a bar plot
plt.figure(figsize=(12, 6))
plt.bar(top_10['country'], top_10['cases'])
plt.title('Top 10 Countries by COVID-19 Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the plot
plt.savefig('covid_cases_by_country.png')
print("Plot saved as 'covid_cases_by_country.png'")

# Display some statistics
print("\nTop 5 countries by total cases:")
print(top_10[['country', 'cases']].head())
