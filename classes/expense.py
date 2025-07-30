class Expense:
    def __init__(self, amount, description, tracker_id, roommate_id):
        self.amount = amount
        self.description = description
        self.tracker_id = tracker_id
        self.roommate_id = roommate_id

    def to_tuple(self):
        return (self.amount, self.description, self.tracker_id, self.roommate_id)
