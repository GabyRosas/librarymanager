from unittest.mock import MagicMock

def test_mock_function():
    mock_func = MagicMock()
    mock_func.return_value = 3
    assert mock_func() == 3

if __name__ == "__main__":
    test_mock_function()
    print("Mock is working correctly")