from app.database.models.players import Player
from app.database.models.teams import Team


class Deserializer:
    def deserialize_team(self, team_data):
        team = Team(name=team_data['name'],
                    stadium=team_data.get('stadium', None),
                    location=team_data.get('location', None),
                    manager=team_data.get('manager', None),
                    logo=team_data.get('logo', None))

        team.players = [self.deserialize_player(player) for player in team_data['players']]

        return team

    def deserialize_player(self, player_data):
        return Player(name=player_data['name'],
                      rating=player_data['rating'],
                      age=player_data['age'],
                      position_id=player_data['position']['id'],
                      starter=player_data['starter'],
                      )
