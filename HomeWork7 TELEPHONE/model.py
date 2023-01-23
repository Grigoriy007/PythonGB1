class Database:
    phone_book = []
    path = ''


    def __init__(self, parth: str='phone_book.txt'):
        self.path = parth

    def open(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for line in data:
                self.phone_book.append(line.strip().split(';'))


    def get(self):
        return self.phone_book


    def update(self, contact:list):
        self.phone_book.append(contact)


    def search(self, search:str):
        global phone_book
        search_results = []
        for line in self.phone_book:
            for field in line:
                if search in field:
                    search_results.append(line)
                    break
        return search_results


    def save(self):
        data = []
        for line in self.phone_book:
           data.append(';'.join(line))
        with open(self.path, 'w', encoding='UTF-8') as file:
            data = file.write('\n'.join(data))

db_phone = Database()