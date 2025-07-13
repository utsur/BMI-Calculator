# BMI Calculator with GUI
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from bmi_calculator_core import calculate_bmi, get_bmi_category, get_category_color, validate_input

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("400x500")
        self.root.resizable(True, True)
        self.root.configure(bg="#f0f0f0")

        # Set application icon and styling
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", 
                             font=("Arial", 12, "bold"),
                             background="#4CAF50")
        self.style.configure("TLabel", 
                             font=("Arial", 12),
                             background="#f0f0f0")
        self.style.configure("Header.TLabel", 
                             font=("Arial", 16, "bold"),
                             background="#f0f0f0")
        self.style.configure("Result.TLabel", 
                             font=("Arial", 14),
                             background="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header_label = ttk.Label(main_frame, 
                                text="BMI Calculator", 
                                style="Header.TLabel")
        header_label.pack(pady=(0, 20))

        # Instructions
        instructions = ttk.Label(main_frame, 
                               text="Enter your weight and height to calculate your BMI",
                               wraplength=350)
        instructions.pack(pady=(0, 20))

        # Input frame
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(fill=tk.X, pady=10)

        # Weight input
        weight_frame = ttk.Frame(input_frame)
        weight_frame.pack(fill=tk.X, pady=5)

        weight_label = ttk.Label(weight_frame, text="Weight:")
        weight_label.pack(side=tk.LEFT, padx=(0, 10))

        self.weight_var = tk.StringVar()
        weight_entry = ttk.Entry(weight_frame, textvariable=self.weight_var, width=10)
        weight_entry.pack(side=tk.LEFT)
        weight_entry.focus()

        weight_unit = ttk.Label(weight_frame, text="kg")
        weight_unit.pack(side=tk.LEFT, padx=5)

        # Height input
        height_frame = ttk.Frame(input_frame)
        height_frame.pack(fill=tk.X, pady=5)

        height_label = ttk.Label(height_frame, text="Height:")
        height_label.pack(side=tk.LEFT, padx=(0, 10))

        self.height_var = tk.StringVar()
        height_entry = ttk.Entry(height_frame, textvariable=self.height_var, width=10)
        height_entry.pack(side=tk.LEFT)

        height_unit = ttk.Label(height_frame, text="m")
        height_unit.pack(side=tk.LEFT, padx=5)

        # Calculate button
        calculate_button = ttk.Button(main_frame, 
                                    text="Calculate BMI", 
                                    command=self.calculate_bmi)
        calculate_button.pack(pady=20)

        # Bind Enter key to calculate_bmi function
        self.root.bind('<Return>', lambda event: self.calculate_bmi())

        # Result frame
        result_frame = ttk.Frame(main_frame)
        result_frame.pack(fill=tk.X, pady=10)

        # BMI result
        self.bmi_result = ttk.Label(result_frame, 
                                  text="", 
                                  style="Result.TLabel")
        self.bmi_result.pack(pady=5)

        # BMI category
        self.bmi_category = ttk.Label(result_frame, 
                                    text="", 
                                    style="Result.TLabel")
        self.bmi_category.pack(pady=5)

        # BMI information
        bmi_info_frame = ttk.Frame(main_frame)
        bmi_info_frame.pack(fill=tk.X, pady=10)

        bmi_info = ttk.Label(bmi_info_frame, 
                           text="BMI Categories:\n" +
                                "Underweight: < 18.5\n" +
                                "Normal weight: 18.5 - 24.9\n" +
                                "Overweight: 25 - 29.9\n" +
                                "Obesity: ≥ 30",
                           justify=tk.LEFT)
        bmi_info.pack(anchor=tk.W)

        # Wikipedia link
        def open_wiki_link(event):
            webbrowser.open("https://de.wikipedia.org/wiki/Body-Mass-Index")

        wiki_link = ttk.Label(bmi_info_frame, 
                            text="Mehr Informationen: Wikipedia - Body-Mass-Index",
                            foreground="blue",
                            cursor="hand2")
        wiki_link.pack(anchor=tk.W, pady=(10, 0))
        wiki_link.bind("<Button-1>", open_wiki_link)

    def calculate_bmi(self):
        try:
            # Get weight and height values
            weight_str = self.weight_var.get()
            height_str = self.height_var.get()

            # Validate input using the core function
            is_valid, error_message, weight, height = validate_input(weight_str, height_str)

            if not is_valid:
                messagebox.showerror("Input Error", error_message)
                return

            # Calculate BMI using the core function
            bmi = calculate_bmi(weight, height)

            # Determine BMI category using the core function
            category = get_bmi_category(bmi)

            # Update result labels
            self.bmi_result.config(text=f"Your BMI: {bmi:.2f}")
            self.bmi_category.config(text=f"Category: {category}")

            # Get color based on category using the core function
            color = get_category_color(category)
            self.bmi_category.config(foreground=color)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
