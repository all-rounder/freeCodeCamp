class Category:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.ledger = []
        self.expense = 0

    def __repr__(self):
        name_length = len(self.name)
        left_star = int((30 - name_length) / 2)
        right_star = 30 - left_star - name_length
        result = "*" * left_star + self.name + "*" * right_star + "\n"
        for line in self.ledger:
            description = line["description"][:23]
            amount = str(format(line["amount"], ".2f"))
            result += description.ljust(23) + amount.rjust(7) + "\n"
        result += "Total: " + str(self.total)
        return result

    def deposit(self, amount, desc=""):
        self.total += amount
        self.ledger.append({"amount": amount, "description": desc})

    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.total -= amount
            self.ledger.append({"amount": -amount, "description": desc})
            return True
        else:
            return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.total -= amount
            category.total += amount
            self.ledger.append({"amount": -amount, "description": "Transfer to " + category.name})
            category.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount <= self.total:
            return True
        else:
            return False


def create_spend_chart(categories):
    cat_len = len(categories)
    result = "Percentage spent by category\n"

    expense_total = 0
    expense_percentage = {}  # use dictionary to save expense_percentage
    for i in categories:
        expense_total += category_expense(i)
    print("expense_total:", expense_total)
    for i in categories:
        expense_percentage[i.name] = category_expense_percentage(i, expense_total)
        print("expense_percentage:", expense_percentage[i.name])

    for i in range(100, -1, -10):
        result += str(i).rjust(3) + "| "
        for j in categories:
            if i / 10 <= expense_percentage[j.name]:
                result += "o  "
            else:
                result += " " * 3
        result += "\n"

    dash_len = 1 + cat_len * 3
    result += " " * 4 + "-" * dash_len + "\n"

    name_height = 0
    for c in categories:
        name_height = max(name_height, len(c.name))
    print("name_height", name_height)

    category_name = ""
    for i in range(name_height):
        category_name += " " * 5
        for c in categories:
            if i < len(c.name):
                category_name += c.name[i] + " " * 2
            else:
                category_name += " " * 3
        category_name += "\n"

    result += category_name[:-1]  # removed "\n" in the last line
    print(result)
    return result


def category_expense(category):
    expense = 0
    for i in category.ledger:
        if i["amount"] < 0:
            expense += i["amount"]
    category.expense = expense
    return expense


def category_expense_percentage(category, expense_total):
    percentage = category.expense / expense_total
    percentage = int(percentage * 10)  # rounded down to the nearest 10
    return percentage
