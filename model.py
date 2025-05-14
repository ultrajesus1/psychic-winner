import math

class QuadraticEquationSolver:
    def solve(self, a, b, c):
        D = b**2 - 4*a*c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            return {'roots': [x1, x2], 'type': 'two_real'}
        elif D == 0:
            x = -b / (2 * a)
            return {'roots': [x], 'type': 'one_real'}
        else:
            real_part = -b / (2 * a)
            imag_part = math.sqrt(-D) / (2 * a)
            return {
                'roots': [(real_part, imag_part), (real_part, -imag_part)],
                'type': 'complex'
            }  