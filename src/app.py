from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource
from hashids import Hashids

app = Flask(__name__)
# TODO: Use env vars
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'this should be a secret random string'
db = SQLAlchemy(app)
api = Api(app)
hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))

    def __repr__(self):
        return '<Url %s>' % f'/{hashids.encode(self.id)}'

db.create_all()


@api.route('/urls')
class UrlListResource(Resource):

    def post(self):
        # TODO: Add request parsing input validation
        new_url = Url(url=request.json['url'])
        db.session.add(new_url)
        db.session.commit()
        hash_id = hashids.encode(new_url.id)
        short_url = f'{request.host_url}{hash_id}'
        # TODO: Add response marshalling
        return {'url': short_url}, 200


@app.route('/<string:hash_id>')
def get_url(hash_id):
    url_id = hashids.decode(hash_id)
    if not url_id:
        return {'message': 'Not Found'}, 404
    url_record = Url.query.get_or_404(url_id[0])
    return {'url': url_record.url}, 200

if __name__ == '__main__':
    app.run(debug=True)
