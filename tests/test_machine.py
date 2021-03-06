#!/usr/bin/env python
#
import unittest
import femagtools.machine

class PmMachineTest(unittest.TestCase):

  def test_char_ld_vector(self):
    m =   dict(p=4,
               r1=0.0806, le=0.0, ls=0.0,
               wind_temp=20.0,
               ld=[0.0014522728, 0.0014522728],
               lq=[0.0032154, 0.0038278836],
               psim=[0.11171972, 0.11171972],
               i1=[80.0],
               beta=[0.0, -41.1])

    pm = femagtools.machine.PmRelMachineLdq(3, m['p'],
                                            m['psim'],
                                            m['ld'],
                                            m['lq'],
                                            m['r1'],
                                            m['beta'],
                                            m['i1'])
    n = [50]
    u1 = 340.0
    T = [171.0]
    r = pm.characteristics(T, n, u1)
      
    self.assertAlmostEqual(r['i1'][0], 79.873, 2)
    self.assertAlmostEqual(r['u1'][0], 304.090, 2)
    self.assertAlmostEqual(r['beta'][0], -39.27, 2)
    self.assertAlmostEqual(r['cosphi'][0], 0.7584, 2)

  def test_char_ld_scalar(self):
     m =   dict(p=4,
                r1=0.0806, le=0.0, ls=0.0,
                wind_temp=20.0,
                ld=0.0014522728,
                lq=0.0038278836,
                psim=0.11171972)

     pm = femagtools.machine.PmRelMachineLdq(3, m['p'],
                                             m['psim'],
                                             m['ld'],
                                             m['lq'],
                                             m['r1'])

     n = [50]
     u1 = 340
     T = [171]
     r = pm.characteristics(T, n, u1)
      
     self.assertAlmostEqual(r['i1'][0], 79.2, 2)
     self.assertAlmostEqual(r['u1'][0], 321.77, 2)
     self.assertAlmostEqual(r['beta'][0], -35.04, 2)
     self.assertAlmostEqual(r['cosphi'][0], 0.7225, 2)

  def test_char_psid_array(self):
    m = dict(p=6,
             r1=0.0, ls=0.0, le=0.0,
             wind_temp=50.0,
             u1=1500.0,
             rwdg=1.0,
             rlen=1.0,
      
             psid=[
               [-2.2155, -1.8844, -1.5092, -1.10915, -0.69265,
                -0.26285, 0.172865, 0.61355, 1.0584, 1.5064, 1.95335],
               [-2.19485, -1.8669, -1.4938, -1.0941, -0.67725, -0.24738,
                0.187985, 0.6272, 1.0682, 1.51025, 1.94215],
               [-2.1329, -1.8102, -1.4462, -1.04965, -0.6349, -0.206885,
                0.224, 0.6545, 1.0815, 1.49485, 1.8851],
               [-2.03525, -1.7199, -1.36535, -0.98, -0.5754, -0.15967,
                0.25879, 0.66955, 1.0626, 1.4385, 1.79655],
               [-1.9173, -1.6093, -1.2698, -0.90125, -0.51485, -0.119,
                0.275275, 0.65555, 1.01955, 1.3699, 1.701],
               [-1.7885, -1.49205, -1.17005, -0.8246, -0.462, -0.09093,
                0.27622, 0.62895, 0.9702, 1.2943, 1.6002],
               [-1.66845, -1.38355, -1.077, -0.75285, -0.41545, -0.07042,
                0.269535, 0.5971, 0.91455, 1.2166, 1.50255],
               [-1.5582, -1.2824, -0.99505, -0.6902, -0.37485, -0.054705,
                0.259315, 0.56385, 0.85995, 1.1445, 1.4154],
               [-1.45355, -1.1977, -0.9233, -0.63665, -0.34132, -0.04326,
                0.247065, 0.5327, 0.81027, 1.08395, 1.3391],
               [-1.37165, -1.12385, -0.861, -0.59115, -0.313635, -0.032998,
                0.23457, 0.50435, 0.76615, 1.0206, 1.27015],
               [-1.2964, -1.0563, -0.8085, -0.55265, -0.290255, -0.0242655,
                0.22365, 0.4781, 0.7273, 0.9695, 1.20785]],
             psiq=[
               [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
               [0.67305, 0.71225, 0.7448, 0.7742, 0.8043, 0.83475, 0.86415,
                0.89075, 0.9114, 0.92225, 0.91105],
               [1.28765, 1.36675, 1.43815, 1.4997, 1.55505, 1.60545, 1.64955,
                1.6842, 1.70135, 1.68245, 1.6212],
               [1.8046, 1.91135, 2.00865, 2.093, 2.1637, 2.21795, 2.25435,
                2.26765, 2.2484, 2.1966, 2.1182],
               [2.2078, 2.32575, 2.43425, 2.5235, 2.59035, 2.6355, 2.6565,
                2.64845, 2.61345, 2.55395, 2.46855],
               [2.50495, 2.6215, 2.7293, 2.81575, 2.8784, 2.91515, 2.92425,
                2.90745, 2.8665, 2.8007, 2.7104],
               [2.7314, 2.8406, 2.9358, 3.01385, 3.0695, 3.10065, 3.1052,
                3.08385, 3.03905, 2.9736, 2.8889],
               [2.91375, 3.0086, 3.0926, 3.1605, 3.20775, 3.23295, 3.234,
                3.2116, 3.1689, 3.10765, 3.03275],
               [3.0632, 3.14755, 3.22035, 3.27915, 3.31905, 3.33935, 3.3376,
                3.3159, 3.27845, 3.2298, 3.1556],
               [3.19795, 3.2683, 3.3327, 3.38205, 3.4153, 3.4335, 3.42895,
                3.409, 3.37505, 3.3271, 3.2662],
               [3.31205, 3.38765, 3.43315, 3.47515, 3.5035, 3.521, 3.514,
                3.4958, 3.46395, 3.4216, 3.36875]],
             Id=[-600.0, -540.0, -480.0, -420.0, -360.0,
                 -300.0, -240.0, -180.0, -120.0, -60.0, 0.0],
             iq=[0.0, 60.0, 120.0, 180.0, 240.0, 300.0,
                 360.0, 420.0, 480.0, 540.0, 600.0])


    pm = femagtools.machine.PmRelMachinePsidq(3, m['p'],
                                              m['psid'],
                                              m['psiq'],
                                              m['r1'],
                                              m['Id'], m['iq'])
        
    n = [16.67]
    u1 = 1400
    T = [5600.0]
    r = pm.characteristics(T, n, u1)
  
    self.assertAlmostEqual(r['i1'][0], 207.74350, 2)
    self.assertAlmostEqual(r['u1'][0], 1192.88, 2)
    self.assertAlmostEqual(r['beta'][0], -38.01, 2)
    self.assertAlmostEqual(r['cosphi'][0], 0.788, 2)

  def test_char_ldd_fieldweakening(self):
    m = dict(
      p=6,
      r1=0.0,
      ld=[0.005152],
      lq=[0.0104825],
      psim=[1.1298],
      beta=[0.0],
      i1=[0.0])

    pm = femagtools.machine.PmRelMachineLdq(3, m['p'],
                                            m['psim'],
                                            m['ld'],
                                            m['lq'],
                                            m['r1'],
                                            m['beta'],
                                            m['i1'])

    n = [16.67]
    u1 = 1400
    T = [5600.0]
    r = pm.characteristics(T, n, u1)
  
    self.assertAlmostEqual(r['i1'][0], 211.971, 2)
    self.assertAlmostEqual(r['u1'][0], 1263.721, 2)
    self.assertAlmostEqual(r['beta'][0], -30.0, 2)
    self.assertAlmostEqual(r['cosphi'][0], 0.729, 2)

  def test_i1beta_char(self):
    m = dict(
      p=4,
      r1=0.055,
      ld=[0.0012634272, 0.0012634272],
      lq=[0.0027257272, 0.003158568],
      psim=[0.11171972, 0.11171972],
      beta=[0.0,-35.0],
      i1=[100.0])
      
    pm = femagtools.machine.PmRelMachineLdq(3, m['p'],
                                            m['psim'],
                                            m['ld'],
                                            m['lq'],
                                            m['r1'],
                                            m['beta'],
                                            m['i1'])

    n = [50]
    u1 = 340
    T = [171]
    r = pm.characteristics(T, n, u1)
      
    self.assertAlmostEqual(r['i1'][0], 84.9758, 2)
    self.assertAlmostEqual(r['u1'][0], 278.48, 2)
    self.assertAlmostEqual(r['beta'][0], -38.02, 2)
    self.assertAlmostEqual(r['cosphi'][0], 0.774, 2)
      

  def test_torque_iqd(self):
    m1 = femagtools.machine.PmRelMachineLdq(3, 4,
                                            psim=0.11172,
                                            ld=1.2667e-3,
                                            lq=3.1477e-3)
    beta = -35 * 3.1415/180
    i1 = 100
    iq, id = femagtools.machine.iqd(beta, i1)
    self.assertAlmostEqual(m1.torque_iqd(iq, id), 215.87, 2)

    beta = [-35, 0]
    i1 = [100]
    ld = [0.0012667696, 0.0012667696]
    lq = [0.0031477052, 0.0027165356]
    psim = [0.1117197, 0.1117197]

    m2 = femagtools.machine.PmRelMachineLdq(3, 4,
                                            psim=psim,
                                            ld=ld,
                                            lq=lq,
                                            beta=beta,
                                            i1=i1)
    self.assertAlmostEqual(m2.torque_iqd(iq, id), 215.87, 2)

if __name__ == '__main__':
  unittest.main()

