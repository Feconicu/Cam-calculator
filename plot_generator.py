
import matplotlib.pyplot as plt
from math import sin, cos, radians, atan, tan, pi
from settings import FOLLOWER_MASS, INITIAL_FORCE, MINIMUM_DISPLACEMENT, SPRING_CONSTANT, ANGULAR_VELOCITY, FRICTION_COEFFICIENT, \
    NUMBER_OF_SPRINGS

class Cam:
    def __init__(self, factors, height, rf_angle, radious):
        self.factors = factors
        self.height = height
        self.rf_angle = rf_angle
        self.radious = radious

    def __dir__(self):
        return self.factors, self.height, self.rf_angle, self.radious

    def calculate_displacement(self, angle):
        """"returns value in mm"""
        angle %= 360
        if angle >= self.rf_angle:
            return 0
        s = 0
        for pow, C in enumerate(self.factors):
            s += C*((angle/self.rf_angle))**pow
        return s

    def calculate_velocity(self, angle):
        """returns value in mm/deg"""
        angle %= 360
        if angle >= self.rf_angle:
            return 0
        v = 0
        for index, C in enumerate(self.factors):
                v += index/self.rf_angle*C*(angle/self.rf_angle)**(index-1) if index-1 > -1 else 0
        return v

    def calculate_acceleration(self, angle):
        angle %= 360
        if angle >= self.rf_angle:
            return 0
        a = 0
        for index, C in enumerate(self.factors):
            a += (C*index*(index-1)*((angle/self.rf_angle)**(index-2)))/(self.rf_angle**2) if index > 1 else 0
        return a


class CamGrapher(Cam):
    def __init__(self, ang_speed, cam_or_factors, *args):
        self.ang_speed = ang_speed
        if isinstance(cam_or_factors, Cam):
            super().__init__(*cam_or_factors.__dir__())
        else:
            super().__init__(cam_or_factors ,*args)
        print(self.factors)
        self.max_acceleration = None
  
    def graph_displacement(self, time_limit = 1, step = 0.01):
        time_axis = []
        displacement_axis = []
        t = 0
        while t < time_limit:
            time_axis.append(t)
            displacement_axis.append(super().calculate_displacement(self.ang_speed*t))
            t += step
        plt.plot(time_axis, displacement_axis)
        plt.xlabel('t [s]')
        plt.ylabel('s [mm]')
        plt.title('s(t)')
        plt.show()

    def graph_velocity(self, time_limit = 1, step = 0.01):
        time_axis = []
        velocity_axis = []
        t = 0
        while t < time_limit:
            time_axis.append(t)
            velocity_axis.append(self.ang_speed*super().calculate_velocity(self.ang_speed*t))
            t += step
        plt.plot(time_axis, velocity_axis)
        plt.xlabel('t [s]')
        plt.ylabel('v [mm/s]')
        plt.title('v(t)')
        plt.show()

    def graph_acceleration(self, time_limit = 1, step = 0.1, dont_show = False):
        time_axis = []
        acceleration_axis = []
        t = 0
        while t < time_limit:
            time_axis.append(t)
            acceleration_axis.append((self.ang_speed**2)*self.calculate_acceleration(self.ang_speed*t))
            t +=step
        self.max_acceleration = max(acceleration_axis, key=abs)
        if not dont_show:
            plt.plot(time_axis, acceleration_axis)
            plt.xlabel('t [s]')
            plt.ylabel('a [mm/s^2]')
            plt.title('a(t)')
            plt.show()

    def graph_shape(self, step = 0.1):
        x_cord = []
        y_cord = []
        angle = 0
        while angle < 360:
            x_cord.append(self.radious*cos(radians(angle+self.rf_angle)))
            y_cord.append(self.radious*sin(radians(angle+self.rf_angle)))
            if angle <= self.rf_angle:
                s_sum_r = self.calculate_displacement(angle) + self.radious
                v_over_omega = self.calculate_velocity(angle)
                first_part = (s_sum_r/cos(atan(v_over_omega/s_sum_r)))
                second_part_argument = pi/2-radians(self.rf_angle)+radians(angle)+atan(v_over_omega/s_sum_r)
                x_cord.append(first_part*cos(second_part_argument))
                y_cord.append(first_part*sin(second_part_argument))
            angle += step
        plt.scatter(x_cord, y_cord, marker='o', color='blue', s=5)
        plt.xlim(-20,20)
        plt.ylim(-20,20)
        plt.axis('equal')
        plt.show()

    def calculate_spring_force(self, mass):
        if self.max_acceleration is None:
            self.graph_acceleration(dont_show=True, step = 0.001)
        force = (abs(self.max_acceleration/1000) - 9.81)*1.5*mass
        torque = (force + mass*9.81)*(self.height+self.radious)/1000
        print('spring force: ', force)
        print('max_torque: ', torque)

    def graph_spring_force(self, safety_factor, mass, step=0.01):
        gamma = 90
        s_axis = []
        force_axis = []
        while gamma <= 180:
            accel = ((-1)*self.ang_speed**2*self.calculate_acceleration(gamma)/1000 - 9.810)
            accel = accel if accel > 0 else 0
            s_axis.append(self.calculate_displacement(gamma))
            force_axis.append(accel*safety_factor*mass)
            gamma += step
        plt.plot(force_axis, s_axis)
        plt.ylabel('s [mm]')
        plt.xlabel('P [N]')
        plt.title('P(t)')
        plt.show()

    def get_shape_inventor_equation(self):
        s_i = f'{self.radious}'
        for i, factor in enumerate(self.factors):
            s_i += f'+{abs(factor):f}*(t/{self.rf_angle})^{i}' if factor>0 else f'-{abs(factor):f}*(t/{self.rf_angle})^{i}'
        print('s_i: ', s_i)

    def graph_torque(self):
        torque_axis = []
        angle_axis = []
        F_g = FOLLOWER_MASS*9.81
        for angle in range(0, 180):
            s_i = self.calculate_displacement(angle)
            s_i_plus_r = s_i + self.radious     #mm

            r_t = self.calculate_velocity(angle)    # mm/deg

            F_s = (ANGULAR_VELOCITY**2)*self.calculate_acceleration(angle)/1000*FOLLOWER_MASS
            F_p = (INITIAL_FORCE + (MINIMUM_DISPLACEMENT + s_i)*SPRING_CONSTANT)*NUMBER_OF_SPRINGS
            angle_axis.append(angle)
            torque_axis.append((F_g + F_p + F_s)*(r_t + FRICTION_COEFFICIENT*s_i_plus_r))   # mNm
            print('F_p: ', F_p)

        plt.plot(angle_axis, torque_axis)
        plt.ylabel('M [Nmm]')
        plt.xlabel('gamma [deg]')
        plt.title('M(gamma)')
        plt.show()
