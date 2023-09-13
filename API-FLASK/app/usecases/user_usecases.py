from app.models.user import User
from app.repositories.user_repositories import UserRepository

class UserUseCases():
    def __init__(self) -> None:
        self.user_repository = UserRepository()
    
    def create_user(self,full_name,birth_date,registration_number):
        new_user = User(full_name,birth_date,registration_number)
        self.user_repository.create(new_user)
        return new_user.registration_number
    
    def get_user_by_registration_number(self,registration_number):
        return self.user_repository.find_by_registration_number(registration_number)
    
    def get_all_users(self):
        return self.user_repository.find_all()
    
    def update_user(self,registration_number,full_name,birth_date):
        updated_user_data = self.user_repository.find_by_registration_number(registration_number)
        if  updated_user_data:
            updated_user_data['registration_number'] = registration_number
            updated_user_data['full_name'] = full_name
            updated_user_data['birth_date'] = birth_date
            self.user_repository.update(registration_number, updated_user_data)
            return  updated_user_data
    
    def delete_user(self,registration_number):
        user_to_delete = self.user_repository.find_by_registration_number(registration_number)
        if user_to_delete:
            self.user_repository.delete(user_to_delete)
    
