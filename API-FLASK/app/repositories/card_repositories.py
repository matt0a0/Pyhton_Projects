from app.models.card import Card
from app.config.db_settings import get_connection
from typing import Type

class CardRepository():
    def __init__(self) -> None:
        self.db = get_connection() #Injeção de dp ou Associação de classes?
        self.cards_collection = self.db['cards']
    
    def create(self, card : Type[Card]):
        card_data = {
        #'card_owner_Registration_Num' : card.card_owner_Registration_Num,
        'agency' : card.agency,
        'account' : card.account,
        'short_name' : card.short_name,
        'flag_option' : card.flag_option,
        'card_type' : card.card_type,
        'maturity_date' : card.maturity_date,
        'card_status' : "SOLICITADO",
        'card_cancel' : ""
        }
        result = self.cards_collection.insert_one(card_data)
        return str(card_data['account'])
    
    def find_by_account(self,card_account):
        return self.cards_collection.find_one({'account' : card_account})

    def find_all(self):
        return list(self.cards_collection.find())
    
    def update(self,card_account,updated_card_data):
        try:
            result = self.cards_collection.update_one({'account' : card_account}, {"$set" : updated_card_data})
            if result.matched_count >0:
                return True
            else:
                return False
        except Exception as expt:
            print("Erro ao atualizar o card {}".format(expt))
            return False

    def delete(self,card_account):
        self.cards_collection.delete_one(card_account)