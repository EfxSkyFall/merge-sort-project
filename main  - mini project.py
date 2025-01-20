## main
from merge_sort import *
from utils import *
def main_main()
    print("Welcome to the merge Sort Program!")
    rdm_list()
    print_lst()
    sorted_list = merge_sort(lst)
    go = input("Do you want to sort another list? yes/no : ")
    if go == "yes":
        main_main()
    else:
        break
    
