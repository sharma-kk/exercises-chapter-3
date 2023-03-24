class Circle:

    def __init__(self, c, r):
        self.centre = c
        self.radius = r

    def __contains__(self, item):
        x = item[0]
        y = item[1]
        c = self.centre
        r = self.radius
        if (x-c[0])**2 + (y - c[1])**2 < r**2:
            return True
        else:
            return False