from app.models.card import Card
from app.repositories.card_repositories import CardRepository

class CardUseCases():
    def __init__(self) -> None:
        self.card_repository = CardRepository()

    def create_card(self,agency,account,short_name,flag_option,card_type,maturity_date):#(S)OLID - precisa aplicar
        new_card = Card(agency,account,short_name,flag_option,card_type,maturity_date) 
        self.card_repository.create(new_card) 
        return new_card.account
    
    def get_card_by_account(self,account):
        return self.card_repository.find_by_account(account)

    def find_all_cards(self):
        return self.card_repository.find_all()
    
    def update_card(self,agency,account,short_name,flag_option,card_type,maturity_date):#(S)OLID - precisa aplicar
        card_to_update = self.card_repository.find_by_account(account)
        if card_to_update:
            card_to_update['agency'] = agency
            card_to_update['short_name'] = short_name
            card_to_update[' flag_optiony'] = flag_option
            card_to_update['card_type'] = card_type
            card_to_update['maturity_date'] = maturity_date
            self.card_repository.update(account,card_to_update)
            return card_to_update
    
    def update_card_delivered(self,account): #(S)OLID
        card_to_update = self.card_repository.find_by_account(account)
        if card_to_update:
            card_to_update['card_status'] = "ENTREGUE"
            self.card_repository.update(account,card_to_update)
            return str(card_to_update['card_status'])
        
    def update_card_active(self,account): #(S)OLID
        card_to_update = card_to_update = self.card_repository.find_by_account(account)
        if card_to_update:
            if card_to_update['card_status'] == "ENTREGUE":
                card_to_update['card_status'] = "ATIVO"
                self.card_repository.update(account,card_to_update)
                return str(card_to_update['card_status'])
            else:
                return print("Não foi possivel Ativar o cartão")
            
    def update_card_block(self,account,reason_block : str): #(S)OLID - precisa aplicar
        card_to_update = card_to_update = self.card_repository.find_by_account(account)
        if card_to_update:
            if card_to_update['card_status'] == "ATIVO":
                card_to_update['card_status'] = str(reason_block).upper()
                self.card_repository.update(account,card_to_update)
                return str(card_to_update['card_status'])
            else:
                return print("Não foi possivel Bloquear o cartão")
            
    def update_card_cancel(self,account,reason_cancel): #(S)OLID - precisa aplicar
        card_to_update = card_to_update = self.card_repository.find_by_account(account)
        if card_to_update:
            card_to_update['card_status'] = "CANCELADO"
            card_to_update['card_cancel'] = str(reason_cancel).capitalize()
            self.card_repository.update(account,card_to_update)
            return str(card_to_update['card_status'])
        else:
            return print("Não foi possivel Cancelar o cartão")

c1 = CardUseCases()
#c1.create_card('7237','45530-7','Matheus','Visa','PLATINUM','05')
#c1.create_card("2222",'0000','Joberval','VISA','BLACK','05')
#c1.update_card('1111','45530-7','Matt V Rodrigues','Visa','BLACK','10')
#c1.update_card_delivered('45530-7')
#c1.update_card_active('45530-7')
#c1.update_card_block('45530-7','Perda')
#c1.update_card_cancel('45530-7',"Sou pobre demais")