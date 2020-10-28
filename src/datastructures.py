
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{
            'id': 1,
            'first_name': 'John',
            'last_name': 'Jackson', 
            'age': 33,
            'lucky_numbers': [7,13,22]
            },
        {
            'id': 2,
            'first_name': 'Jane',
            'last_name': 'Jackson', 
            'age': 35,
            'lucky_numbers': [10,14,3]
        },
        
        {
                
            'id': 3,
            'first_name': 'Jimmy',
            'last_name': 'Jackson', 
            'age': 5,
            'lucky_numbers': [1]

        }]



    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99)

    def add_member(self, member):
        # fill this method and update the return
        if 'id' in member:
            self._members.append(member)
        else:
            member['id'] = self._generateId()
            self._members.append(member)
        return None
        

    def delete_member(self, id):
        # fill this method and update the return
        for position in range(len(self._members)):
            print("this is position",position)
            print("this is member",self._members)
            if self._members[position]['id'] == id:
                self._members.pop(position)
        return None
        

    def get_member(self, id):
        # fill this method and update the return
        for all_members in self._members:
            if all_members['id'] == int(id):
                return all_members
        return 'member does not exist'
    
    def get_name_member(self, name):
        # fill this method and update the return
        for all_members in self._members:
            if all_members['first_name'] == name:
                return all_members
            
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        if len(self._members) > 0:
            return self._members
        else:
            return "array is empty"