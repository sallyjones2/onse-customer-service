from behave import when, then, given


@when('I update the surname to "{new_surname}" of customer with ID "{customer_id:d}"')
def update_surname(context, new_surname, customer_id):
    response = context.web_client.put(
        '/customers/',
        json={'customer_id': customer_id, 'new_surname': new_surname})
    print(response.get_json())
    assert response.status_code == 202, response.status_code

