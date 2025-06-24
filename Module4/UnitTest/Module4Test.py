import unittest
import os

from Module4.Module4 import cleanFiles, genFiles

class TestCleanFiles(unittest.TestCase):

    def setUp(self):
        self.testWrite = "Module4/UnitTest/testWrite.txt"
        self.testAppend = "Module4/UnitTest/testAppend.txt"
        genFiles(self.testWrite, self.testAppend)

    def test_clean_files(self):
        with open(self.testWrite, 'r') as f:
            ogWrite = f.readlines()
        with open(self.testAppend, 'r') as f:
            ogAppend = f.readlines()

        cleanFiles(self.testWrite, self.testAppend)

        with open(self.testWrite, 'r') as f:
            clWrite = f.readlines()
        with open(self.testAppend, 'r') as f:
            clAppend = f.readlines()

        # Check total rows match
        self.assertEqual(len(ogWrite) + len(ogAppend), len(clWrite) + len(clAppend))

        # Check no 'no' in cleaned write file
        for line in clWrite:
            self.assertNotIn('no', line)

        # Optional: Check data integrity
        for line in clWrite:
            self.assertIn(line, ogWrite)

    def tearDown(self):
        os.remove(self.testWrite)
        os.remove(self.testAppend)

if __name__ == '__main__':
    unittest.main()