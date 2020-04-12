"""Administrate users, trainings, scores; run trainings."""


def parse_cli():
    '''Parse command-line arguments'''
    pass


class Trainer:
    pass


class Training:
    pass


class Player:
    pass


class Team:
    pass

if __name__=='__main__':
    cli_args = parse_cli()
    # role = cli_args.role
    role = 'player'

    if role == 'player':
        print(role)

    elif role == 'trainer':
        print(role)

    else:
        print("Role '%' invalid.".format(role))
        exit()
