'''
Created on Jul 8, 2014

@author: Caroline
'''
class queue:
    def __init__(self):
        q = []
    def add(self, tabinstance):
        'Pass this a tabInstance to add it to the queue'
        self.q.append(tabinstance)
    
    def getNext(self):
        return self.q.pop()