#!/usr/bin/env python
#
import unittest
import os
import femagtools.tks

class TksReaderTest(unittest.TestCase):
    def test_read_tks( self ):
        testPath = os.path.split(__file__)[0]
        if not testPath: testPath='.'
        filename = "data/TKS-M400-65A.txt"
        tks = femagtools.tks.Reader('{0}/{1}'.format(testPath, filename))
        r = tks.getValues()
        self.assertEqual(r['name'], 'TKS-M400-65A') 
        self.assertEqual(len(r['losses']['f']), 4) 
        self.assertEqual(len(r['losses']['B']), 13) 
        self.assertEqual(len(r['losses']['pfe']), 13) 
        self.assertEqual(len(r['losses']['pfe'][0]), 4) 
        self.assertAlmostEqual(r['losses']['f'][-1], 400.0, 1) 
        self.assertAlmostEqual(r['losses']['B'][-1], 1.8, 3) 
        self.assertAlmostEqual(r['losses']['pfe'][3][-1], 30.841, 2) 
if __name__ == '__main__':
  unittest.main()
