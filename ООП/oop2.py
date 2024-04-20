class Note(object):
    def __init__(self, text):
        self.text = text
        self.count = 0

    def upcount(self):
        self.count += 1 

note1 = Note('Задача 1')
note2 = Note('Задача 2')
# print(note1.__dict__)
# print(dir(note1))
print(note1.text)