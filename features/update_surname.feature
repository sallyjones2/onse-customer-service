Feature: Update surname

  Scenario: Update customer surname
    Given customer "Chardonnay Smith" with ID "12345678" exists
    When I update the surname to "Brown" of customer with ID "12345678"
    And I fetch customer "12345678"
    Then I should see customer "Chardonnay Brown"
