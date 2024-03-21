import tkinter as tk

root = tk.Tk()
root.title('Personal Budget Tracker')


# Window configuration
window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

centre_x = int(screen_width/2 - window_width/2)
centre_y = int(screen_height/2 - window_height/2)

root.geometry(f'{window_width}x{window_height}+{centre_x}+{centre_y}')
root.resizable(False,False)


# Methods
class BudgetTracker(tk):
    def __init__(self):
        self.income = []
        self.expenses = []
    
    def add_income(self, amount, source):
        self.epenses.append((amount,source))  
        
    def add_expense(self, amount, expense):
        self.expenses.append((amount, expense))
        
    def calculate_savings(self):
        total_income = sum(amount for amount, source in self.income)
        total_expenses = sum(amount for amount, expense in self.expenses)
        return total_income - total_expenses
    
    
    # Display Report
    def display_report(self):
        print("Income")
        for amount, source in self.income:
            print(f"Source: {source}, Amount: {amount}")
        print("\nExpenses:")
        for amount, expense in self.expenses:
            print(f"Expense: {expense}, Amount: {amount}")
        print("\nTotal Income: ", sum(amount for amount, source in self.income))
        print("Total Expenses: ", sum(amount for amount, expense in self.income))
        print("Saving: ", self.calculate_savings())
        

text = tk.Label(root, text='Track your spending').pack(padx=10,pady=12)


#Income Amout & Source
income_amount_text = tk.Label(root, text='Enter income amount here:').pack()
income = tk.Entry(root).pack()

income_source_text = tk.Label(root, text='Enter income source here').pack()
income = tk.Entry(root, text='Enter income source here:').pack()

#Add income
button_add_income_amount = tk.Button(root, text="Add Income").pack()


root.mainloop()

