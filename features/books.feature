Feature: Gestión de inventario

  Scenario: Agregar libro
    Given la base de datos está lista
    When añado un libro
    Then el libro se añade correctamente

