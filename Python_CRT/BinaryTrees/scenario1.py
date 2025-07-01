'''
Employee Hierarchy Tree (Binary Tree)
Contest A company stores employees in a reporting structure where each manager
 has two direct reports max.
Beginner-Friendly Tashs:
-Build a binary tree where each node is an employee and children are 
subordinates.
-Print all employee names in In-Order, Pre-Order, and Post-Order traversal
-Count how many employees are at the lowest level (leaf nodes).
-Find the depth of the hierarchy (height of the tree)
-Find the manager of a given employee by traversing the tree.
'''
class EmployeeNode:
    def __init__(self, name):
        self.name = name
        self.left = None  
        self.right = None  

class EmployeeHierarchy:
    def __init__(self, ceo_name):
        self.root = EmployeeNode(ceo_name)

    def insert(self, manager_name, left_name=None, right_name=None):
        # Insert left and right subordinates under the manager
        manager_node = self.find(self.root, manager_name)
        if not manager_node:
            print(f"Manager {manager_name} not found.")
            return
        if left_name:
            manager_node.left = EmployeeNode(left_name)
        if right_name:
            manager_node.right = EmployeeNode(right_name)

    def find(self, node, name):
        # Helper to find a node by name
        if not node:
            return None
        if node.name == name:
            return node
        left = self.find(node.left, name)
        if left:
            return left
        return self.find(node.right, name)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.name)
            self.in_order(node.right)

    def pre_order(self, node):
        if node:
            print(node.name)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.name)

    def count_leaves(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return self.count_leaves(node.left) + self.count_leaves(node.right)

    def find_height(self, node):
        if not node:
            return 0
        return 1 + max(self.find_height(node.left), self.find_height(node.right))

    def find_manager(self, node, employee_name, manager=None):
        if not node:
            return None
        if node.name == employee_name:
            return manager
        left = self.find_manager(node.left, employee_name, node.name)
        if left:
            return left
        return self.find_manager(node.right, employee_name, node.name)

# Build the hierarchy
company = EmployeeHierarchy("CEO")
company.insert("CEO", "Manager1", "Manager2")
company.insert("Manager1", "Employee1", "Employee2")
company.insert("Manager2", "Employee3", "Employee4")

print("\nIn-Order Traversal:")
company.in_order(company.root)

print("\nPre-Order Traversal:")
company.pre_order(company.root)

print("\nPost-Order Traversal:")
company.post_order(company.root)

print("\nNumber of employees at the lowest level (leaf nodes):")
print(company.count_leaves(company.root))

print("\nDepth of the hierarchy (height of the tree):")
print(company.find_height(company.root))

print("\nFind manager of Employee3:")
manager_of_emp3 = company.find_manager(company.root, "Employee3")
if manager_of_emp3:
    print(f"Manager of Employee3 is {manager_of_emp3}")
else:
    print("Employee not found.")
