from ..repository.User_repository import select_all


def selec_all_user_service():
    users = select_all()
    print(users)
    return users