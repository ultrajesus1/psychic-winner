from model import QuadraticEquationSolver
from view import EquationUI


class EquationController:
    def init(self):
        self.solver = QuadraticEquationSolver()
        self.ui = EquationUI()

    def run(self):
        while True:
            try:
                a, b, c = self.ui.input_coefficients()
                result = self.solver.solve(a, b, c)

                message = ''
                if result['type'] == 'two_real':
                    message = f"Уравнение имеет два действительных корня: {result['roots'][0]:.2f}, {result['roots'][1]:.2f}"
                elif result['type'] == 'one_real':
                    message = f"Уравнение имеет один действительный корень: {result['roots'][0]:.2f}"
                elif result['type'] == 'complex':
                    r1, im1 = result['roots'][0]
                    r2, im2 = result['roots'][1]
                    message = f"Уравнение имеет комплексные корни: ({r1:.2f}+{im1:.2f}i), ({r2:.2f}-{im2:.2f}i)"

                result['message'] = message
                self.ui.plot_solution(a, b, c, result['roots'], result['type'])
                self.ui.display_result(result)
                break
            except Exception as e:
                print(e)  