from api import app, db, request
from api.models.author import AuthorModel
from api.schemas.author import author_schema, authors_schema


@app.route('/authors', methods=["GET"])
def get_authors():
    authors = AuthorModel.query.all()
    return authors_schema.dump(authors), 200


@app.route('/authors/<int:author_id>', methods=["GET"])
def get_author_by_id(author_id):
    author = AuthorModel.query.get(author_id)
    if not author:
        return f"Author id={author_id} not found", 404

    return author_schema.dump(author), 200


@app.route('/authors', methods=["POST"])
def create_author():
    author_data = request.json
    author = AuthorModel(**author_data)
    db.session.add(author)
    db.session.commit()
    return author_schema.dump(author), 201


@app.route('/authors/<int:author_id>', methods=["PUT"])
def edit_author(author_id):
    author_data = request.json
    # добавить более компактную валидацию
    # if {author_data.keys} == {"name", "surname"}:
    if author_data.get("name") and author_data.get("surname"):

        author = AuthorModel.query.get(author_id)
        if author is None:
            return {"Error": f"Author id={author_id} not found"}, 404
        for key, value in author_data.items():
            setattr(author, key, value)      
        db.session.commit()
        return author_schema.dump(author), 200
    return {"Error": "Missing parameter (name, surname)"}, 404


@app.route('/authors/<int:author_id>', methods=["DELETE"])
def delete_author(author_id):
    author = AuthorModel.query.get(author_id)
    if not author:
        return f"Author id={author_id} not found", 404
    db.session.delete(author)
    db.session.commit()
    return f"Author id={author_id} deleted", 200
