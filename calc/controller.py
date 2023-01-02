import view
import logger
import model

# реализовать калькулятор с системой логирования:
# решение вводных примеров (2+3=5)
# решение уравнений (х+3=0) х=3
# упрощение многочленов (x*2+3x*2+4) 4*x*2 + 4

# Записать в файл задачу от пользователя и ответ

def run_calc():
    while True:
        mode = view.choose()
        if mode == "1":
            expr = view.get_expr()
            result = model.execute_expr(expr)
            view.show_res(result)
            logger.log_exec(ewpr, result)
        elif mode == "2":
             expr = view.get.expr()
             result = model.solve_eq(expr)
             view.show_res(result)
             logger.log_exec(expr, result)
        elif mode == "3":
            expr = view.get.expr()
            result = model.simplify_pol(expr)
            view.show_res(result)
            logger.log_exec(expr, result)
        elif mode == "4":
            history = logger.get_history()
            view.show_history(history)
        else:
            view.error_mode()