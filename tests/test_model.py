#!/usr/bin/env python
#
import unittest
import femagtools

modelpars = dict(
    name="PM 130 L4",
    lfe=0.1,
    poles=4,
    stator=dict(
        yoke_diam=0.13,
        zeroangle=0.0,
        num_slots=12,
        inside_diam=0.07,
        mcvNameYoke="3",
        num_slots_gen=3,
        nodedist=1.5,
        rlength=1.0))


class ModelTest(unittest.TestCase):

    def test_getset(self):
        m = dict(modelpars)
        m['stator']['statorRotor3'] = dict(
            slot_h1=0.002,
            slot_h2=0.004,
            middle_line=0,
            tooth_width=0.009,
            wedge_width2=0.0,
            wedge_width1=0.0,
            slot_top_sh=0,
            slot_r2=0.002,
            slot_height=0.02,
            slot_r1=0.003,
            slot_width=0.003)
        model = femagtools.MachineModel(m)
        attr = 'stator.statorRotor3.slot_height'.split('.')
        self.assertEqual(model.get(attr), 20e-3)
        newvalue = 1
        model.set_value(attr, newvalue)
        self.assertEqual(model.get(attr), newvalue)

if __name__ == '__main__':
    unittest.main()

