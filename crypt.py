"""
    made by @skvozsneg
"""
import hashlib

from math import gcd
from random import randint


# Классы исключений
class WrongVarRange(Exception):
    pass


# Классы
class Rsa:
    def __init__(self):
        self.p, self.q = self.get_random_primes()
        self.n = self.p * self.q
        self.eller = (self.p - 1) * (self.q - 1)
        self.e = self.get_random_e(self.n, self.eller)
        self.d = self.get_d(self.e, self.eller)

        self.open_key = (self.e, self.n)    # Открытый ключ.
        self.closed_key = (self.d, self.n)  # Закрытый ключ.

    # Методы
    def send_message(self, message):
        """Подпись отправляемоего сообщения.

        :param message: Отправляемое сообщение.
        :return: Сообщение и цифровая подпись.
        """
        message_hash = int(''.join([i for i in hashlib.md5(message.encode()).hexdigest() if i.isdigit()])[:5])
        digit_sign = (message_hash ** self.d) % self.n

        return message, digit_sign

    def get_message(self, message, digit_sign):
        """Проверка подписанного сообщения.

        :param digit_sign: Цифровая подпись полученного сообщения.
        :param message: Получаемое сообщение
        :return: Истина, если проверка успешна. Ложь, если проверка провалена.
        """
        message_hash = int(''.join([i for i in hashlib.md5(message.encode()).hexdigest() if i.isdigit()])[:5])
        hash_obr = (digit_sign ** self.e) % self.n

        return message_hash == hash_obr

    # Статические методы
    @classmethod
    def is_prime(cls, n: int) -> bool:
        """Проверка числа на простату.

        :param n: Проверяемое число.
        :return: Истина или ложь
        """
        if n < 2:
            return False
        if n == 2:
            return True

        limit = n ** 1 / 2
        i = 2
        while i <= limit:
            if n % i == 0:
                return False
            i += 1
        return True

    @classmethod
    def get_random_primes(cls, min_prime=3, max_prime=1000, n=2) -> tuple:
        """Получение случайного списка простых чисел.

        :param min_prime: Минимальное простое число.
        :param max_prime: Максимальное простое число.
        :param n: Количество необходимых чисел.
        :return: Список с простыми числами.
        """
        if min_prime > max_prime or n > max_prime:
            raise WrongVarRange("Неверный диапазон переменных.")

        primes = set()
        prime_list = [i for i in range(min_prime, max_prime) if cls.is_prime(i)]

        while len(primes) != n:
            primes.add(prime_list[randint(0, len(prime_list) - 1)])

        return tuple(primes)

    @classmethod
    def get_random_e(cls, n, eller):
        """Получение случайного e.

        :param eller: Выбирается такое e, что e взаимно простое с eller.
        :param n: Выбирается такое e, что e больше 0 и меньше n.
        :return: Случайное e.
        """
        candidate_list = [i for i in range(0, n + 1)]
        while True:
            e = candidate_list.pop(randint(0, len(candidate_list) - 1))
            if gcd(e, eller) == 1:
                break

        return e

    @classmethod
    def get_d(cls, e, eller):
        """Вычисление d.

        :param e: Необходимая для вычисления переменная.
        :param eller: Необходимая для вычисления переменная.
        :return: Искомый d.
        """
        d = 1
        while d * e % eller != 1:
            d += 1

        return d


