class RandomizedSet:
    '''
                                    element_to_remove = 7

                                before:     [4, 7, 9, 3, 5]
                                after:      [4, 5, 9, 3]

                                before:     {4:0, 7:1, 9:2, 3:3, 5:4}
                                after:      {4:0, 9:2, 3:3, 5:1}

    '''

    def __init__(self):
        self.data_map = {} # dictionary, aka map, aka hashtable, aka hashmap
        self.data = [] # list aka array

    def insert(self, val: int) -> bool:

      
        if val in self.data_map:
            return False
        
        self.data_map[val] = len(self.data)

        # add to the list
        self.data.append(val)
        
        return True

    def remove(self, val: int) -> bool:

      
        if not val in self.data_map:
            return False

       
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        self.data[-1] = val

        # remove the last element in the list
        self.data.pop()

        # remove the element to be removed from the dictionary
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        
        return random.choice(self.data)