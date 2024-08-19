from unittest.mock import patch
import pytest
from src.controllers.CategoryController import CategoryController


class TestCategoryController:
    @pytest.fixture
    def category_controller(self):
        with patch('src.controllers.CategoryController.CategoryModel') as MockCategoryModel:
            mock_category_model = MockCategoryModel.return_value
            controller = CategoryController()
            return controller, mock_category_model

    """Feature: Crear categoría
    
      Scenario: Crear una categoría con éxito
        Given un controlador de categorías
        And una categoría con nombre "TestCategory" que no existe
        When se intenta crear la categoría
        Then la categoría debería ser creada con éxito
        And el método `category_exists` debería ser llamado una vez con los datos de la categoría
        And el método `create` debería ser llamado una vez con la tabla de la categoría y los datos
        And el resultado debería ser 1"""
    def test_create_category_success(self, category_controller):
        controller, mock_category_model = category_controller
        data = {'category_name': 'TestCategory'}

        mock_category_model.category_exists.return_value = False
        mock_category_model.create.return_value = 1
        result = controller.create_category(data)
        mock_category_model.category_exists.assert_called_once_with(data)
        mock_category_model.create.assert_called_once_with(mock_category_model.table, data)
        assert result == 1
        """
      Scenario: Intentar crear una categoría que ya existe
        Given un controlador de categorías
        And una categoría con nombre "TestCategory" que ya existe
        When se intenta crear la categoría
        Then la categoría no debería ser creada
        And el método `category_exists` debería ser llamado una vez con los datos de la categoría
        And el método `create` no debería ser llamado
        And el resultado debería ser 0"""

    def test_create_category_already_exists(self, category_controller):
        controller, mock_category_model = category_controller
        data = {'category_name': 'TestCategory'}

        mock_category_model.category_exists.return_value = True
        result = controller.create_category(data)
        mock_category_model.category_exists.assert_called_once_with(data)
        mock_category_model.create.assert_not_called()
        assert result == 0

