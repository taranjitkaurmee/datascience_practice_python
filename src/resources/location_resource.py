from flask_restful import Resource, reqparse
from src.services.location_service import LocationService
from src.utility.decorators import log_request


class LocationResource(Resource):
    """
    Represents the RESTful API resource for managing location information.

    Endpoints:
        GET /api/location/<int:location_id>:
            Retrieves information about a specific location.
        POST /api/location:
            Creates a new location.
        PUT /api/location/<int:location_id>:
            Updates information about a specific location.
        DELETE /api/location/<int:location_id>:
            Deletes a specific location.

    Methods:
        get(self, location_id=None):
            Retrieves information about a specific location or a list of all locations.

        post(self):
            Creates a new location based on the provided information.

        put(self, location_id):
            Updates information about a specific location.

        delete(self, location_id):
            Deletes a specific location.

    Request Parameters:
        location_id (int, optional): The unique identifier of the location (for GET, PUT, and DELETE operations).

    Request JSON Payload (for POST and PUT operations):
        {
            "city": "City Name",
            "state": "State Name",
            "country": "Country Name"
        }

    Returns:
        dict: A JSON response containing the result of the corresponding operation.
    """

    @log_request
    def get(self, location_id=None):
        try:
            return LocationService.get_location(location_id)
        except Exception as e:
            return {"message": str(e)}, 404

    @log_request
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('city', type=str, required=True, help='city is required')
            parser.add_argument('state', type=str, required=True, help='state is required')
            parser.add_argument('country', type=str, required=True, help='country is required')
            args = parser.parse_args()

            return LocationService.create_location(city=args['city'], state=args['state'], country=args['country'])
        except Exception as e:
            return {"message": str(e)}, 400

    @log_request
    def put(self, location_id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('city', type=str, required=True, help='city is required')
            parser.add_argument('state', type=str, required=True, help='state is required')
            parser.add_argument('country', type=str, required=True, help='country is required')
            args = parser.parse_args()

            return LocationService.update_location(location_id=location_id, city=args['city'], state=args['state'],
                                                   country=args['country'])
        except Exception as e:
            return {"message": str(e)}, 404

    @log_request
    def delete(self, location_id):
        try:
            return LocationService.delete_location(location_id)
        except Exception as e:
            return {"message": str(e)}, 404
