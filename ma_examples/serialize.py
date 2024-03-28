from author import Author
from schema import AuthorSchema

author = Author("123", "Alex", "alex5@mail.ru") 
author_schema1 = AuthorSchema()
result = author_schema1.dump(author) # Для сериализации одной сущности
print(result, type(result))          # указываем конкретный экземпляр


authors = [
    Author("1", "Alex"),
    Author("2", "Bill"),
    Author("3", "Tom")
]
author_schema2 = AuthorSchema(many=True) # many=True для списка
result = author_schema2.dump(authors)   # экземпляров
print(result, type(result))