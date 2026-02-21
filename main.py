import json
import os
from datetime import datetime

# Colors & Formatting
G = '\033[92m'  # Green
Y = '\033[93m'  # Yellow
R = '\033[91m'  # Red
B = '\033[94m'  # Blue
C = '\033[96m'  # Cyan
W = '\033[0m'   # Reset (White)
BOLD = '\033[1m'

FILENAME = "expenses.json"

def clear_screen():
    # Windows ke liye 'cls', Mac/Linux ke liye 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []

def save_data(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    while True:
        clear_screen()
        print(f"{BOLD}{C}--- ➕ ADD NEW EXPENSES ---{W}")
        print(f"{Y}(Type 'done' to go back){W}\n")
        
        amount_input = input(f"{BOLD}Enter amount: {W}").strip().lower()
        if amount_input == 'done': break
        
        try:
            amount = float(amount_input)
            category = input(f"{BOLD}Enter category: {W}").strip().capitalize()
            if category.lower() == 'done': break

            date = datetime.now().strftime("%Y-%m-%d %H:%M")
            expenses.append({"date": date, "amount": amount, "category": category})
            save_data(expenses)
            print(f"\n{G}✅ Added ₹{amount} to {category}!{W}")
            input("\nPress Enter to add more...")
        except ValueError:
            print(f"\n{R}❌ Error: Please enter a valid number.{W}")
            input("Press Enter to try again...")

def view_expenses(expenses):
    clear_screen()
    print(f"{BOLD}{B}--- 📋 EXPENSE HISTORY ---{W}\n")
    if not expenses:
        print(f"{R}No expenses found.{W}")
    else:
        print(f"{BOLD}{'Date':<18} | {'Category':<15} | {'Amount':<10}{W}")
        print("-" * 50)
        total = 0
        for exp in expenses:
            print(f"{C}{exp['date']:<18}{W} | {Y}{exp['category']:<15}{W} | {G}₹{exp['amount']:<10}{W}")
            total += exp['amount']
        print("-" * 50)
        print(f"{BOLD}Total Expenditure: {G}₹{total}{W}")
    
    input(f"\n{B}Press Enter to return to menu...{W}")

def delete_expense(expenses):
    clear_screen()
    print(f"{BOLD}{R}--- 🗑️ DELETE RECORDS ---{W}\n")
    cat = input("Enter category name to delete: ").strip().capitalize()
    
    old_len = len(expenses)
    expenses[:] = [e for e in expenses if e['category'] != cat]
    
    if len(expenses) < old_len:
        save_data(expenses)
        print(f"\n{G}🗑️ Success: All '{cat}' records deleted!{W}")
    else:
        print(f"\n{Y}⚠️ No records found for '{cat}'.{W}")
    input("\nPress Enter to return...")

def main():
    expenses = load_data()
    while True:
        clear_screen()
        # ASCII Header
        print(f"""{BOLD}{G}
  💰 ============================ 💰
     EXPENSE MANAGEMENT ENGINE
  💰 ============================ 💰{W}""")
        print(f"\n  {C}1.{W} ➕ Add Expenses")
        print(f"  {C}2.{W} 📋 View History")
        print(f"  {C}3.{W} 🗑️  Delete Category")
        print(f"  {C}4.{W} 🚪 Exit")
        
        choice = input(f"\n{BOLD}Select Option (1-4): {W}")

        if choice == "1": add_expense(expenses)
        elif choice == "2": view_expenses(expenses)
        elif choice == "3": delete_expense(expenses)
        elif choice == "4":
            print(f"\n{Y}Goodbye! Your data is saved.{W}")
            break
        else:
            print(f"\n{R}Invalid choice!{W}")
            input("Press Enter...")

if __name__ == "__main__":
    main()