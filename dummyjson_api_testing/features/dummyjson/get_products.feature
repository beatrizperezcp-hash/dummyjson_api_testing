Feature: GET /products

  @get_products
  Scenario: GET /products
    Given prepare uri from the file dummyson_api and the endpoint /products
    Then prepare header with the following data
      | key       | value                                |
      | x-api-key | configuration.dummyson_api.x-api-key |
    And performa method and validate the status code 200
    And verify the key products with the following conditions
      | key      | condition | value |
      | id       | >         | 0     |
      | title    | not       | any   |
      | price    | >         | 0     |
      | stock    | >=        | 0     |
      | category | not       | Null  |
    Then validate id is not duplicated