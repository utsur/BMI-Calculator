# BMI Calculator Core Logic
import re

def calculate_bmi(weight, height):
    """
    Calculate BMI using weight in kg and height in meters.
    Args:    weight (float): Weight in kilograms, height (float): Height in meters
    Returns: float: Calculated BMI value
    """
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive values.")
    
    return weight / (height ** 2)

def get_bmi_category(bmi):
    """
    Determine the BMI category based on the BMI value.
    Args:    bmi (float): BMI value
    Returns: str: BMI category (Underweight, Normal weight, Overweight, or Obesity)
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def get_category_color(category):
    """
    Get the color code for a BMI category.
    Args:    category (str): BMI category
    Returns: str: Hex color code
    """
    if category == "Underweight":
        return "#2196F3"  # Blue
    elif category == "Normal weight":
        return "#4CAF50"  # Green
    elif category == "Overweight":
        return "#FF9800"  # Orange
    else:
        return "#F44336"  # Red

def validate_input(weight_str, height_str):
    """
    Validate weight and height input strings.
    Args: weight_str (str): Weight as string, height_str (str): Height as string
    Returns:
        tuple: (is_valid, error_message, weight, height)
            - is_valid (bool): True if input is valid, False otherwise
            - error_message (str): Error message if input is invalid, empty string otherwise
            - weight (float): Converted weight value if valid, None otherwise
            - height (float): Converted height value if valid, None otherwise
    """
    # Check if inputs are empty
    if not weight_str or not height_str:
        return False, "Please enter both weight and height.", None, None
    
    # Normalize decimal separator
    weight_str = weight_str.replace(',', '.')
    height_str = height_str.replace(',', '.')
    
    # Check if inputs are valid numbers
    weight_pattern = r'^\d+(\.\d+)?$'
    height_pattern = r'^\d+(\.\d+)?$'
    
    if not re.match(weight_pattern, weight_str):
        return False, "Please enter a valid weight.", None, None
    
    if not re.match(height_pattern, height_str):
        return False, "Please enter a valid height.", None, None
    
    # Convert to float
    weight = float(weight_str)
    height = float(height_str)
    
    # Check for valid ranges
    if weight <= 0 or height <= 0:
        return False, "Weight and height must be positive values.", None, None
    
    return True, "", weight, height