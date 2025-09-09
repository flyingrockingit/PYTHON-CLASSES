class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)   
            return result
        except Exception as e:
            return f"Error: {e}"

    def display(self):
        print(f"Expression: {self.expression}")
        print(f"Result: {self.solve()}")


if __name__ == "__main__":
    expr = input("Enter an expression (e.g., 3+5*2): ")
    solver = ExpressionSolver(expr)   
    solver.display()

