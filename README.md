# hr-analytics-data-cleaning-dashboard
End-to-end HR Analytics project using Python (Pandas) and Excel featuring data cleaning, feature engineering, analysis, pivot tables, and an interactive dashboard

This project transforms a messy employee dataset into clean, analysis-ready data and presents key business insights through an interactive Excel dashboard.

---

## Project Overview

The project follows a complete data analytics workflow:

- Import raw HR dataset
- Explore data structure
- Handle missing values
- Clean inconsistent text
- Remove duplicate records
- Convert and process dates
- Create new analytical features
- Filter and sort employee records
- Perform aggregations
- Generate Pivot Tables
- Export cleaned dataset
- Build an interactive HR Analytics Dashboard in Excel

---

## Dataset

The dataset contains over **10,000 employee records** with attributes such as:

- Employee Name
- Age
- Salary
- Performance Score
- City
- Department
- Joining Date
- Email

The original dataset intentionally contains:

- Missing values
- Duplicate records
- Inconsistent text formatting
- Invalid dates
- Unstructured data

---

## Project Workflow

### 1. Data Exploration

- Dataset preview
- Shape
- Data types
- Summary statistics
- Missing value analysis

---

### 2. Data Cleaning

- Filled missing values
- Converted data types
- Standardized text formatting
- Removed duplicate records
- Reset index

---

### 3. Feature Engineering

Created new columns including:

- Year
- Month
- Day
- Month Name
- Day Name
- Days Since Joined

---

### 4. Business Calculations

Calculated:

- Bonus
- Tax
- Net Salary

Generated:

- Salary Category
- Performance Grade
- Age Category

---

### 5. Data Analysis

Performed analysis including:

- Average Salary
- Maximum Salary
- Minimum Salary
- Average Performance
- Employee Count

Grouped data by:

- Department
- City

---

### 6. Pivot Tables

Created pivot tables for:

- Average Salary by Department and City
- Employee Count by Department
- Average Department Performance

---

### 7. Dashboard

An interactive Excel dashboard was created to visualize HR insights, making the data easier to interpret for business decision-making.

---

## Technologies Used

- Python
- Pandas
- Microsoft Excel
- Pivot Tables
- Data Cleaning
- Data Analysis

---

## Skills Demonstrated

- Data Cleaning
- Data Wrangling
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Business Analytics
- HR Analytics
- Data Transformation
- Pivot Table Analysis
- Dashboard Development
- Python Programming

---

## Project Structure

```
HR-Analytics-Data-Cleaning-Dashboard/
│
├── data_analysis.py
├── industry_employee_messy_dataset_10200_rows.xlsx
├── Cleaned Data.xlsx
├── HR_Analytics_Dashboard.xlsx
├── README.md
└── screenshots/
    ├── dashboard.png
    ├── dataset.png
    └── pivot_tables.png
```

---

## Future Improvements

- Build an interactive Power BI dashboard
- Automate reporting with Python
- Create visualizations using Matplotlib and Seaborn
- Add predictive HR analytics
- Deploy as a Streamlit web application

---

## Author

**Muhammad Salar Shah**

Aspiring Data Analyst | Financial Technology Student | Python & Excel Enthusiast

This repository is part of my portfolio showcasing practical data analytics and business intelligence projects.
