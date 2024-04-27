from plot_generator import Cam, CamGrapher
from factors_solver import find_factors
from settings import BC, HEIGHT, RF_PHASE_ANGLE, ANGULAR_VELOCITY, RADIOUS

factors = find_factors(BC, RF_PHASE_ANGLE)
cam = Cam(factors, HEIGHT, RF_PHASE_ANGLE, RADIOUS)
camgrapher = CamGrapher(ANGULAR_VELOCITY, cam)

camgrapher.graph_torque()
# camgrapher.graph_displacement(0.25, 0.001)
# camgrapher.graph_velocity(0.25, 0.001)
# camgrapher.graph_acceleration(0.25, 0.00001)
# camgrapher.graph_shape()
# print(camgrapher.calculate_spring_force(0.25))
# camgrapher.graph_spring_force(1.2, 0.25)
# camgrapher.cam_eq()
