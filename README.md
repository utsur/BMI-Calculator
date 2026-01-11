# BMI Calculator

A simple BMI (Body Mass Index) calculator with a graphical user interface.

## Project Structure

The project is organized following the separation of concerns principle:

- **BMICalculator.py**: Contains the user interface logic using Tkinter
- **bmi_calculator_core.py**: Contains the core BMI calculation logic
- **test_bmi_core.py**: Contains tests for the core functionality

### Screenshot of the Application
<img alt="img.png" height="auto" src="screenshot.png" width="30%"/>

## Features

- Calculate BMI based on weight (kg) and height (m)
- Display BMI category (Underweight, Normal weight, Overweight, Obesity)
- Color-coded results for better visualization
- Input validation with user-friendly error messages
- Support for both dot and comma as decimal separators

## How to Run

1. Make sure you have Python installed
2. Run the application:
   ```
   python BMICalculator.py
   ```

3. To run the tests:
   ```
   python test_bmi_core.py
   ```

## Design Decisions

### Separation of Concerns

The application follows a clear separation between:

- **UI Logic**: Responsible for displaying the interface, handling user input, and presenting results
- **Business Logic**: Responsible for the actual BMI calculations, categorization, and input validation

This separation makes the code:
- More maintainable
- Easier to test
- More reusable (the core logic can be used in other interfaces)

### Core Module Functions

The core module provides these main functions:

- `calculate_bmi(weight, height)`: Calculates BMI value
- `get_bmi_category(bmi)`: Determines the health category based on BMI
- `get_category_color(category)`: Returns a color code for the category
- `validate_input(weight_str, height_str)`: Validates user input

## Future Improvements

Potential enhancements for the future:

- Add support for imperial units (pounds, inches)
- Save history of calculations
- Provide more detailed health information
- Add data visualization for BMI trends