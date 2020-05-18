#MFDFA-Analytics-by-SKDataScience
#multifractal DFA singularity spectra - module 04
#Version 3.0 - Modified by R.R.Rosa - Dec 2018 - mfdfa_ss_m4.py
#This module is the entry point for testing the modified first-order uni- and multifractal DFA methods.
#The initial dataset is a time series of size 2ˆn (tseries.txt)

import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

## Loading data
#dx = loadtxt('tseries.txt')
#size=8192
#dx = dx[1 - 1 : 8192]               # We take the first 8192 samples

## Computing
# Modified first-order DFA
[timeMeasure, meanDataMeasure, scales] = getHurstByUpscaling(dx)                    # Set of parameters No. 1
#[timeMeasure, meanDataMeasure, scales] = getHurstByUpscaling(dx, 3.0, 0, 2.0)       # Set of parameters No. 2

[bScale, bDM, bsIndex, HMajor, HMinor] = getScalingExponents(timeMeasure, meanDataMeasure)

# Modified first-order MF-DFA
[_, dataMeasure, _, stats, q] = getMSSByUpscaling(dx, isNormalised = 1)

## Output
# Modified first-order DFA
plt.figure()
plt.subplot(2, 1, 1)
plt.loglog(timeMeasure, meanDataMeasure, 'ko-')
plt.xlabel(r'$\mu(t)$')
plt.ylabel(r'$\mu(\Delta x)$')
plt.grid('on', which = 'minor')
plt.title('Modified First-Order DFA of a Multifractal Noise')

plt.subplot(2, 1, 2)
plt.loglog(scales, meanDataMeasure, 'ko-')
plt.loglog(bScale, bDM, 'ro')
plt.xlabel(r'$j$')
plt.ylabel(r'$\mu(\Delta x)$')
plt.grid('on', which = 'minor')

# Modified first-order MF-DFA
print('alpha_min = %g, alpha_max = %g, dalpha = %g' % (stats['LH_min'], stats['LH_max'], stats['LH_max'] - stats['LH_min']))
print('h_min = %g, h_max = %g, dh = %g\n' % (stats['h_min'], stats['h_max'], stats['h_max'] - stats['h_min']))


plt.figure()
nq = np.int(len(q))
leg_txt = []
for qi in range(1, nq + 1):
    llh = plt.loglog(scales, dataMeasure[qi - 1, :], 'o-')
    leg_txt.append('tau = %g (q = %g)' % (stats['tau'][qi - 1], q[qi - 1]))
plt.xlabel(r'$j$')
plt.ylabel(r'$\mu(\Delta x, q)$')
plt.grid('on', which = 'minor')
plt.title('Modified First-Order MF-DFA of a Multifractal Noise')
plt.legend(leg_txt)

plt.figure()

#plt.subplot(2, 1, 1)
plt.plot(q, stats['tau'], 'ko-')
plt.xlabel(r'$q$')
plt.ylabel(r'$\tau(q)$')
plt.grid('on', which = 'major')
plt.title('Statistics of Modified First-Order MF-DFA of a Multifractal Noise')

plt.figure()

#plt.subplot(2, 1, 2)
plt.plot(stats['LH'], stats['f'], 'ko-')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$f(\alpha)$')
plt.grid('on', which = 'major')


plt.show()