# Sharesansar Data Pipeline 🚀

An end-to-end data engineering and analytics backend system that scrapes live Nepalese stock market data from Sharesansar, processes it using Pandas, stores it in an SQLite database using SQLAlchemy ORM, and serves it through a FastAPI REST API.

---

## 🏗️ Architecture Overview

The project follows a layered ETL (Extract, Transform, Load) and REST API architecture.

### 1. Data Extraction (`extractor.py`)

* Scrapes live stock market data from Sharesansar using Requests and BeautifulSoup.
* Extracts raw market table rows for further processing.

### 2. Data Transformation (`transformer.py`)

* Converts raw scraped data into a structured Pandas DataFrame.
* Cleans and validates market values.
* Performs type conversion and handles missing values.

### 3. Market Analytics (`analyzer.py`)

Generates market insights including:

* 📈 Top Gainers
* 📉 Top Losers
* 💧 Highest Trading Volume Stocks

### 4. Database Layer (`database.py`, `models.py`, `loader.py`)

* Uses SQLite for persistent storage.
* Uses SQLAlchemy ORM for database abstraction.
* Loads transformed market data into the database through transactional sessions.

### 5. API Layer (`schema.py`, `main.py`)

* Uses FastAPI to expose REST API endpoints.
* Uses Pydantic schemas for response validation and serialization.
* Provides live market analytics through API endpoints.

---

## 📊 Project Architecture

```text
                    Sharesansar
                          │
                          ▼
                   extractor.py
                          │
                          ▼
                      raw_rows
                          │
                          ▼
                  transformer.py
                          │
                          ▼
                     cleaned_df
                      ╱      ╲
                     ╱        ╲
                    ▼          ▼
              analyzer.py   loader.py
                                │
                                ▼
                           SQLite DB
                                │
                                ▼
                            models.py
                                │
                                ▼
                            schema.py
                                │
                                ▼
                             main.py
                                │
                                ▼
                         Browser / API
```

---

## 🧠 Concepts Implemented

* ETL (Extract, Transform, Load) Pipeline
* Web Scraping
* Data Cleaning and Validation
* Object Relational Mapping (ORM)
* Database Transactions
* REST API Development
* Dependency Injection
* API Serialization
* Persistent Storage
* Backend System Architecture

---

## 🛠️ Technology Stack

| Category        | Technology               |
| --------------- | ------------------------ |
| Language        | Python 3.13.5            |
| Data Processing | Pandas, NumPy            |
| Web Scraping    | Requests, BeautifulSoup4 |
| Database        | SQLite                   |
| ORM             | SQLAlchemy               |
| API Framework   | FastAPI                  |
| Validation      | Pydantic                 |
| Server          | Uvicorn                  |

---

## 🚀 API Endpoints

| Endpoint               | Description            |
| ---------------------- | ---------------------- |
| `/api/market`          | Fetch all market data  |
| `/api/market/gainers`  | Fetch top 5 gainers    |
| `/api/market/losers`   | Fetch top 5 losers     |
| `/api/market/{symbol}` | Fetch a specific stock |

---

## 🚀 Running the Project

### Clone the Repository

```bash
git clone https://github.com/AakashKhanal-10/Sharesansar-Data-Pipeline
cd sharesansar-data-pipeline
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Load Market Data into Database

```bash
python loader.py
```

### Start the FastAPI Server

```bash
python -m uvicorn main:app --reload
```

Open the interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 🎯 Version 1 Features

* ✅ Live Sharesansar market data scraping
* ✅ ETL pipeline architecture
* ✅ Market analytics engine
* ✅ SQLite persistent storage
* ✅ SQLAlchemy ORM integration
* ✅ FastAPI REST API
* ✅ Pydantic schema validation
* ✅ Interactive Swagger documentation

---

## 🔮 Planned Features for Version 2

* Automated scheduled data collection
* Historical market data storage
* Interactive dashboards
* Data visualization and charting
* Technical indicators
* Portfolio analytics
* AI-powered market insights
* Docker containerization
* Cloud deployment

---

## 🐍 Python Version

Developed and tested with:

```text
Python 3.13.5
```

---

## 📄 License

This project is developed for educational, learning, and portfolio purposes.
