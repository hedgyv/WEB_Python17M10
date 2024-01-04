from pymongo import MongoClient
from django.contrib.auth.models import User

uri = "mongodb+srv://web17_mod8:IDkrkN1JmruWcbSb@web17.k2uu2ec.mongodb.net/?retryWrites=true&w=majority"



def save_user_to_mongodb(request):
    # Получение данных пользователя
    user = User.objects.get(username=request.username)
    user_data = {
        'username': user.username,
        'email': user.email,
        'password': user.password
    }

    # Подключение к MongoDB и сохранение данных
    client = MongoClient(uri)
    db = client.quotes_db
    users_collection = db['users']
    users_collection.insert_one(user_data)

    # Закрытие соединения с MongoDB
    client.close()

    # Далее можно добавить какую-то логику или перенаправление
    # на страницу после сохранения данных

    # Возвращение HTTP-ответа или перенаправление на другую страницу
    # return HttpResponse('User data saved in MongoDB')
