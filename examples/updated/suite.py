#!/usr/bin/env python

from expsuite import PyExperimentSuite
from numpy import *
import os



class Suite(PyExperimentSuite):

    restore_supported = True

    def reset(self, params, repeat):
        # initialize array
        self.numbers = zeros(params['iterations'])

        # seed random number generator
        random.seed(params['seed'])


    def iterate(self, params, repeat, iteration):
        # draw normally distributed random number
        self.numbers[iteration] = random.normal(params['mean'], params['std'])

        # calculate sample mean and offset
        samplemean = mean(self.numbers[:iteration])
        offset = abs(params['mean']-samplemean)

        # return dictionary
        ret = {'iteration':iteration,
               'number':self.numbers[iteration],
               'samplemean':samplemean,
               'offset':offset}

        return ret


    def save_state(self, params, repeat, iteration):
        # save array as binary file
        save(os.path.join(params['path'],
                          params['name'],
                          'array_%i.npy' % repeat), self.numbers)


    def restore_state(self, params, repeat, iteration):
        # load array from file
        self.numbers = load(os.path.join(params['path'],
                            params['name'],
                            'array_%i.npy' % repeat))



if __name__ == '__main__':
    suite = Suite()
    suite.start()
