## utils
import random
def rdm_list():
       size = int(input("How many values do you want in this list ?"))
       lowb = int(input("Enter the lower bound of the list : "))
       upb = int(input("Enter the upper bound of the list : "))
       lst = []
       random.randint(size,lowb,upb).append(lst)


def print_lst(lst):
    print("your unsorted list is : ",lst)

              
