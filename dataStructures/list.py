class List:
    def __init__(self):
        self.list = []

    def is_empty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def get_length(self):
        return len(self.list)

    def insert(self, position, item):
        if position < 1:
            raise Exception("Invalid position")

        elif position > len(self.list) + 1:
            raise Exception("Invalid position")

        else:
            self.list.insert(position, item)

    def remove(self, position):
        if position < 1:
            raise Exception("Invalid position")

        elif position > len(self.list):
            raise Exception("Invalid position")

        else:
            self.list.pop(position-1)

    def get_entry(self, position):
        if position < 1:
            raise Exception("Invalid position")

        elif position > len(self.list):
            raise Exception("Invalid position")

        else:
            return self.list[position-1]

    def replace(self, position, item):
        if position - 1 < 0:
            raise Exception("Invalid position")

        elif position - 1 > len(self.list):
            raise Exception("Invalid position")

        else:
            self.list[position - 1] = item

    def clear(self):
        self.list.clear()
