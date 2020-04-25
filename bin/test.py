from trainapp import *

lu_acc = Account(name='lu')
lu_trainer = lu_acc.add_trainer_role()
lu_player = lu_acc.add_player_role()

r_path = '../data/example_running.csv'
lu_trainer.load_plan(r_path, name = 'running')
s_path = '../data/example_strength.csv'
lu_trainer.load_plan(s_path, name = 'strength')

for plan in lu_trainer.plans:
    lu_trainer.assign_plan(player=lu_player, plan=plan)


lu_player.show_plans()
for plan in lu_player.plans:
    print(plan)
    lu_player.claim_training(plan)

print()
print(lu_player)
