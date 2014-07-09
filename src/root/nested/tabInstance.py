'''
Created on May 23, 2014

@author: Caroline
'''

class tabInstance(object):
    '''
    A class for a tab. should be implemented in subclasses.
    '''


    def __init__(self, player, tabid):
        self.playerType = player
        self.tabid = tabid