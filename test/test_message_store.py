from unittest.mock import Mock
from lib.db.message_store import MessageStore
import freezegun


class TestMessageStore:
    def test_message_store_has_empty_message_list_when_initialized(self):
        # Given
        message_store = MessageStore()
        # Then
        assert message_store.messages == []

    def test_store_actually_stores_a_message(self):
        # Given
        mocked_message = Mock()
        mocked_message.author = "joe"
        mocked_message.bot = False

        message_store = MessageStore()

        # When

        message_store.store(mocked_message)

        # Then
        assert mocked_message in message_store.messages

    @freezegun.freeze_time("2023-01-01 00:06:00")
    def x_test_message_since_contains_the_right_messages(self, message_sample):
        message_store = MessageStore()
        message_store.messages = message_sample

        message_since_last_two_hours = message_store.messages_since(2)

        print([message.created_at for message in message_since_last_two_hours])

        assert len(message_since_last_two_hours) == 4
        assert 5 in [message.content for message in message_since_last_two_hours]
        assert 2 not in [message.content for message in message_since_last_two_hours]
