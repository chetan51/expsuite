#!/usr/bin/env python

from matplotlib import pyplot as plt

from suite import Suite



if __name__ == '__main__':
  suite = Suite()

  from pylab import rcParams

  rcParams.update({'figure.autolayout': True})
  rcParams.update({'figure.facecolor': 'white'})
  rcParams.update({'ytick.labelsize': 8})
  rcParams.update({'figure.figsize': (12, 6)})

  experiments = suite.get_exps()
  print experiments

  plt.plot(suite.get_history(experiments[0], 0, 'offset'), linewidth=2, label='std=10')
  plt.plot(suite.get_history(experiments[1], 0, 'offset'), linewidth=2, label='std=5')
  plt.plot(suite.get_history(experiments[2], 0, 'offset'), linewidth=2, label='std=1')

  plt.legend()
  plt.show()
