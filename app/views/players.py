from flask import abort, request
from flask_restplus import Resource
from app.database import Player, Team
from app.extensions import api, db
from app.translation.serializer import Serializer


@api.route('/players/<int:player_id>')
class PlayersView(Resource):
    def get(self, player_id):
        player = db.session.query(Player).get(player_id)

        if not player:
            abort(404, 'Player with ID {} not found'.format(player_id))

        return Serializer.serialize_player(player)


@api.route('/teams/<int:team_id>/players')
class PlayersTeamListView(Resource):
    def get(self, team_id):
        starters_flag = request.args.get('starters', None)

        team = db.session.query(Team).get(team_id)
        if not team:
            abort(404, 'Team with ID {} not found'.format(team_id))

        players = team.players
        if starters_flag:
            return dict(list=[Serializer.serialize_player(player) for player in players if player.starter == 1])

        return dict(list=[Serializer.serialize_player(player) for player in players])


@api.route('/players')
class PlayersListView(Resource):
    def get(self):
        players = db.session.query(Player).all()

        return dict(list=[Serializer.serialize_player(player) for player in players])

