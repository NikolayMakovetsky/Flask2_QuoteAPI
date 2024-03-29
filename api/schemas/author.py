from api import ma
from api.models.author import AuthorModel
from api.models.quote import QuoteModel
# важно импортировать QuoteModel, т.к. в AuthorModel
# есть relationship 'QuoteModel'

# Используем AutoSchema
class AuthorSchema(ma.SQLAlchemyAutoSchema):
   class Meta:
       model = AuthorModel
       # параметры не указываются т.к. используется АВТОсхема

# для единичного экземпляра класса AuthorModel
author_schema = AuthorSchema()
# для списка экземпляров класса AuthorModel
authors_schema = AuthorSchema(many=True)

