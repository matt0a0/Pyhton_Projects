from app.repositories.card_repositories import CardRepository
from app.repositories.user_repositories import UserRepository

class AssociacionUseCases(CardRepository,UserRepository):
    def __init__(self) -> None:
        super().__init__()
        self.user_repository = UserRepository()
        self.card_repository = CardRepository() 

    def associate(self,registration_number,account):
        user = self.user_repository.find_by_registration(registration_number)
        card = self.card_repository.find_by_account(account)
        
        if user:
            user['cards_accounts'] = [card] #Array de objetos Precisa melhorar
            self.user_repository.update(registration_number,user)
#List cards from user