from flask import abort
from flask_restplus import Resource
from app.database import Team
from app.extensions import api, db
from app.translation.serializer import Serializer


@api.route('/teams')
class TeamsListView(Resource):
    def get(self):
        teams = db.session.query(Team).all()

        return dict(list=[Serializer.serialize_team(team) for team in teams])


@api.route('/teams/<int:team_id>')
class TeamsView(Resource):
    def get(self, team_id):
        team = db.session.query(Team).get(team_id)

        if not team:
            abort(404, 'Team with ID {} not found'.format(team_id))

        return Serializer.serialize_team(team)


