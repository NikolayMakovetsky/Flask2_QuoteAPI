from api import app, db, request
from api.models.author import AuthorModel


@app.route('/authors', methods=["GET"])
def get_authors():
    authors = AuthorModel.query.all()
    authors_dict = [author.to_dict() for author in authors]
    return authors_dict, 200


@app.route('/authors/<int:author_id>', methods=["GET"])
def get_author_by_id(author_id):
    author = AuthorModel.query.get(author_id)
    if not author:
        return f"Author id={author_id} not found", 404

    return author.to_dict(), 200


@app.route('/authors', methods=["POST"])
def create_author():
    author_data = request.json
    author = AuthorModel(author_data["name"])
    db.session.add(author)
    db.session.commit()
    return author.to_dict(), 201


@app.route('/authors/<int:author_id>', methods=["PUT"])
def edit_author(author_id):
    author_data = request.json
    if author_data.get("name"):
        author = AuthorModel.query.get(author_id)
        if author is None:
            return {"Error": f"Author id={author_id} not found"}, 404
        author.name = author_data["name"]
        db.session.commit()
        return author.to_dict(), 200
    return {"Error": "New author name is not defined"}, 404


@app.route('/authors/<int:author_id>', methods=["DELETE"])
def delete_author(author_id):
    """Функция предназначена для удаления автора если у него нет цитат,
    в противном случае удаление автора приведет к ошибке
    при обращении к цитатам с удаленным автором"""
    author = AuthorModel.query.get(author_id)
    if not author:
        return f"Author id={author_id} not found", 404
    db.session.delete(author)
    db.session.commit()
    return f"Author id={author_id} deleted", 200
