#   Tested launch
from crypt import Rsa


if __name__ == '__main__':
    crypt = Rsa()
    print(crypt.open_key, crypt.closed_key)

    message, sign = crypt.send_message('asdasdas')
    print(message, sign)
    print(crypt.get_message(
        message=message,
        digit_sign=sign
    ))
