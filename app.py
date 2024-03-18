import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from design import Ui_main_w


class MainWindow(QMainWindow, Ui_main_w):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_summer.setText('Рассчитать')
        self.out_summer.show()
        self.btn_summer.clicked.connect(self.func_summer)

        self.btn_winter.setText('Рассчитать')
        self.out_winter.show()
        self.btn_winter.clicked.connect(self.func_winter)

    def func_summer(self):
        try:
            a_summer_1 = float(self.le_summer.text())
            result = round(0.3 * float(a_summer_1) / 100 * 11.5, 2)
            result_2 = round(0.7 * float(a_summer_1) / 100 * 8.5, 2)
            total = round((0.3 * a_summer_1 / 100 * 11.5) + (0.7 * a_summer_1 / 100 * 8.5), 2)

            self.out_summer.setText(f'Вы потратили по городу {result} литров \n'
                                    f'Вы потратиил по трассе {result_2} литров \n'
                                    f'Общий расход бензина {total} литров\n \n'
                                    f'Расход 11.5 / 8.5 л. на 100 км.')

        except Exception as e:
            msg = QMessageBox.information(
                self, 'Внимание', f"Что-то пошло не так. \n"
                                  f"Проверьте исходные данные.")

    def func_winter(self):
        try:
            a_winter_1 = float(self.le_winter.text())
            result = round(0.3 * float(a_winter_1) / 100 * 13.8, 2)
            result_2 = round(0.7 * float(a_winter_1) / 100 * 10.2, 2)
            total = round((0.3 * a_winter_1 / 100 * 13.8) + (0.7 * a_winter_1 / 100 * 10.2), 2)

            self.out_winter.setText(f'Вы потратили по городу {result} литров \n'
                                    f'Вы потратиил по трассе {result_2} литров \n'
                                    f'Общий расход бензина {total} литров\n \n'
                                    f'Расход 13.8 / 10.2 л. на 100 км.')

        except Exception as e:
            msg = QMessageBox.information(
                self, 'Внимание', f"Что-то пошло не так. \n"
                                  f"Проверьте исходные данные.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
