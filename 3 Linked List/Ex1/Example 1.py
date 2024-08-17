# Import .py from another folder
"""import sys

sys.path.insert(0, 'D:/3. Work/13. Python/Data_Structure_and_Algorithm/3 Linked List')
"""
from Linked_list import *

ll = Linked_list()
ll.insert_value(["banana", "mango", "grapes", "orange"])
ll.print_LL()
ll.insert_after_value("mango", "apple")  # insert apple after mango
ll.print_LL()
ll.remove_by_value("orange")  # remove orange from linked list
ll.print_LL()
ll.remove_by_value("figs")
ll.print_LL()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print_LL()
