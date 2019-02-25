from flask import jsonify
from flask_restful import Resource, reqparse
from db import get_db


class Dictionary(Resource):
    def get(self):
        # handling query string
        parser = reqparse.RequestParser()
        parser.add_argument('word', type=str, location='args')
        args = parser.parse_args()

        # database connection
        conn = get_db()
        c = conn.cursor()

        # fetch 6 similar data from database and return them
        if args["word"] != '':
            c.execute("SELECT word,meaning FROM 'dictionary' WHERE word like ? Order by word",
                      ('{}%'.format(args["word"]),))

            r = [dict((c.description[i][0], value)
                      for i, value in enumerate(row)) for row in c.fetchmany(6)]

            return jsonify({'results': r})
        else:
            return {'results': ''}
