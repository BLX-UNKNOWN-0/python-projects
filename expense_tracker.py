# BLX-UNKNOWN-0
# PROJECT 12 // EXPENSE TRACKER
 
import json
import os
from datetime import datetime  # NEW CONCEPT 1: datetime module
 
DATA_FILE = "expenses.json"
 
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []
 
def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)
 
def add_expense(expenses):
    print("\n--- Add Expense ---")
    try:
        amount = float(input("Amount (NPR): "))
        category = input("Category (food/transport/bills/other): ").strip().lower()
        note = input("Note (optional): ").strip()
        
        expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")  # NEW CONCEPT 1 in use
        }
        expenses.append(expense)
        save_expenses(expenses)
        print(f"✅ Added: NPR {amount:.2f} [{category}]")
    except ValueError:
        print("❌ Invalid amount.")
 
def view_expenses(expenses):
    if not expenses:
        print("\n No expenses yet.")
        return
    
    print("\n--- All Expenses ---")
    # NEW CONCEPT 2: f-string column formatting with alignment
    print(f"{'#':<4} {'Date':<17} {'Category':<12} {'Amount':>10}  Note")
    print("-" * 55)
    for i, e in enumerate(expenses, 1):
        print(f"{i:<4} {e['date']:<17} {e['category']:<12} NPR {e['amount']:>7.2f}  {e['note']}")
 
def summary(expenses):
    if not expenses:
        print("\n No expenses to summarize.")
        return
    
    # NEW CONCEPT 3: aggregating data with a dictionary
    totals = {}
    for e in expenses:
        cat = e["category"]
        totals[cat] = totals.get(cat, 0) + e["amount"]  # .get() with default value
    
    grand_total = sum(totals.values())
    
    print("\n--- Summary by Category ---")
    for cat, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * int(total / grand_total * 20)
        print(f"{cat:<12} NPR {total:>8.2f}  {bar}")
    print("-" * 35)
    print(f"{'TOTAL':<12} NPR {grand_total:>8.2f}")
 
def delete_expense(expenses):
    view_expenses(expenses)
    if not expenses:
        return
    try:
        index = int(input("\nEnter # to delete: ")) - 1
        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses(expenses)
            print(f"🗑️  Deleted: NPR {removed['amount']} [{removed['category']}]")
        else:
            print("❌ Invalid number.")
    except ValueError:
        print("❌ Enter a valid number.")
 
def main():
    expenses = load_expenses()
    
    print("=" * 40)
    print("   💸 EXPENSE TRACKER — BLX_UNKNOWN-0")
    print("=" * 40)
    
    while True:
        print("\n[1] Add Expense")
        print("[2] View All")
        print("[3] Summary")
        print("[4] Delete Expense")
        print("[5] Quit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid choice.")
 
if __name__ == "__main__":
    main()