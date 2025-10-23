class SessionManager:
    def __init__(self):
        self.user = None

    def set_user(self, user_data):
        self.user = user_data

    def get_user(self):
        return self.user

    def clear_user(self):
        self.user = None


session = SessionManager()
