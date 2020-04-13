"""Administrate users, trainings, scores; run trainings."""

import os
import numpy as np
import pandas as pd
import uuid

def parse_cli():
    '''Parse command-line arguments'''
    pass

class Account:
    '''Account for an identity. Has credentials and roles.'''
    __name__ = 'Account'

    def __init__(self, name, email=None):
        self.name = name
        self.uuid = uuid.uuid1()
        self.roles = set()
        self.email = email
        print('New Account created.')


    def add_player_role(self, name=None):
        if name is None:
            name = self.name

        player_role = Player(name)
        self.roles.add(player_role)
        return player_role


    def rm_player_role(self, name=None):
        for role in self.roles:
            if role.__class__.__name__ == 'Player':
                print('Player role found. Removal failed - not implemented.')
            else:
                print('No op')


    def add_trainer_role(self, name=None):
        if name is None:
            name = self.name

        trainer_role = Trainer(name)
        self.roles.add(trainer_role)
        return trainer_role


    def show_roles(self):
        for role in self.roles:
            print(role)

    def __str__(self):
        return 'UUID: {}\nUsername: {}\nEmail: {}\nRoles: {}'.format(self.uuid, self.name, self.email, self.roles)


class Team:
    '''A team is made up of players, trainers and a manager.
    Also, the team has a team-score, and team-plans.'''
    __name__ = 'Team'

    def __init__(self, name):
        self.name = name
        self.uuid = uuid.uuid1()
        self.manager = None # TODO
        self.accounts = set()
        self.score = 0
#        self.score_history = pd.DataFrame(columns=['time', 'score', 'accounts']) # TODO: timeseries is better

    def add_account(self, account):
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
        return 'UUID: {}\nRole: {}\nName: {}\nTeam: {}'.format(self.uuid, self.__class__.__name__, self.name, self.team)


class Player(Role):
    '''Player can execute plan and look at stats.'''
    def __init__(self, name, team=None):
        super().__init__(name, team)
        self.plan_book = set()
        self.training_history = pd.DataFrame(columns=['time', 'plan_uiid', 'claimed'])
        self.score = 0
        print('Player role initialized.')

    def show_plans(self):
        for plan in plan_book:
            print(plan)


    def show_training_history(self):
        print(self.training_history)


    def claim_training(self, plan):
        '''Player states that they have completed the training.
        Track this in their history, and assign points.'''
        history_entry = [time.time(), plan.uuid, True]
        print(history_entry)

    def __str__(self):
        string = 'UUID: {}\nRole: {}\nName: {}\nTeam: {}'.format(self.uuid, self.__class__.__name__, self.name, self.team)
        string += '\nScore: {}'.format(self.score)
        return string

class Manager(Role):
    '''Managers invite & kick players to/from teams. Also, they assign roles.'''
    def __init__(self, name, team):
        super().__init__(name, team)
        print('Manager role initialized.')


    def create_team(self):
        pass


    def show_team(self):
        pass


    def invite_player(self, player):
        pass


    def kick_player(self, player):
        pass





class Trainer(Role):
    '''Trainer objects own, create and edit Trainings.''' 
    def __init__(self, name, team=None):
        super().__init__(name, team)
        self.plans = set()
        print('Trainer role initialized.')


    def create_plan(self, name):
        '''Create a new training plan.'''
        pass


    def load_plan(self, path, name=None):
        '''Load an existing training plan from csv. This is a wrapper for Plan.from_csv .'''
        if name is None:
            folder_path, file_name = os.path.split(path)
            name = os.path.splitext(file_name) [0]

        # Create a new plan instance, fill with csv
        plan = Plan(name)
        plan.from_csv(path)
        self.plans.add(plan)

        return plan


    def edit_plan(self, training_id):
        '''Change the content or scoring of a training'''
        pass


    def show_plans(self):
        '''Print all plans'''
        print(list(self.plans))
        for plan in list(self.plans):
            print(plan)


    def update_points(self, plan, score):
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

    def to_csv(self, data_folder):
        full_path = os.path.join(data_folder, name)
        self.exercises.to_csv(full_path)

    def from_csv(self, path):
        self.exercises = pd.read_csv(path)

    def __str__(self):
        return str(self.exercises)


class Workout:
    '''A real-time workout session.
    A player exectues a plan, which contains target times.
    The session gives the player controls to pause the session, which will be recorded in the workout-log.'''
    
    def __init__(self, plan):
        self.plan = plan
        self.time = None

    def show_plan(self):
        print(self.plan)


if __name__=='__main__':

    lu_acc = Account(name='lu')
    print(lu_acc)

    lu_trainer = lu_acc.add_trainer_role()
    r_path = '../data/example_running.csv'
    lu_trainer.load_plan(r_path, name = 'testname')
    s_path = '../data/example_strength.csv'
    lu_trainer.load_plan(s_path, name = 'testname')

    lu_player = lu_acc.add_player_role()
    lu_player.score += 100
    print()
    print(lu_player)
