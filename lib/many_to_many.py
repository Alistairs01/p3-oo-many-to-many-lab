class Author:
    all_authors = []

    def __init__(self, name:str):
        self.name = name
        self._contracts = []
        Author.all_authors.append(self)
    def contracts(self):
        return self._contracts
    
    def books(self):
        return [contract.book for contract in self._contracts]
    
    def sign_contract(self, book: 'Book', date: str, royalties: int):
        if not isinstance(book, Book):
            raise Exception("book must be an instance in Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract
    

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)
        
    def add_contract(self, contract:'Contract'):
        if not isinstance(contract, Contract):
            raise Exception("contract must be an instance of Contract")
        self._contracts.append(contract)

class Book:
    all_books = []

    def __init__(self, title:str):
        self.title = title
        self._contracts = []
        Book.all_books.append(self)

    def contracts(self):
        return self._contracts
    def authors(self):
        return list(set(contract.author for contract in self._contracts))
        


class Contract:
    all = []

    def __init__(self, author: 'Author', book: 'Book', date: str, royalties: int):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        author._contracts.append(self)
        book._contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date:str):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [contract for contract in cls.all if contract.date == date]
        