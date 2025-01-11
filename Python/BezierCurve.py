# ---------------------------------- Import ----------------------------------
from matplotlib import pyplot as plt
import numpy as np

# ---------------------------------- Class ----------------------------------
class BezierCurve:
    """
    @brief Initialize the instance of BezierCurve class
    
    @param self: The instance itself (No need to input while using)
    @param CurveOrdef: The ordef of bezier curve
    @param ControlPoints: All control points of bezier curve
    @param CurveAccuracy: The amount of points on curve

    @return none
    """
    def __init__ (self, CurveOrder, ControlPoints, CurveAccuracy):
        if CurveOrder + 1 != ControlPoints.shape[0]:
            print("Error! Curve order add 1 must be equal to the number of control points!")
            return
        if CurveOrder < 1:
            print("Error! Curve order must be over 1!")
            return
        
        self.CurveOrder = CurveOrder
        self.ControlPoints = ControlPoints
        self.CurveAccuracy = CurveAccuracy
        self.Curve = np.zeros((CurveAccuracy, 2))

    """
    @brief Use DeCasteljau algorithm to calculate bezier curve

    @param self: The instance itself (No need to input while using)
    @param t: A parameter in the expression of bezier curve
    @param CurveOrder: The order of curve
    @param CalculatePoints: The value used to calculate, usually the x-position or y-position of control points

    @return The final value, usually the x-position or y-position of a point on bezier curve
    """
    def DeCasteljau (self, t, CurveOrder, CalculatePoints):
        if t < 0 or t > 1:
            print("Error! Parameter \'t\' must in [0, 1]!")
            return
        if CurveOrder + 1 != CalculatePoints.shape[0]:
            print("Error! Curve order add 1 must be equal to the number of control points!")
            return
        if CurveOrder < 1:
            print("Error! Curve order must be over 1!")
            return
        
        if CurveOrder == 1:
            return ((1 - t) * CalculatePoints[0] + t * CalculatePoints[1])
        else:
            return (1 - t) * self.DeCasteljau(t, CurveOrder - 1, CalculatePoints[0:CurveOrder]) + t * self.DeCasteljau(t, CurveOrder - 1, CalculatePoints[1:(CurveOrder + 1)])

    """
    @brief Generate the points on bezier curve

    @param self: The instance itself (No need to input while using)

    @return The array of all points of bezier curve
    """
    def GenerateCurve (self):
        if self.CurveOrder < 1:
            print("Error! Curve order must be over 1!")
            return
        if self.CurveOrder + 1 != self.ControlPoints.shape[0]:
            print("Error! Curve order add 1 must be equal to the number of control points!")
            return
        
        bezier_curve = np.zeros((self.CurveAccuracy, 2))
        i = 0
        ControlPoints_x = self.ControlPoints[:, 0]
        ControlPoints_y = self.ControlPoints[:, 1]

        for t in np.linspace(0, 1, self.CurveAccuracy):
            bezier_curve[i, 0] = self.DeCasteljau(t, self.CurveOrder, ControlPoints_x)
            bezier_curve[i, 1] = self.DeCasteljau(t, self.CurveOrder, ControlPoints_y)
            i += 1

        return bezier_curve
    
    """
    @brief Draw bezier curve

    @param self: The instance itself (No need to input while using)

    @return none
    """
    def DrawCruve (self):
        self.Curve = self.GenerateCurve()
        plt.plot(self.Curve[:, 0], self.Curve[:, 1])
        plt.show()


# Test
CurveOrder = 5
ControlPoints = np.zeros((CurveOrder + 1, 2))
CurveAccuracy = 100
ControlPoints[0, 0] = 0
ControlPoints[0, 1] = 0
ControlPoints[1, 0] = 1
ControlPoints[1, 1] = 0
ControlPoints[2, 0] = 2
ControlPoints[2, 1] = 0
ControlPoints[3, 0] = 3
ControlPoints[3, 1] = 0
ControlPoints[4, 0] = 4
ControlPoints[4, 1] = 0
ControlPoints[5, 0] = 5
ControlPoints[5, 1] = 0
bezier_curve = BezierCurve(CurveOrder, ControlPoints, CurveAccuracy)
bezier_curve.DrawCruve()
