from expense_class import Expense

def expense_tracker():
    print("Welcome to expense tracker")
    expense_file = "expense.csv"
    expense = get_user_expense()
    save_user_expense(expense,expense_file)
    display_user_expense(expense_file)
    

def get_user_expense():
    expense_name = input("What did you spend on? ")
    expense_amount = input("How much did you spend on it? ")
    category = ["Home",
        "Food",
        "work",
        "fun",
        "other"
    ]
    for i,a in enumerate(category):
        print(f"{i+1}. {a}",)
    expense_category = int(input("Enter the Category "))

    expense = Expense(name= expense_name,category = category[expense_category-1],cost=expense_amount)
    return expense
def save_user_expense(expense,expense_file):
    with open(expense_file,'a') as f:
        f.write(f"{expense.name},{expense.category},{expense.cost}\n")
def display_user_expense(expense_file):
    expense_list : list[Expense] = []
    with open(expense_file,'r') as f:
        lines = f.readlines()
        for line in lines:
            name,category,cost= line.strip().split(",")
            element = Expense(name,category,cost)
            expense_list.append(element)
    tracker = {}
    for i in expense_list:
        tracker[i.category]=tracker.get(i.category,0)
        tracker[i.category]+=float(i.cost)
    sums = 0
    for key,value in tracker.items():
        print(f"The amount spend on {key} = {value}")
        sums+=value
    print(f"The total expense is {sums}")
    
    


if __name__ == "__main__":
    expense_tracker()