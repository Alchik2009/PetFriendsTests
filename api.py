import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com"

    '''Авторизация с верным логином. Получаем код статуса ответа и уникальный ключ авторизации'''
    def get_api_key(self, email: str, password: str) -> json:
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'/api/key', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    '''Получение списка пиптомцев'''
    def get_list_of_pets(self, auth_key: json, filter: str = '') -> json:
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url+'/api/pets', headers=headers, params=filter)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    '''Добавление нового питомца'''
    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: str, pet_photo) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpg')
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url+'/api/pets', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    '''Добавление питомца без фото'''
    def create_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age
            })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url+'/api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    '''Добавление фото в карточку питомца'''
    def add_photo_of_pet(self, auth_key: json, pet_id, pet_photo) -> json:
        headers = {'auth_key': auth_key['key']}
        data = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'images/jpg')}
        res = requests.post(self.base_url + '/api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    '''Обновление карточки питомца'''
    def update_information_of_pets(self, auth_key: json, pet_id, name: str, animal_type: str, age: str) -> json:
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.put(self.base_url + '/api/pets/' + pet_id, headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    '''Удаление питомца'''
    def delete_api_pet(self, auth_key, pet_id):
        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url+'/api/pets/' + pet_id, headers=headers)
        status = res.status_code
        return status
