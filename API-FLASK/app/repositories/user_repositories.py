from app.models.user import User
from app.config.db_settings import get_connection
from typing import Type

class UserRepository():
    def __init__(self) -> None:
        self.db = get_connection() #Crio um acesso ao meu banco
        self.users_collection = self.db['users'] #Crio a minha coleção de usuários
    
    def create(self,user : Type[User]): #Injeção de dependencia de Models # Interface Required
        user_data = {
            'full_name' :  user.full_name,
            'birth_date' : user.birth_date,
            'registration_number' : user.registration_number, #Utilizado Como Id no lugar do Id gerado pelo MongoDb,
            'cards_accounts' : []

        }
        result = self.users_collection.insert_one(user_data)
        return str(user_data['registration_number'])
    
    
    def find_by_registration(self, registration_number):
        return self.users_collection.find_one({'registration_number' : registration_number})

    def find_all(self):
        return list(self.users_collection.find())
    
    def update(self,registration_number,updated_user_data):
        try:
            result = self.users_collection.update_one({'registration_number': registration_number}, {'$set' : updated_user_data})
            if result.modified_count > 0:
                return True
            else:
                return False
        except Exception as expt:
            print("Erro ao atualizar o usuário {}".format(expt))
            return False
    
    def delete(self,registation_number):
        self.users_collection.delete_one(registation_number)