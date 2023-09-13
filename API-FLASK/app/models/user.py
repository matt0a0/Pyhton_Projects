class User():
    def __init__(self,full_name,birth_date,registration_number) -> None:
        self.full_name = full_name
        self.birth_date = birth_date
        self.registration_number = registration_number
        self.cards_accounts = []
    
    def add_card(self,card):
        self.cards_accounts.append(card)
