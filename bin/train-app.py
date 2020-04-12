"""Administrate users, trainings, scores; run trainings."""

import os
import numpy as np
import pandas as pd
import uuid

def parse_cli():
    '''Parse command-line arguments'''
    pass


class Trainer:
    '''Trainer objects own, create and edit Trainings. Also, they administrate team memberships and scoring.''' 
    def __init__(self, name, team=None):
        self.name = name
        self.uuid = uuid.uuid1()
        self.team = team
        self.plans = set()


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

        return name, exercise_df


    def edit_plan(self, training_id):
        '''Change the content or scoring of a training'''
        pass


    def show_plans(self, training_id):
        '''A wrapper for Plan.show'''
        for plan in list(self.plans):
            print(plan.uui, plan.name, plan.exercises)

    def show(self):
        print('UUID: ', self.uuid, '\nName: ', self.name, '\nTeam: ', self.team)


class Plan:
    '''A training plan. Contains a table of exercises.'''

    def __init__(self, name):
        # non-unique name-tag
        self.name = name
        # unique identifier to avoid collisions between same name
        self.uuid = uuid.uuid1()
        # exercies are stored in a pandas data frame
        self.exercises = pd.DataFrame() 

    def to_csv(self, data_folder):
        full_path = os.path.join(data_folder, name)
        self.exercises.to_csv(full_path)

    def from_csv(self, path):
        self.exercises = pd.read_csv(path)

    def show(self):
        print(self.exercises)



class Player:
    pass


class Team:
    pass

if __name__=='__main__':

    lu = Trainer('lu')
    lu.show()


    plan = Plan('test')
    plan.from_csv('../data/example_running.csv')
    plan.show()


    if False:
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
