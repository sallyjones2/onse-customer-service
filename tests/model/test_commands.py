import pytest

from customer_service.model import commands
from customer_service.model.customer import Customer
from customer_service.model.errors import CustomerNotFound


def test_get_customer_when_customer_does_not_exist(customer_repository):
    with pytest.raises(CustomerNotFound):
        commands.get_customer(customer_id=99999,
                              customer_repository=customer_repository)


def test_get_customer(customer_repository):
    customer = Customer(customer_id=1234, first_name='Gene', surname='Kim')
    customer_repository.store(customer)

    result = commands.get_customer(customer_id=1234,
                                   customer_repository=customer_repository)

    assert result is customer


def test_create_customer(customer_repository):
    customer = Customer(first_name='Nicole', surname='Forsgren')

    commands.create_customer(customer=customer,
                             customer_repository=customer_repository)

    stored_customer = customer_repository.fetch_by_id(customer.customer_id)

    assert stored_customer.first_name == 'Nicole'
    assert stored_customer.surname == 'Forsgren'


def test_update_surname(customer_repository):
    customer_id = 12345678
    new_surname = "Hello"
    customer = Customer(customer_id=customer_id, first_name='Gene',
                        surname='Kim')
    customer_repository.store(customer)

    commands.update_surname(customer_id=customer_id, new_surname=new_surname,
                            customer_repository=customer_repository)

    customer = customer_repository.fetch_by_id(customer_id)
    assert customer.surname == new_surname
