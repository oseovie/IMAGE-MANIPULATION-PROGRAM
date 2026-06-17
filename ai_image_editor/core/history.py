class EditHistory:
    def __init__(self):
        self.entries = []

    def add(self, action, details=None):
        self.entries.append({"action": action, "details": details or {}})
