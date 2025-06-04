import os
import shutil
import sys
import unittest

from minifier import Minifier

class TestScriptMinify(unittest.TestCase):
    DIR_TEMP = "temp"
    PATH_SCRIPT = os.path.join(DIR_TEMP, "sample.sh")
    PATH_SCRIPT_MINIFIED = os.path.join(DIR_TEMP, "sample-minified.sh")
    PATH_ONE_LINE = os.path.join(DIR_TEMP, "oneline.txt")
    PATH_MULTILINE = os.path.join(DIR_TEMP, "multiline.txt")

    def test_if_fails_without_error(self):
        os.remove(self.PATH_SCRIPT)

        args = [
            "minifier.py",
            "-i",
            self.PATH_SCRIPT,
            "-o",
            self.PATH_SCRIPT_MINIFIED,
        ]

        sys.argv = args          
        
        minifier = Minifier()
        minifier.run()

        self.assertFalse(os.path.exists(self.PATH_SCRIPT_MINIFIED))
    
    def test_if_linearized_script_is_created(self):        
        args = [
            "main.py",
            "-i",
            self.PATH_SCRIPT,
            "-o",
            self.PATH_SCRIPT_MINIFIED,
        ]

        sys.argv = args          
        
        minifier = Minifier()
        minifier.run()

        self.assertTrue(os.path.exists(self.PATH_SCRIPT_MINIFIED))

    
    def test_if_linearized_script_runs_successful(self):
        args = [
            "main.py",
            "-i",
            self.PATH_SCRIPT,
            "-o",
            self.PATH_SCRIPT_MINIFIED,
        ]

        sys.argv = args          
        
        minifier = Minifier()
        minifier.run()

        one_liner = self._load_file(self.PATH_SCRIPT_MINIFIED)
        os.system(one_liner)

        self.assertTrue(os.path.exists(self.PATH_ONE_LINE))
        self.assertTrue(os.path.exists(self.PATH_MULTILINE))

        hi_there = self._load_file(self.PATH_ONE_LINE).splitlines()

        length_hi_there = len(hi_there)
        self.assertEqual(length_hi_there, 1)

        multiline = self._load_file(self.PATH_MULTILINE).splitlines()
        length_multiline = len(multiline)
        self.assertEqual(length_multiline, 4)
        

    def _load_file(self, path: str) -> str:
        if not os.path.exists(path):
            return None
        
        with open(path, "r") as reader:
            return reader.read()


    def setUp(self):
        self.begin_args = sys.argv.copy()

        if os.path.exists(self.DIR_TEMP):
            shutil.rmtree(self.DIR_TEMP, ignore_errors=True)

        os.makedirs(self.DIR_TEMP)

        sample_sh = f"""#!/bin/bash

ME=$(whoami)

mkdir -p temp

echo "Hi $ME" > {self.PATH_ONE_LINE}

MULTILINE="This is a 
multiline string
that will see if we can 
have this go into a single line"

echo $MULTILINE > {self.PATH_MULTILINE}
"""
        with open(self.PATH_SCRIPT, "w") as writer:
            writer.write(sample_sh)


    def tearDown(self):
        sys.argv = self.begin_args



if __name__ == "__main__":
    # Verbosity levels
    # 0 = quiet - Displays total number of tests executed and global result
    # 1 = default - Same as zero plus a dot for each successful test or an F for every failure
    # 2 = verbose - You get help string of every test and the result
    unittest.main(verbosity=2)
