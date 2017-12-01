class Serializer:
    @staticmethod
    def serialize_player(player):
        return {
            'id': player.id,
            'name': player.name,
            'rating': player.rating,
            'age': player.age,
            'team': Serializer.serialize_team(player.team),
            'position': player.position.name,
            'starter': player.starter,
        }

    @staticmethod
    def serialize_team(team):
        return {
            'id': team.id,
            'name': team.name,
            'manager': team.manager,
            'stadium': team.stadium,
            'location': team.location,
            'logo': team.logo,
        }

    @staticmethod
    def serialize_position(position):
        return {
            'id': position.id,
            'name': position.name,
        }
