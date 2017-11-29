class Serializer:
    @staticmethod
    def serialize_player(player):
        return {
            'id': player.id,
            'name': player.name,
            'rating': player.rating,
            'age': player.age,
            'team': Serializer.serialize_team(player.team),
            'position': Serializer.serialize_position(player.position),
        }

    @staticmethod
    def serialize_team(team):
        return {
            'id': team.id,
            'name': team.name,
        }

    @staticmethod
    def serialize_position(position):
        return {
            'id': position.id,
            'name': position.name,
        }
