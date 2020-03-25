from google.cloud import firestore

class User:
    def __init__(self, username, first_name, last_name, chat_id):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.chat_id = chat_id

    def to_dict(self):
        return {
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "chat_id": self.chat_id,
        }

    def save(self):
        db = firestore.Client()
        doc_ref = db.collection(type(self).__name__.lower()).document(self.username)
        return doc_ref.set({
            "first_name": self.first_name,
            "last_name": self.last_name,
            "chat_id": self.chat_id,
        })