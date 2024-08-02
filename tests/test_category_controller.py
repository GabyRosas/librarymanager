import pytest
from unittest.mock import patch, MagicMock
from src.controllers.CategoryController import CategoryController

class TestCategoryController:
    @pytest.fixture
    def category_controller(self):
        with patch('src.controllers.CategoryController.CategoryModel') as MockCategoryModel:
            mock_category_model = MockCategoryModel.return_value
            controller = CategoryController()
            return controller, mock_category_model

    def test_create_category_success(self, category_controller):
        controller, mock_category_model = category_controller
        data = {'category_name': 'TestCategory'}

        mock_category_model.category_exists.return_value = False
        mock_category_model.create.return_value = 1
        result = controller.create_category(data)
        mock_category_model.category_exists.assert_called_once_with(data)
        mock_category_model.create.assert_called_once_with(mock_category_model.table, data)
        assert result == 1

    def test_create_category_already_exists(self, category_controller):
        controller, mock_category_model = category_controller
        data = {'category_name': 'TestCategory'}

        mock_category_model.category_exists.return_value = True
        result = controller.create_category(data)
        mock_category_model.category_exists.assert_called_once_with(data)
        mock_category_model.create.assert_not_called()
        assert result == 0