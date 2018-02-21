#!/usr/bin/env python
"""
finite_automata.py

Description:
  Creates DFA/NFA objects that can be drawn in dot format.

@author Jesse Opitz
"""

# Custom python files
from state import *
from edge import *

class finite_automata:
    """
    Object containing 5 tuple needed for creating an NFA or DFA.
    
    @type   states:      list of type state
    @type   alphabet:    string
    @type   transitions: list of type edge
    @type   init_state:  string
    @type   acc_state:   list of type state
    """
    def __init__(self):
        # List of states
        self.states = []
        
        # Alphabet
        self.alphabet = ''
        
        # List of transitions
        self.transitions = []

        # Initial/start state
        self.init_state = ''

        # List of accepting states
        self.acc_states = []
    
    def draw(outfile):
        print 'draw finite automata'
    
    def set_alphabet(self, ab):
        self.alphabet = ab

    def get_alphabet(self):
        # returns string of alphabet
        return repr(self.alphabet)

    def add_state(self, name, is_init, is_acc):
        new_state = State(name, is_init, is_acc)
        self.states.append(new_state)

    #def rem_state(self, state_name):
    #    print 'remove', state_name
    
    def add_transition(self, name, source, target):
        new_edge = Edge(name, source, target)
        self.transitions.append(new_edge)

    #def rem_transition(self, edge_name):
    #     print 'remove', edge_name

    #def rem_acc_state(self, state):
        # go through list of states
        # change state status is_acc = False
        # rem from list of acc_states
   #     print 'remove', state
    
    def get_states(self):
        # returns a string of states
        return self.states

    def get_transitions(self):
        # returns list of transitions
        return self.transitions

    def get_init(self):
        # returns initial state
        return self.init_state

    def get_acc_state(self):
        # returns list of accepting states
        return self.acc_state

    def print_transitions(self):
        # returns a string of a list of transitions
        t = []
        for t in self.transitions:
            t.append('(' + t.get_source() + ',' + t.get_name() + ') = ' +t.get_target())
                    
        return t

    def print_acc_states(self):
        # returns a string of a list of accepting states
        a = []
        for a in self.acc_state:
            a.append(acc_state.get_name())

        return a

    def print_five_tuple(self):
        print "States:"
        for s in self.states:
            print '-->', s.get_name()
        print "Alphabet:", self.get_alphabet()
        print "Transitions:"
        for t in self.transitions:
            print '-->(' + t.get_source() + ',' + t.get_name() + ') = ' +t.get_target()
        print "Initial State:"
        for s in self.states:
            if s.get_init():
                print '-->', s.get_name()
                pass
        print "Accepting States:"
        for s in self.states:
            if s.get_acc():
                print '-->', s.get_name()
                pass
