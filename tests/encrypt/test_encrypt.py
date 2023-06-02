# Referências bibliográficas:
# https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
# https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest-raises
import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = "buapau"  # iniciais dos emojis do readme
    invalid_message = 3
    invalid_key = "buapau"
    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(invalid_message, 3)
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message(message, invalid_key)
    assert encrypt_message(message, 9) == "uapaub"
    assert encrypt_message(message, 3) == "aub_uap"
    assert encrypt_message(message, 4) == "ua_paub"
