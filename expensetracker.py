import json
import csv

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.monthly_budget = 0

    def set_budget(self):
        try:
            self.monthly_budget = float(input("Enter your monthly budget: "))
            print(f"Monthly budget set to {self.monthly_budget:.2f}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

    def add_expense(self):
        try:
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category (e.g., Food, Transport, etc.): ")
            amount = float(input("Enter the expense amount: "))
            description = input("Enter a brief description of the expense: ")
            self.expenses.append({
                "date": date,
                "category": category,
                "amount": amount,
                "description": description
            })
            print("Expense added successfully!\n")
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.\n")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.\n")
            return

        print("Your Expenses:")
        total_spent = 0
        for expense in self.expenses:
            if all(key in expense for key in ["date", "category", "amount", "description"]):
                print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']:.2f}, Description: {expense['description']}")
                total_spent += expense['amount']
            else:
                print("Incomplete expense entry found and skipped.")
        print(f"\nTotal Spent: {total_spent:.2f}")

        if self.monthly_budget:
            remaining_budget = self.monthly_budget - total_spent
            if remaining_budget < 0:
                print("Warning: You have exceeded your budget!\n")
            else:
                print(f"Remaining Budget: {remaining_budget:.2f}\n")

    def save_expenses_to_csv(self):
        try:
            with open("expenses.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Category", "Amount", "Description"])
                for expense in self.expenses:
                    writer.writerow([expense["date"], expense["category"], expense["amount"], expense["description"]])
            print("Expenses saved to expenses.csv\n")
        except Exception as e:
            print(f"An error occurred while saving expenses: {e}\n")

    def load_expenses_from_csv(self):
        try:
            with open("expenses.csv", "r") as file:
                reader = csv.DictReader(file)
                self.expenses = [row for row in reader]
                for expense in self.expenses:
                    expense["amount"] = float(expense["amount"])
            print("Expenses loaded successfully from CSV!\n")
        except FileNotFoundError:
            print("No saved expenses found. Starting fresh.\n")
        except Exception as e:
            print(f"An error occurred while loading expenses: {e}\n")

    def track_budget(self):
        total_spent = sum(expense["amount"] for expense in self.expenses)
        print(f"Total Spent: {total_spent:.2f}")
        if self.monthly_budget:
            remaining_budget = self.monthly_budget - total_spent
            if remaining_budget < 0:
                print("Warning: You have exceeded your budget!\n")
            else:
                print(f"You have {remaining_budget:.2f} left for the month.\n")
        else:
            print("Monthly budget not set.\n")


def main():
    tracker = ExpenseTracker()
    tracker.load_expenses_from_csv()

    while True:
        print("Menu:")
        print("1. Set Monthly Budget")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.set_budget()
        elif choice == "2":
            tracker.add_expense()
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.track_budget()
        elif choice == "5":
            tracker.save_expenses_to_csv()
        elif choice == "6":
            tracker.save_expenses_to_csv()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
