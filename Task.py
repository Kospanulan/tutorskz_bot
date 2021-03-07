class Task:
    def __init__(self, discipline="", deadline="", chat_id="", user_id=""):
        self.discipline = discipline
        self.deadline = deadline
        self.chat_id = chat_id
        self.user_id = user_id

    def __str__(self):
        pass

    def setDiscipline(self, discipline):
        self.discipline = discipline

    def setDeadline(self, deadline):
        self.deadline = deadline

    def setChat_id(self, chat_id):
        self.chat_id = chat_id

    def setUser_id(self, user_id):
        self.user_id = user_id

    def getDiscipline(self):
        return self.discipline

    def getDeadline(self):
        return self.deadline

    def getChat_id(self):
        return self.chat_id

    def getUser_id(self):
        return self.user_id

