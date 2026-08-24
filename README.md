# 📊 Data Analytics & Data Engineering Learning Path

Welcome to the **Data Analytics & Data Engineering** repository! This repository serves as a structured repository and portfolio containing Python scripts, exploratory data analysis (EDA) notebooks, algorithmic exercises, data pipelines, and real-world assignments.

---

## 📁 Repository Structure

```text
├── assignment1/             # Assignment 1: Student Data Analysis
│   ├── Assignmet1.ipynb     # Jupyter Notebook with student dataset exploration
│   └── students.csv         # Student performance and demographic dataset
│
├── assignmnet2/             # Assignment 2: Global University Rankings Analysis
│   ├── assignment2.ipynb    # Interactive notebook for university data exploration
│   ├── solve.py             # Data cleaning, transformation, and statistical questions
│   └── university.csv       # World university rankings dataset
│
├── data-engineer/           # Data Engineering & Infrastructure
│   └── docker/
│       └── pipeline.py      # Parameterized data processing pipeline
│
├── exercises/               # Algorithmic Python Exercises & Practice
│   ├── count_unique_values.py # Count unique elements in collections
│   ├── fibonaci_series.py     # Fibonacci sequence generation
│   ├── palindrome_num.py      # Palindrome number check
│   ├── reverse_string.py      # String reversal algorithms
│   └── sum_digits.py          # Sum of digits computation
│
├── functions/               # Python Functions & Reusable Logic
│   └── fun.py               # Function definitions, parameters, and return patterns
│
├── jupyter/                 # ETL & Exploratory Data Analysis Notebooks
│   ├── ETL script.ipynb     # Extract, Transform, Load (ETL) pipeline notebook
│   ├── script.ipynb         # Data analysis and visualization experiments
│   └── jobs.xlsx            # Job postings and market analysis dataset
│
├── list/                    # Python Lists & Operations
│   └── lists.py             # List manipulation, methods, and slicing
│
├── loops/                   # Control Flow & Iterations
│   └── loops.py             # For loops, while loops, and list comprehensions
│
├── oop/                     # Object-Oriented Programming (OOP)
│   └── oop.py               # Classes, objects, methods, and encapsulated logic
│
├── sets/                    # Python Sets & Set Theory
│   └── sets.py              # Set operations, uniqueness, intersections & unions
│
├── tuples/                  # Python Tuples
│   └── tuples.py            # Immutability, tuple unpacking, and indexing
│
├── .gitignore               # Ignored files (Jupyter checkpoints, cache, venvs)
└── README.md                # Project documentation and roadmap
```

---

## 📖 Module Details & Documentation

### 1. 🎓 Assignments (`assignment1/` & `assignmnet2/`)
- **Assignment 1 (`assignment1/`)**:
  - Focuses on exploratory data analysis of student performance using `students.csv`.
  - Investigates correlations, distributions, and demographic statistics using Pandas and visualizations.
- **Assignment 2 (`assignmnet2/`)**:
  - Analyzes the `university.csv` dataset containing world university rankings.
  - **Key tasks implemented in [solve.py](file:///c:/Users/bons/Documents/data-analytics/assignmnet2/solve.py)**:
    - Data cleaning: parsing string values (commas, percentages, female-to-male ratios).
    - University & country distribution across top 100 rankings.
    - Identification of top institutions with >50% international student body and female representation.

---

### 2. ⚙️ Data Engineering & Pipelines (`data-engineer/`)
- **[pipeline.py](file:///c:/Users/bons/Documents/data-analytics/data-engineer/docker/pipeline.py)**:
  - Demonstrates command-line parameterized data processing with `sys.argv`.
  - Integrates with Pandas to generate structured DataFrames for daily ingestion workflows.
  - Designed for containerized batch execution (Docker ready).

---

### 3. 📓 ETL & Data Analytics Notebooks (`jupyter/`)
- **ETL Script (`jupyter/ETL script.ipynb`)**:
  - Implements end-to-end Extract, Transform, and Load (ETL) operations on tabular datasets.
- **Jobs Analysis (`jupyter/jobs.xlsx` & `jupyter/script.ipynb`)**:
  - Analyzes employment trends, job roles, salary bands, and skill distributions from Excel data.

---

### 4. 🧠 Python Foundations & Exercises (`exercises/`, `oop/`, `functions/`, etc.)
- **`exercises/`**: Algorithmic problem solving focusing on time/space complexity:
  - Fibonacci Series calculation
  - Palindrome checking
  - String manipulation and reversal
  - Digit summation
  - Unique value frequency counting
- **Data Structures & OOP**:
  - `list/`, `tuples/`, `sets/`, `loops/`, `functions/`: Mastering idiomatic Python programming.
  - `oop/oop.py`: Class-based design and custom utility classes (e.g. `MaxNumberFinder`).

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.9+ installed.

### Installation
Clone this repository and install the recommended dependencies:

```bash
git clone https://github.com/bonssss/Data_Analytics_Path.git
cd Data_Analytics_Path
```

Install core libraries:
```bash
pip install pandas numpy openpyxl jupyter matplotlib seaborn
```

---

## 💻 Running the Code

### 1. Run Data Engineering Pipeline
Pass the target day integer as a command-line argument:
```bash
python data-engineer/docker/pipeline.py 10
```

### 2. Run Assignment 2 University Analysis
```bash
cd assignmnet2
python solve.py
```

### 3. Run Practice Exercises
```bash
python exercises/fibonaci_series.py
python exercises/palindrome_num.py
python oop/oop.py
```

### 4. Launch Jupyter Notebooks
```bash
jupyter notebook
```
Navigate to `jupyter/` or `assignment1/` to run the interactive notebooks.

---

## 🛠️ Tech Stack & Tools
- **Language**: Python 3
- **Data Processing**: Pandas, NumPy
- **File Formats**: CSV, Excel (`.xlsx`), JSON
- **Environment**: Jupyter Notebooks, VS Code / Antigravity IDE
- **Version Control**: Git & GitHub
- **Containerization**: Docker (Pipeline workflows)

---

## 👤 Author
- **GitHub**: [@bonssss](https://github.com/bonssss)
