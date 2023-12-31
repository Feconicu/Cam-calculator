import numpy as np

HEIGHT = 6                                      #maximum displacement in millimeters
RADIOUS = 14                                     #base circle radious in mm
RF_PHASE_ANGLE = 180                             #sum of angles of rise and fall phases
BC = np.array([                                 #Boundry conditions Table - each row must be in [position (deg), lift (mm), velocity (mm/deg), acceleration (mm/deg^2)]
    [       0,      0,    0,    0],
    [RF_PHASE_ANGLE/2, HEIGHT, None, None],
    [  RF_PHASE_ANGLE,      0,    0,    0],
])

ANGULAR_VELOCITY = 3600                          #in deg/s
