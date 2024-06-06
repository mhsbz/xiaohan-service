from ..models import user


def new_user(member_id: str) -> user.User:
    return user.User(member_id)
