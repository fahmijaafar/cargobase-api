import logging
import app_config
from fastapi import FastAPI
from routers import resources
from db_init import Base, engine

# create the database schema
Base.metadata.create_all(engine)

# remove existing log handlers if any and instantiate logging config
root = logging.getLogger()
if root.handlers:
    for handler in root.handlers:
        root.removeHandler(handler)
logging.basicConfig(level=app_config.settings.log_level)

# create the application and config
logging.debug("Initializing FastAPI instance.")
app_wrapper = FastAPI()
app = FastAPI(title="Cargobase Technical Assessment",
              description="Web Scraping Flight Information Data",
              version="0.0.1")

# include routers for the app

app.include_router(resources.router)