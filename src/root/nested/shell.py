'''
Created on Jul 8, 2014

@author: Caroline
'''
import cmd, sys
import webbrowser

class Shell(cmd.Cmd):
    intro = 'Type youtube followed by a link. Type help or ? to list commands.\n'
    prompt = '> '
    file = None
    queue = []
    
    def do_youtube(self, arg):
        new = 2
        link = arg#parse(arg)
        self.queue.append(link)
        webbrowser.open(link,new=new)
        #print(link)
      

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    #return tuple(map(string, arg.split()))

if __name__ == '__main__':
    Shell().cmdloop()