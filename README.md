# London Transportation Analysis

## 📌 Project Overview
This project analyzes different types of journeys in London, exploring their prices, popularity, and trends over time. The dataset contains information on millions of journeys taken via different transport modes such as Bus, Underground, Overground, Tram, and Emirates Airline. The goal is to derive insights from the data, visualize key trends, and provide useful statistics.

## 📂 Dataset
- The dataset used is `tfl_journeys_final.csv`.
- It includes information on the number of journeys (in millions), transport type, month, year, and other relevant details.
- Missing values were handled using the `dropna()` function.
- A synthetic price column was added using random uniform values based on transport type.

## 📊 Analysis & Visualizations

### 1️⃣ Relationship Between Number of Journeys and Price
- A scatter plot was created to analyze the relationship between the number of journeys and the assigned price.
- **Graph:**
  ![Scatter Plot](https://github.com/alvaroperez1804/London_transportation/blob/master/Scatter_plot.png)

### 2️⃣ Most Popular Transport Types
- The dataset was grouped by `journey_type` to find the most used transport modes in terms of total journeys.
- **Graph:**
  ![Most Popular Transport](IMAGENES%20DE%20PROYECTO%20SQL/MOST%20POPULAR.PNG)

### 3️⃣ Emirates Airline Popularity Over Time
- The project identifies the top 5 months and years where the Emirates Airline transport mode was most popular.
- The results were sorted in descending order to show peak demand periods.
- **Graph:**
  ![Emirates Popularity](https://github.com/alvaroperez1804/London_transportation/blob/master/emirates_.png)

### 4️⃣ Least Popular Years for Underground & DLR
- The dataset was filtered to examine the years where the `Underground & DLR` transport mode had the lowest number of journeys.
- **Graph:**
  ![Underground Least Popular](https://github.com/alvaroperez1804/London_transportation/blob/master/less.png)

## 🛠 Technologies Used
- **Python** (Pandas, Matplotlib, Seaborn, NumPy)
- **Git & GitHub** for version control
- **Jupyter Notebook / VS Code** for coding and analysis

## 📌 Key Findings
- **Buses** have the lowest average price, while **Emirates Airline** is the most expensive mode of transport.
- The **Underground & DLR** is among the most used modes of transport.
- The Emirates Airline had peak usage during certain months, which may indicate seasonal trends or special events.
- Some years had a significant decline in the use of Underground & DLR, possibly due to economic factors or external events.

## 📎 How to Use the Code
1. Clone this repository:
   ```sh
   git clone https://github.com/alvaroperez1804/London_transportation.git
   ```
2. Install required dependencies:
   ```sh
   pip install pandas matplotlib seaborn numpy
   ```
3. Run the Python script to generate visualizations and insights.

## 📬 Contact
For any questions or suggestions, feel free to reach out:
- **GitHub:** [alvaroperez1804](https://github.com/alvaroperez1804)
- **Email:** your.email@example.com

