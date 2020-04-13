from trainapp import *

lu_acc = Account(name='lu')
print(lu_acc)

lu_trainer = lu_acc.add_trainer_role()
lu_player = lu_acc.add_player_role()
r_path = '../data/example_running.csv'
lu_trainer.load_plan(r_path, name = 'testname')
s_path = '../data/example_strength.csv'
lu_trainer.load_plan(s_path, name = 'testname')

plan = lu_trainer.plans.pop()
lu_trainer.assign_plan(player=lu_player, plan=plan)


print(lu_player)
print(lu_player.plans)
lu_player.claim_training(plan)
print()
print(lu_player)
