"""Administrate users, trainings, scores; run trainings."""

import os
import time
import uuid
import pandas as pd

def parse_cli():
    '''Parse command-line arguments'''
    return


class Account:
    '''Account for an identity. Has credentials and roles.'''
    __name__ = 'Account'

    def __init__(self, name, email=None):
        self.name = name
        self.uuid = uuid.uuid1()
        self.roles = set()
        self.email = email
        self.team = None
        print('New Account created.')


    def create_team(self, name):
        '''Create a new team.'''
        self.add_manager_role()
        self.team = Team(name)


    def add_manager_role(self):
        '''Make this account a team-manager.'''
        manager_role = Manager(self.name)
        self.roles.add(manager_role)


    def add_player_role(self):
        '''Make this account able to execute training plans.'''
        player_role = Player(self.name)
        self.roles.add(player_role)
        return player_role


    def add_trainer_role(self, name=None):
        '''Make this account able to create training plans.'''
        if name is None:
            name = self.name

        trainer_role = Trainer(name)
        self.roles.add(trainer_role)
        return trainer_role


    def rm_role(self, role='Player'):
        '''Remove a role.'''
        for role in self.roles:
            if role.__class__.__name__ == role:
                print('{} role found. Removal failed - not implemented.'.format(role))
            else:
                print('No op')


    def show_roles(self):
        '''List all roles.'''
        for role in self.roles:
            print(role)


    def __str__(self):
        string = 'UUID: {}\nUsername: {}'.format(self.uuid, self.name)
        string += '\nEmail: {}\nRoles: {}'.format(self.email, self.roles)
        return string


class Team:
    '''A team is made up of players, trainers and a manager.
    Also, the team has a team-score, and team-plans.'''
    __name__ = 'Team'

    def __init__(self, name):
        self.name = name
        self.uuid = uuid.uuid1()
        self.accounts = set()
        self.score = 0


    def add_account(self, account):
        '''Assign an account to the team.'''
        self.account.add(account)


    def update_score(self):
        '''Sum the scores from the team's players to generate the current team-score'''
        new_score = 0
        for account in self.accounts:
            for role in account.roles:
                if role.__class__.__name__ == 'Player':
                    player = role
                    new_score += player.score
                    break

        self.score = new_score
        # n_accounts = len(self.accounts)
        # history_entry = [time.time(), new_score, n_accounts]
        # self.score_history.append(history_entry)


class Role:
    '''Generic parent object for all roles that teammembers can have.'''

    def __init__(self, name, team=None):
        self.name = name
        self.uuid = uuid.uuid1()
        self.team = team


    def __str__(self):
        string = 'UUID: {}\nRole: {}'.format(self.uuid, self.__class__.__name__)
        string += '\nName: {}\nTeam: {}'.format(self.name, self.team)
        return string


    def delete(self):
        '''Delete this role.'''
        return 'deleted'


class Player(Role):
    '''Player can execute plan and look at stats.'''
    def __init__(self, name, team=None):
        super().__init__(name, team)
        self.plans = set()
        self.training_history = pd.DataFrame(columns=['time', 'plan_uiid', 'claimed'])
        self.score = 0
        print('Player role initialized.')


    def show_plans(self):
        '''Show all plans'''
        print('Plan,\tPoints')
        for plan in self.plans:
            print('{},\t{}'.format(plan.name, plan.points))


    def show_training_history(self):
        '''Show trainings done in the past.'''
        print(self.training_history)


    def claim_training(self, plan):
        '''Player states that they have completed the training.
        Track this in their history, and assign points.'''
        history_entry = [time.time(), plan.uuid, True]
        self.score += plan.points
        print(history_entry)


    def __str__(self):
        string = 'UUID: {}\nRole: {}'.format(self.uuid, self.__class__.__name__)
        string += '\nName: {}\nTeam: {}'.format(self.name, self.team)
        string += '\nScore: {}'.format(self.score)
        return string


class Manager(Role):
    '''Managers invite & kick players to/from teams. Also, they assign roles.'''
    def __init__(self, name):
        super().__init__(name)
        print('Manager role initialized.')
        self.team = None


    def create_team(self, name):
        '''Create a new team.'''
        self.team = Team(name)


    def leave_team(self):
        '''Leave a created team.'''
        self.team = None


    def show_team(self):
        '''Show current team.'''
        return


    def invite_account(self, player):
        '''Invite a human/account to the current team.'''
        return player


    def remove_account(self, player):
        '''Kick an account from the current team.'''
        return player


class Trainer(Role):
    '''Trainer objects own, create and edit Trainings.'''
    def __init__(self, name, team=None):
        super().__init__(name, team)
        self.plans = set()
        print('Trainer role initialized.')


    def assign_plan(self, plan, player):
        '''Assign a training to a player.'''
        player.plans.add(plan)


    def create_plan(self, name):
        '''Create a new training plan.'''
        return name


    def load_plan(self, path, name=None):
        '''Load an existing training plan from csv. This is a wrapper for Plan.from_csv .'''
        if name is None:
            file_name = os.path.split(path)[1]
            name = os.path.splitext(file_name)[0]

        # Create a new plan instance, fill with csv
        plan = Plan(name)
        plan.from_csv(path)
        self.plans.add(plan)

        return plan


    def edit_plan(self, training_id):
        '''Change the content or scoring of a training'''
        return training_id

    def show_plans(self):
        '''Print all plans'''
        print(list(self.plans))
        for plan in list(self.plans):
            print(plan)


    def update_points(self, plan, points):
        '''Re-assign the number of points a training gives to a player.'''
        plan.points = points



class Plan:
    '''A training plan. Contains a table of exercises.'''

    def __init__(self, name):
        # non-unique name-tag
        self.name = name
        # unique identifier to avoid collisions between same name
        self.uuid = uuid.uuid1()
        # exercises are stored in a pandas data frame
        self.exercises = pd.DataFrame()
        # A training gives points to a player for completing it
        self.points = 100

    def to_csv(self, data_folder, name):
        '''Save plan as csv file.'''
        full_path = os.path.join(data_folder, name)
        self.exercises.to_csv(full_path)

    def from_csv(self, path):
        '''Load plan from csv file.'''
        self.exercises = pd.read_csv(path)

    def __str__(self):
        string = str(self.__class__.__name__) + " "
        string += str(self.name) + ", " + str(self.points) + "\n"
        string += str(self.exercises)
        return string


if __name__ == '__main__':

    pass
