from api import ma
from api.models.quote import QuoteModel
from api.schemas.author import AuthorSchema

# Используем Schema
class QuoteSchema(ma.SQLAlchemySchema):
    class Meta:
        model = QuoteModel

    id = ma.auto_field()
    text = ma.auto_field()
    author = ma.Nested(AuthorSchema())
    # Описываем параметры, т.к. используется ОБЫЧНАЯ схема

quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)