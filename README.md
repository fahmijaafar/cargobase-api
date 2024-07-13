# Cargobase Assessment for Integration Engineer

## Package used:
- fastAPI for API Framework
- SQLite for Database and SQLAlchemy for ORM
- BeautifulSoup for Data Scraping
- Pydantic for Data Validation
- Pytest for Testing

## Clone the repository to your workspace and do the following steps for running the applications:

1. Activating virtual environment
```
python -m venv venv

source venv/bin/activate OR .\venv\Scripts\activate.ps1 if you're on windows
```
2. Running the application
```
pip install -r requirements.txt

python -m uvicorn main:app
```
3. Testing the application
```
pytest test.py
```

Thank you for taking your time to review the assessment

Disclaimer: As the question was not clear for what is essential flight data, I've put all information that could be retreived for it, which makes it long, and as I'm unable to find the exact possible structure of the json object, I've not created the class for response object to validate.
