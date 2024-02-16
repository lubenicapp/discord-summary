from datetime import datetime, timedelta


class MessageStore:
    """
        message structure:
        [
            {
                "content":
                "name":
                "datetime",
            },

    """

    def __init__(self):
        self.messages = []

    def store(self, message):
        self.messages.append(message)
        messages = self.messages[::-1][:200]
        self.messages = messages

    def messages_since(self, hours):
        now = datetime.now()
        delta = timedelta(hours=hours)
        sample = [message for message in self.messages if message.created_at > now - delta]
        return sample
