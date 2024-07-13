from fastapi import APIRouter, Query
from dependencies.flightstats import get_flights_info

# create a router object
router = APIRouter(
    prefix="/api"
)

#create an endpoint for fetching flight info
@router.get(
    "/search",
    summary="query flight info",
    status_code=200,
)
async def search_flight(
    airline_code: str = Query(
        description="query string",
        example="AK",
    ),
    airline_number: str = Query(
        example="11"
    ),
    departure_date: str = Query(
        example="2022-01-01"
    )
):
    result = await get_flights_info(
        airline_code, airline_number, departure_date
    )
    return result