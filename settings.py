import numpy as np

##############################################################################
    # cam parameters #
##############################################################################

HEIGHT = 18                                     #maximum displacement in millimeters
RADIOUS = 30                                    #base circle radious in mm
RF_PHASE_ANGLE = 180                            #sum of angles of rise and fall phases
BC = np.array([                                 #Boundry conditions Table - each row must be in [position (deg), lift (mm), velocity (mm/deg), acceleration (mm/deg^2)]
    [       0,      0,    0,    0],
    [RF_PHASE_ANGLE/2, HEIGHT, None, None],
    [  RF_PHASE_ANGLE,      0,    0,    0],
])

ANGULAR_VELOCITY = 1260                         #in deg/s
FRICTION_COEFFICIENT = 0.6  #wcześniej liczono dla 0,8

##############################################################################
    # spring parameters #
##############################################################################

INITIAL_FORCE = 0.31                            # N
SPRING_CONSTANT = 0.02                          # N/mm
NUMBER_OF_SPRINGS = 4
MINIMUM_DISPLACEMENT = 22.6                     # mm
MAXIMUM_DISPLACEMENT = 40.6                     # mm
##############################################################################
    # platform parameters #
##############################################################################

FOLLOWER_MASS = 0.25                            # kg
