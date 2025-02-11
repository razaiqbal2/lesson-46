class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression  

    def evaluate(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"

    def display_result(self):
        result = self.evaluate()
        print(f"The result of the expression '{self.expression}' is: {result}")



if __name__ == "__main__":

    expression = input("Enter a mathematical expression: ")

    solver = ExpressionSolver(expression)

    solver.display_result()
