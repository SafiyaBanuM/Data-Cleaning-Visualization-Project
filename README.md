# Data-Cleaning-Visualization-Project
##  Project Overview
This project was completed as part of the **Thiranex Data Science Internship**.

The objective of the project is to clean, analyze, and visualize a real-world dataset using Python. The project demonstrates essential data preprocessing techniques and multiple data visualization methods to extract meaningful business insights.

---

## Dataset

**Dataset Name:** Maven Fuzzy Factory - Orders Dataset

The dataset contains information about:

- Order ID
- Order Date
- Website Session ID
- User ID
- Product ID
- Items Purchased
- Product Price
- Cost of Goods Sold (COGS)

---

##  Objectives

- Load the dataset using Pandas
- Explore the dataset
- Check for missing values
- Check for duplicate records
- Convert data types
- Detect outliers
- Create meaningful visualizations
- Generate business insights

---

##  Technologies Used

- Python
- Pandas
- Matplotlib

---

##  Data Cleaning

The following data cleaning steps were performed:

- Checked dataset structure
- Verified column names
- Checked for missing values
- Checked duplicate records
- Converted the `created_at` column from Object to Datetime format
- Detected outliers using Box Plot

---

##  Visualizations

The following visualization techniques were used:

-  Box Plot
-  Histogram
-  Bar Chart
-  Pie Chart
-  Scatter Plot
-  Items Purchased Bar Chart

---

##  Key Insights

- No missing values were found in the dataset.
- No duplicate records were identified.
- Product ID 1 received the highest number of orders.
- Most customer orders were placed at the \$49.99 price point.
- Product prices showed a positive relationship with Cost of Goods Sold (COGS).
- Most customers purchased a single item per order.

---

##  Project Screenshots

The generated visualizations are available in the **screenshots** folder.

---

##  How to Run the Project

1. Clone this repository.

```
git clone https://github.com/Safiya23092006/Data-Cleaning-Visualization-Project.git
```

2. Install the required libraries.

```
pip install pandas matplotlib
```

3. Run the Python script.

```
python data-visualization-project.py
```

---

##  Project Structure

```
Data-Cleaning-Visualization-Project/
│
├── interntask1.py
├── README.md
├── screenshots/
│   ├── boxplot.png
│   ├── histogram.png
│   ├── barchart.png
│   ├── piechart.png
│   ├── scatterplot.png
│   └── items_purchased.png
└── dataset/
    └── orders.csv
```

---

##  Author

**Safiya Banu M**

Second Year Computer Science Engineering Student

Completed as part of the **Thiranex Data Science Internship**.

---
