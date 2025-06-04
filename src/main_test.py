import os
import shutil
import sys
import unittest

from main import Main

class TestMain(unittest.TestCase):
    PATH_INPUT = "scripts/sample.sh"
    DIR_TEMP = "temp"
    PATH_OUTPUT = "temp/sample-linearized.sh"
    
    def test_linearize(self):        
        args = [
            "main.py",
            "-i",
            self.PATH_INPUT,
            "-o",
            self.PATH_OUTPUT,
        ]

        sys.argv = args          
        
        main = Main()
        main.run()

        assert os.path.exists(self.PATH_OUTPUT)


    def setUp(self):
        self.begin_args = sys.argv.copy()
        if os.path.exists(self.DIR_TEMP):
            shutil.rmtree(self.DIR_TEMP, ignore_errors=True)


    def tearDown(self):
        sys.argv = self.begin_args
        if os.path.exists(self.DIR_TEMP):
            shutil.rmtree(self.DIR_TEMP, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
