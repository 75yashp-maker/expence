class Expenses:
    def __init__(self, title, amount, category, date):
        self.title = title
        self.amount = amount
        self.category = category
        self.date = date

    def to_tuple(self):
        return (self.title, self.amount, self.category, self.date)
        
