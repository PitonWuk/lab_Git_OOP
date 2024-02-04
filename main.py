import redis
import bcrypt


class ShoppingCart:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    def register_user(self, username, password):
        #перевірити чи існує користувач
        if self.redis_client.hexists(username, 'password_hash'):
            print("Користувач вже існує")
            return False
        #створення та зберігання хешу
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.redis_client.hset(username, 'password_hash', password_hash)
        print("Користувач успішно зареєстрований!")
        return True

    def login(self, username, password):
        #перевірка логіну та паролю
        stored_password_hash = self.redis_client.hget(username, 'password_hash')
        if stored_password_hash and bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode("utf-8")):
            print(f'Ви увійшли як {username}')
            self.current_user = username
            return True
        else:
            print("Невірний логін або пароль")
            return False


cart_app = ShoppingCart()
if cart_app.register_user('user4', '123'):
    if cart_app.login('user4', '123'):
        print("Успіх")



