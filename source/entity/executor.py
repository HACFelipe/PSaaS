from entity.code import Code

class Executor():
    """Model for Executor"""

    def __init__(self, code: Code, language : str):
        self.code = code
        self.language = language

    def execute(self, code : Code):
        print("Executing [%s] in [%s]" % (self.code.id, self.language))
        return ["Results for Code [%s]" % (self.code.id[2:])]