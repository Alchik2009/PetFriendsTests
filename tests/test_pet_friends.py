from api import PetFriends
from settings import email, password

pf = PetFriends()

'''Авторизация с верным логином'''
def test_get_api_key(email=email, password=password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

'''Получение списка питомцев'''
def test_get_list_of_pets(filter=''):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

'''Добавление питомца с фото'''
def test_add_new_pet(name='Валера', animal_type='Кот', age= '4', pet_photo='images/Cat.jpg'):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

'''Добавление питомца без фото'''
def test_create_pet_simple(name='Женя', animal_type='Кот', age= '40'):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

'''Добавление фото питомца в карточку'''
def test_add_photo_of_pet(pet_photo='images/Evgen.jpg'):
    _, auth_key = pf.get_api_key(email, password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
    assert status == 200
    assert result['pet_photo'] != 0

'''Обновление карточки питомца'''
def test_put_new_information_of_pet(name='Митя', animal_type='Пес', age= '33'):
    _, auth_key = pf.get_api_key(email, password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) > 0:
        status, result = pf.update_information_of_pets(auth_key, my_pets['pets'][1]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
    else:
        raise Exception('У Вас нет питомцев')

'''Удаление питомца'''
def test_delete_api_pets():
    _, auth_key = pf.get_api_key(email, password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) > 0:
        status = pf.delete_api_pet(auth_key, my_pets['pets'][0]['id'])
        assert status == 200
    else:
        raise Exception('У Вас нет питомцев')
