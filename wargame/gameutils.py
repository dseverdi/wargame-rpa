import random


def weighted_random_selection(obj1, obj2):
    """ Slucajan odabir: 
        odaberi s vjerojatnošću 0.3 ranjavnanje Taliona, inače, neprijatelja 
    """

    # nacini listu 3x referencu na obj1, i 7x referenci na obj2
    weighted_list = 3 * [id(obj1)] + 7 * [id(obj2)] 
    selection = random.choice(weighted_list)

    # vrati obj1 ako si odabrao id(obj1) inače obj2
    return obj1 if selection == id(obj1) else obj2
    

# formatiranje ispisa
def print_bold(msg, end='\n'):
    print("\033[1m  {} \033[0m".format(msg),end='\n')