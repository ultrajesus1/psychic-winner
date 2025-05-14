import matplotlib.pyplot as plt

class EquationUI:
    @staticmethod
    def input_coefficients():
        print("Введите коэффициенты a, b, c:")
        try:
            a = float(input('a= '))
            b = float(input('b= '))
            c = float(input('c= '))
            return a, b, c
        except ValueError:
            raise Exception("Ошибка ввода! Коэффициенты должны быть числами.")

    @staticmethod
    def plot_solution(a, b, c, roots, type_):
        x_values = []
        y_values = []
        for i in range(-10, 11):
            x = i
            y = a*x**2 + b*x + c
            x_values.append(x)
            y_values.append(y)

        plt.plot(x_values, y_values, label=f'{a}x^2+{b}x+{c}')

        if type_ == 'two_real':
            plt.scatter(roots, [0]*len(roots), color='red', s=100, zorder=5)
        elif type_ == 'one_real':
            plt.scatter([roots[0]], [0], color='green', s=100, zorder=5)
        elif type_ == 'complex':
            pass  # Не рисуем точки для комплексных корней

        plt.title(f'График функции {a}x^2+{b}x+{c}=0')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.show()

    @staticmethod
    def display_result(result):
        print(result['message'])