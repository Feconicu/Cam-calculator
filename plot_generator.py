

class Cam:
    def __init__(self, factors, height, rf_angle):
        self.factors = factors
        self.height = height
        self.rf_angle = rf_angle

    def __dir__(self):
        return self.factors, self.height, self.rf_angle

    def calculate_displacement(self, angle):
        angle %= 360
        if angle >= self.rf_angle:
            return 0
        s = 0
        for pow, C in enumerate(self.factors):
            s += C*((angle/self.rf_angle))**pow
        return s

class CamGrapher(Cam):
    def __init__(self, ang_speed, cam_or_factors, *args):
        self.ang_speed = ang_speed
        if isinstance(cam_or_factors, Cam):
            super().__init__(*cam_or_factors.__dir__())
        else:
            super().__init__(cam_or_factors ,*args)

    def graph_displacement(self):
        pass




    