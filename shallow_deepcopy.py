import copy

users = ['ajit',
         {'id': 1, 'name': 'Alice', 'active': True},
         {'id': 2, 'name': 'Bob', 'active': False},
         {'id': 3, 'name': 'Charlie', 'active': False},
         {'id': 4, 'name': 'David', 'active': True}
         ]

# Shallow copy
filtered_users = copy.copy(users)

# Modifying a top level and nested item respectively in original dict
users[0] = 'kumar'  # since this top level items change only the respective list gets changed
users[1]['name'] = 'wonder'

# Modifying a top level and nested item respectively in shallow copied dict
filtered_users[0] = 'Bob'  # since this top level items change only the respective list gets changed
filtered_users[1]['name'] = 'Merley'  # this change  appears in both the list

print(users)
print(filtered_users)
"""
import copy
original_dict = {'a': 1, 'b': {'x': 10, 'y': 20}}

# Deep copy
deep_copied_dict = copy.deepcopy(original_dict)
# Modifying a top level and nested item respectively in original dict
original_dict['a'] = 'Modified'
original_dict['b']['x'] = '10.5'

# Modifying a top level and nested item respectively in deep copied dict
deep_copied_dict['a'] = 'Changed'
deep_copied_dict['b']['x'] = '0.005'

print("Original dict:", original_dict)
print("Deep copied dict:", deep_copied_dict)
"""
