import uuid
import hashlib


def hash_password(password: str) -> str:
    """
    Encrypt a string
    :param password: string to encrypt
    :return: encrypted string
    """
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password: str, user_password: str) -> bool:
    """
    Compare a hashed_password string with user_password string. For this the user input is also encrypted.
    :param hashed_password: Encrypted string
    :param user_password: Plain string
    :return: True if the passwords matches else False
    """
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def empty_str(string: str) -> bool:
    """
    A function which checks if a string is empty
    :param string: string to check
    :return: False if string is not empty, else True
    """
    if string != '':
        return False
    else:
        return True


def contain_space(string: str) -> bool:
    """
    Checks if a string contains space chars
    :param string: string to check
    :return: True if a space character is found else False
    """
    return string.__contains__(' ')


def check_credentials(string: str) -> bool:
    """
    Checks if a string contains space chars or is empty
    :param string: string to check
    :return: True if a space character is found else False
    """
    if empty_str(string) is False and not contain_space(string):
        return True
    return False
