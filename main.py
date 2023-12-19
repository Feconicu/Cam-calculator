from plot_generator import Cam, CamGrapher
from factors_solver import find_factors
from settings import BC, HEIGHT, RF_PHASE_ANGLE

factors = find_factors(BC, RF_PHASE_ANGLE)
cam = Cam(factors, HEIGHT, RF_PHASE_ANGLE)
