from flask import jsonify, Blueprint, current_app, request

from customer_service.model import commands
from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound

customers = Blueprint('customers', __name__, url_prefix='/customers/')


@customers.route('/<string:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer_repository = current_app.customer_repository
    try:
        customer = commands.get_customer(
            customer_id=int(customer_id),
            customer_repository=customer_repository)

        return jsonify(customerId=str(customer.customer_id),
                       firstName=customer.first_name,
                       surname=customer.surname)
    except CustomerNotFound:
        return jsonify({
            'message': 'Not found'
        }), 404


@customers.route('/', methods=['POST'])
def create_customer():
    customer_repository = current_app.customer_repository
    body = request.get_json()

    customer = Customer(first_name=body['firstName'],
                        surname=body['surname'])

    commands.create_customer(
        customer=customer,
        customer_repository=customer_repository)

    return jsonify(customerId=customer.customer_id,
                   firstName=customer.first_name,
                   surname=customer.surname), 201