---

# 📊 Streamlit Data Cleaning App

An interactive data exploration and visualization web application built with **Python** and **Streamlit**.

This app allows users to upload CSV or Excel files and instantly perform data previewing, summarization, and visualization — without writing a single line of code.

---

## 🚀 Live Demo

App Link: https://datacleaning-app-g6ehacrkvn6mxp8qfvfpra.streamlit.app/

---

## 📌 Project Overview

The **Data Cleaning App** enables users to:

* Upload CSV or Excel datasets
* View dataset structure and statistics
* Detect missing and duplicate records
* Explore numerical and categorical summaries
* Create interactive visualizations

This project demonstrates practical skills in:

* Data handling using **Pandas**
* Data visualization using **Matplotlib**
* Building interactive dashboards using **Streamlit**
* Creating user-friendly analytical tools

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **NumPy**
* **Matplotlib**

---

## ✨ Features

### 📁 1. File Upload Support

* Upload `.csv`, `.xlsx`, and `.xls` files
* Automatic format detection
* Error handling for unsupported formats

---

### 📊 2. Data Overview

* Number of rows and columns
* Total missing values
* Duplicate record detection
* Dataset structure (`data.info()`)

---

### 📃 3. Statistical Summary

* Numerical feature summary (`mean`, `std`, `min`, `max`, etc.)
* Non-numerical feature summary (categorical insights)
* Boolean column handling

---

### ✏️ 4. Column Selection

* Interactive multi-column selection
* Preview selected dataset columns

---

### 📈 5. Data Visualization

Users can generate:

* 📈 Line Chart
* 🔵 Scatter Plot
* 📊 Bar Chart
* 📶 Histogram (Numerical Columns Only)
* 📦 Box Plot (Numerical Columns Only)

All charts are dynamically generated based on selected X and Y axes.

---

## 🖥️ How To Run Locally

### 1️⃣ Clone The Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a requirements file yet, install manually:

```bash
pip install streamlit pandas numpy matplotlib openpyxl
```

### 3️⃣ Run The Application

```bash
streamlit run app.py
```
---

## 🎯 Use Cases

* Quick exploratory data analysis (EDA)
* Academic projects
* Business dataset inspection
* Data analytics portfolio project
* Beginner-friendly analytics tool
