import requests
from datetime import datetime
from models.flight import Flight
from db_init import session
from helpers.scraper import scrape_essential_data
from models import error_message
import app_config

async def get_flights_info(airline_code, airline_number, departure_date):

    # check existing records in db and if its final, if not fetch from web
    flight = session.query(Flight).filter_by(airline_code=airline_code, airline_number=airline_number, departure_date=departure_date).first()

    if flight and flight.flight_data["flightNote"]["final"] == True:
        result = flight.flight_data
        session.close()
    else:
        # getting latest flight data from website
        try:
            flightstats_base_url = app_config.settings.flightstats_base_url
            full_url = flightstats_base_url + f"{airline_code}/{airline_number}"
            departure_datetime = datetime.strptime(departure_date, "%Y-%m-%d")
            url_params = {
                "year": departure_datetime.year,
                "month": departure_datetime.month,
                "day": departure_datetime.day
            }
            flight_data = requests.get(full_url, params=url_params, verify=False)

            # massage data for essential value
            result = scrape_essential_data(flight_data)
            if result:
                # insert essential flight data into db
                flight = Flight(airline_code=airline_code, airline_number=airline_number, departure_date=departure_date, flight_data=result)
                session.add(flight)
                session.commit()
                session.close()
            else:
                result = {
                    "Error": "JSON Error",
                    "Description": error_message.ScrapingErrorMessage
                }
        except requests.exceptions.RequestException:
            result = {
                    "Error": "HTTP Connection Error",
                    "Description": error_message.HTTPConnectionErrorMessage
                }
    return result