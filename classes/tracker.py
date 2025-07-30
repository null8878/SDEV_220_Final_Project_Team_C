class Tracker:
    def __init__(self, tracker_id):
        self.tracker_id = tracker_id
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
