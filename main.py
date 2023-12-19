from plot_generator import Cam, CamGrapher
from factors_solver import find_factors
from settings import BC, HEIGHT, RF_PHASE_ANGLE, ANGULAR_VELOCITY, RADIOUS

factors = find_factors(BC, RF_PHASE_ANGLE)
cam = Cam(factors, HEIGHT, RF_PHASE_ANGLE, RADIOUS)
camgrapher = CamGrapher(ANGULAR_VELOCITY, cam)

camgrapher.graph_velocity(1, 0.001)
camgrapher.graph_shape(0.01)

