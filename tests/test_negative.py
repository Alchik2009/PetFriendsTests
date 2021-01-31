from api import PetFriends
from settings import email, password

pf = PetFriends()

'''1. Авторизация с пустым логином. Получение 403 кода с описанием ошибки'''
def test_get_api_key_without_email(email='', password=password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    AssertionError(f'The combination of user name and password is incorrect ')

'''2. Авторизация с пустым паролем. Получение 403 кода с описанием ошибки'''
def test_get_api_key_without_password(email=email, password=''):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert AssertionError(f'The combination of user name and password is incorrect ')

'''3. Авторизация с пустым лоигном и паролем. Получение 403 кода с описанием ошибки'''
def test_get_api_key_without_email_and_password(email='', password=''):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert AssertionError(f'The combination of user name and password is incorrect ')

'''4. Авторизация с неверным логином. Получение 403 кода с описанием ошибки'''
def test_get_api_key_invalid_email(email='Alchik', password=password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert AssertionError(f'The combination of user name and password is incorrect ')

'''5. Авторизация незарегистрированного пользователя. Получение 403 кода с описанием ошибки'''
def test_get_api_key_unregistered_user(email='shirinkineg@yandex.ru', password='password'):
    status, result = pf.get_api_key(email, password)
    assert status == 403
    assert AssertionError(f'The combination of user name and password is incorrect ')

'''6. Добавление питомца: имя = символы'''
def test_add_new_pet(name='$$$$$$$$', animal_type='Кот', age= '4', pet_photo='images/Cat.jpg'):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

'''7. Добавление питомца: имя = пустое'''
def test_add_new_pet(name='', animal_type='Кот', age= '4', pet_photo='images/Cat.jpg'):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

'''8. Добавление питомца: порода = символы'''
def test_add_new_pet(name='Петя', animal_type='$$$$$$', age= '4', pet_photo='images/Dog.jpeg'):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

'''9. Добавление питомца: порода = пустое'''
def test_add_new_pet(name='Петя', animal_type='', age= '4', pet_photo='images/Dog.jpeg'):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

'''10. Добавление питомца: фото = pdf формат'''
def test_add_new_pet(name='Вася', animal_type='Пес', age= '8', pet_photo='images/Листовка_Зачем загружать фото.pdf'):
    _, auth_key = pf.get_api_key(email, password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name
