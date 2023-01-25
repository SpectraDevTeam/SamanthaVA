import unittest
import sys, io
import importlib

class TestCommandFunctions(unittest.TestCase):

    def test_endprogram_inputcheck(self):
        module = importlib.import_module("commands.endprogram")
        self.assertTrue(module.command_matches_input('end task'))
    
    def test_flip_inputcheck(self):
        module = importlib.import_module("commands.flip")
        self.assertTrue(module.command_matches_input('flip a coin'))
            
    def test_joke_inputcheck(self):
        module = importlib.import_module("commands.joke")
        self.assertTrue(module.command_matches_input('tell me a joke'))
            
    def test_roll_inputcheck(self):
        module = importlib.import_module("commands.roll")
        self.assertTrue(module.command_matches_input('roll a d20'))
            
    def test_settimer_inputcheck(self):
        module = importlib.import_module("commands.settimer")
        self.assertTrue(module.command_matches_input('set a timer for 20 mins'))
            
    def test_time_inputcheck(self):
        module = importlib.import_module("commands.time")
        self.assertTrue(module.command_matches_input('tell me the time'))
        

        

        
    
if __name__ == '__main__':
    unittest.main()
