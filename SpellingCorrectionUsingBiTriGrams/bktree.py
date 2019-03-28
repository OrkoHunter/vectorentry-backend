from collections import deque

from .utility import distance_function

class BKTree(object):
    def __init__(self, items_list = None, items_dict = None):
        if items_list is None:
            items_list = []

        if items_dict is None:
            items_dict = {} 

        self.tree = None
        
        for item in items_list:
            self.add(item)
        
        for item in items_dict:
            self.add(item)
    
    def add(self, item):
        node = self.tree
        
        if self.tree is None:
            self.tree = (item, {})
            return
        
        while True:                              ## for a single distance i.e. for each corresponding distance 1, 2, 3, etc., have only one item 
            parent, children = node
            dist = distance_function(item, parent)
            node = children.get(dist)
            if node is None:
                children[dist] = (item, {})
                break
    
    def find(self, item, n):
        if self.tree is None:
            return []
        
        candidates = deque([self.tree])
        found = []
        
        while candidates:
            candidate, children = candidates.popleft()
            dist = distance_function(item, candidate)
            if dist <= n:
                found.append((dist, candidate))
            
            if children:                          ##??
            	## check for range [d-n, d+n)
                lower = dist - n   
                upper = dist + n
                candidates.extend(c for d, c in children.items() if abs(lower) <= d < upper)

        found.sort()
        return found
    
    def __iter__(self):
        if self.tree is None:
            return
        
        candidates = deque([self.tree])
        
        while candidates:
            candidate, children = candidates.popleft()
            yield candidate
            candidates.extend(children.values())