from api import app, db, request
from api.models.author import AuthorModel
from api.models.quote import QuoteModel
from api.schemas.quote import quote_schema, quotes_schema

@app.route('/quotes', methods=["GET"])
def quotes():
    quotes = QuoteModel.query.all()
    return quotes_schema.dump(quotes)
    # return [quote.to_dict() for quote in quotes]
    
@app.route('/quotes/<int:quote_id>', methods=["GET"])
def quote_by_id(quote_id):
    quote = QuoteModel.query.get(quote_id)
    if quote is not None:
        return quote.to_dict(), 200
    return {"Error": f"Quote id={quote_id} not found"}, 404    

@app.route('/authors/<int:author_id>/quotes', methods=["GET"])
def quotes_by_author_id(author_id):
    author = AuthorModel.query.get(author_id)
    if author:
        quotes = author.quotes.all()
        return [quote.to_dict() for quote in quotes], 200  # Возвращаем все цитаты автора
    return {"Error": f"Author id={author_id} not found"}, 404

@app.route('/authors/<int:author_id>/quotes', methods=["POST"])
def create_quote(author_id):
    quote_data = request.json
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author id={author_id} not found"}, 404

    quote = QuoteModel(author, quote_data["text"])
    db.session.add(quote)
    db.session.commit()
    return quote.to_dict(), 201


@app.route('/quotes/<int:quote_id>', methods=["PUT"])
def edit_quote(quote_id):
    quote_data = request.json
    quote = QuoteModel.query.get(quote_id)
    quote.text = quote_data["text"]
    db.session.commit()
    return quote.to_dict(), 200


@app.route('/quotes/<int:quote_id>', methods=["DELETE"])
def delete_quote(quote_id):
    quote = QuoteModel.query.get(quote_id)
    if not quote:
        return {"Error": f"Quote id={quote_id} not found"}, 404
    db.session.delete(quote)
    db.session.commit()
    return f"Quote id={quote_id} deleted", 200
