# 随机产生半径r，再随机产生角度theta，注意半径的随机不能从0到r，要从0到r^2随机后开方，因为是面积微分的随机，不是半径微分的随机。

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        r = random.uniform(0, self.radius * self.radius)
        theta = random.uniform(0, 2*math.pi)
        return [self.x_center + math.sqrt(r)*math.cos(theta), self.y_center + math.sqrt(r)*math.sin(theta)]