from app.extensions import db


class Base(db.Model):
    """Convenience base DB model class."""

    __abstract__ = True