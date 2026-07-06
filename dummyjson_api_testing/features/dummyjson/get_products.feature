Feature: GET /products

  @get_products
  Scenario: GET /products
    Given prepare uri from the file dummyson_api and the endpoint /products
    Then prepare header with the following data
      | key        | value                                 |
      | x-api-key  | configuration.dummyson_api.x-api-key  |
    And performance method and validate the status code 200