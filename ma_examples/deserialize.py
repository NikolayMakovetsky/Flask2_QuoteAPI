# from author import Author
from schema import AuthorSchema

json_data = """
{
    "name": "Ivan",
    "email": "ivan@mail.ru"
}
"""
schema1 = AuthorSchema() # десериализация одного экземпляра
result = schema1.loads(json_data) # есть load и loads !!
print(result, type(result))


json_data = """
[
    {
    "id": 1,
    "name": "Alex",
    "email": "alex@mail.ru"
    },
    {
    "id": 2,
    "name": "Bill",
    "email": "bill@mail.ru"
    },
    {
    "id": 3,
    "name": "Tom",
    "email": "tom@mail.ru"
    }
]
"""
schema2 = AuthorSchema(many=True) # десериализация списка экземпляров
result = schema2.loads(json_data) # есть load и loads !!
print(result, type(result))

