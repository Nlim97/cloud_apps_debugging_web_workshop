class Post:
    def __init__(self, title, content, tags=None, id=None):
        self.id = id
        self.title = title
        self.content = content
        self.tags = tags if tags is not None else []

    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.tags})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
