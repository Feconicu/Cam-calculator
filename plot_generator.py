
import matplotlib.pyplot as plt
from math import sin, cos, radians, atan, pi

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


class CamGrapher(Cam):
    def __init__(self, ang_speed, cam_or_factors, *args):
        self.ang_speed = ang_speed
        if isinstance(cam_or_factors, Cam):
            super().__init__(*cam_or_factors.__dir__())
        else:
            super().__init__(cam_or_factors ,*args)

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
        print(len(velocity_axis))
        plt.plot(time_axis, velocity_axis)
        plt.xlabel('t [s]')
        plt.ylabel('v [mm/s]')
        plt.title('v(t)')
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