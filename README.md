# FastAPI Async Task Manager & Scraper Service

A production-ready, modular asynchronous backend built with **FastAPI** designed for task creation, background execution, and state persistence.

##

![Python](https://img.shields.io/badge/Python-3.11-blue)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)

## 🚀 Key Features

- **Asynchronous Execution:** Non-blocking API responses leveraging FastAPI's `BackgroundTasks`.
- **Modular Architecture:** Decoupled database connection logic (`database.py`) and API routing (`main.py`).
- **Data Persistence:** SQLite-backed status tracking (`pending`, `processing`, `completed`).
- **Strict Data Validation:** Request body parsing and validation powered by **Pydantic**.

## 🛠 Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Uvicorn** (ASGI server)
* **SQLite3**
* **Pydantic**

## 📦 Quick Start

### 1. Clone the repository & set up environment

```bash
git clone [https://github.com/owiga/FastAPI_Structure.git](https://github.com/owiga/FastAPI_Structure.git)
cd FastAPI_Structure

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/macOS
# venv\Scripts\activate   # For Windows

# Install dependencies
pip install fastapi uvicorn
