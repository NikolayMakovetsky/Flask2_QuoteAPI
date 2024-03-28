from marshmallow import Schema, fields

class AuthorSchema(Schema):
    id = fields.Integer() # "123" преобразуется в int
    name = fields.Str()
    email = fields.Email() # встроен отдельный класс Email !
    surname = fields.Str() # если surname не передать то ошибки не будет

# Доп параметры для поля email (Пример)
# required=True # параметр является обязательным
# error_messages={'required': 'email is required', 'code':400 }
# сообщение при возникновении ошибки

