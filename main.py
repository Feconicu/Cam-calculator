from plot_generator import Cam, CamGrapher
from factors_solver import find_factors
from settings import BC, HEIGHT, RF_PHASE_ANGLE, ANGULAR_VELOCITY

factors = find_factors(BC, RF_PHASE_ANGLE)
cam = Cam(factors, HEIGHT, RF_PHASE_ANGLE)
camgrapher = CamGrapher(ANGULAR_VELOCITY, cam)
camgrapher.graph_velocity(1, 0.0000001)
camgrapher.graph_displacement(1, 0.0000001)
