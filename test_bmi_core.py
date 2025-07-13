# Test script for BMI calculator core functionality
from bmi_calculator_core import calculate_bmi, get_bmi_category, get_category_color, validate_input

def test_calculate_bmi():
    """Test the BMI calculation function"""
    # Test normal case
    assert round(calculate_bmi(70, 1.75), 2) == 22.86
    
    # Test edge cases
    try:
        calculate_bmi(0, 1.75)  # Should raise ValueError
        print("FAIL: calculate_bmi should raise ValueError for weight=0")
    except ValueError:
        print("PASS: calculate_bmi correctly raises ValueError for weight=0")
    
    try:
        calculate_bmi(70, 0)  # Should raise ValueError
        print("FAIL: calculate_bmi should raise ValueError for height=0")
    except ValueError:
        print("PASS: calculate_bmi correctly raises ValueError for height=0")

def test_get_bmi_category():
    """Test the BMI category determination function"""
    assert get_bmi_category(17) == "Underweight"
    assert get_bmi_category(18.5) == "Normal weight"
    assert get_bmi_category(24) == "Normal weight"
    assert get_bmi_category(25) == "Overweight"
    assert get_bmi_category(29) == "Overweight"
    assert get_bmi_category(30) == "Obesity"
    assert get_bmi_category(35) == "Obesity"
    print("PASS: get_bmi_category correctly determines all BMI categories")

def test_get_category_color():
    """Test the category color function"""
    assert get_category_color("Underweight") == "#2196F3"
    assert get_category_color("Normal weight") == "#4CAF50"
    assert get_category_color("Overweight") == "#FF9800"
    assert get_category_color("Obesity") == "#F44336"
    print("PASS: get_category_color correctly returns colors for all categories")

def test_validate_input():
    """Test the input validation function"""
    # Valid inputs
    is_valid, error, weight, height = validate_input("70", "1.75")
    assert is_valid == True
    assert error == ""
    assert weight == 70
    assert height == 1.75
    
    # Test with comma as decimal separator
    is_valid, error, weight, height = validate_input("70,5", "1,75")
    assert is_valid == True
    assert error == ""
    assert weight == 70.5
    assert height == 1.75
    
    # Empty inputs
    is_valid, error, weight, height = validate_input("", "1.75")
    assert is_valid == False
    assert "both weight and height" in error
    
    # Invalid number format
    is_valid, error, weight, height = validate_input("abc", "1.75")
    assert is_valid == False
    assert "valid weight" in error
    
    # Zero or negative values
    is_valid, error, weight, height = validate_input("0", "1.75")
    assert is_valid == False
    assert "positive values" in error
    
    print("PASS: validate_input correctly validates all test cases")

if __name__ == "__main__":
    print("Testing BMI calculator core functionality...")
    test_calculate_bmi()
    test_get_bmi_category()
    test_get_category_color()
    test_validate_input()
    print("All tests completed!")