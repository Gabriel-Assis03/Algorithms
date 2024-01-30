import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    message = '123456'
    result1 = encrypt_message(message, 4)
    assert result1 == '65_4321'
    result2 = encrypt_message(message, 3)
    assert result2 == '321_654'
    result3 = encrypt_message(message, 9)
    assert result3 == '654321'
    with pytest.raises(
        TypeError, match="tipo inválido para key"
    ):
        encrypt_message(message, '2')
    with pytest.raises(
        TypeError, match="tipo inválido para message"
    ):
        encrypt_message(3, 3)
