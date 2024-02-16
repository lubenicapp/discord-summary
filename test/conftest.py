import datetime
from unittest.mock import Mock
import discord.member
import pytest


@pytest.fixture()
def message_sample():
    """
    return simple mocked messages
    """
    messages = []
    for i in range(6):
        mocked_message = Mock()
        mocked_message.created_at.retur_vae = datetime.datetime(2023, 1, 1, i)
        mocked_message.content.return_value = f"{i}"
        messages.append(mocked_message)

    return messages
