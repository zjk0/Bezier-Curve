# pragma once

/**
 * ---------------------------------- Include ----------------------------------
 */
#include <vector>

/**
 * ---------------------------------- Marcos ----------------------------------
 */
#define ERROR 0.0f

/**
 * ---------------------------------- Namespace ----------------------------------
 */
using namespace std;

/**
 * ---------------------------------- Class ----------------------------------
 */
class BezierCurve {
    private:
    int CurveOrder;
    vector<float> ControlPoints;
    vector<float> Curve;

    public:
    BezierCurve(int CurveOrder, vector<float> ControlPoints);
    ~BezierCurve();
    float DeCasteljau(float t, int CurveOrder, vector<float> ControlPoints);
    float GenerateCurve(void);
};

BezierCurve::BezierCurve (int CurveOrder, vector<float> ControlPoints) {
    this->CurveOrder = CurveOrder;
    this->ControlPoints = ControlPoints;
}

float BezierCurve::DeCasteljau (float t, int CurveOrder, vector<float> CalculatePoints) {
    if (t < 0 || t > 1) {
        return ERROR;
    }
    if (CurveOrder + 1 != ControlPoints.size()) {
        return ERROR;
    }
    if (CurveOrder < 1) {
        return ERROR;
    }

    if (CurveOrder == 1) {
        return ((1 - t) * CalculatePoints[0] + t * CalculatePoints[1]);
    }
    else {
        return (1 - t) * DeCasteljau(t, CurveOrder - 1, CalculatePoints[0:CurveOrder]) + t * DeCasteljau(t, CurveOrder - 1, CalculatePoints[1:(CurveOrder + 1)])
    }
}

float BezierCurve::GenerateCurve (void) {

}