import pandas
import numpy
from PyQt6.QtCharts import QBarSeries, QChart, QBarCategoryAxis, QValueAxis, QChartView, QBarSet, QLineSeries
from PyQt6.QtCore import Qt, QSizeF


class SumByMonth(QChart):
    def __init__(self, data):
        super().__init__()

        self.setTitle('Month End Balance By Month')
        self.legend().setVisible(False)
        self.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        # Prepare the data
        df = pandas.DataFrame.from_records(data, columns=['Month', 'Amount'])
        pivot = df.pivot_table(values=['Amount'], columns=['Month'], aggfunc=numpy.sum)
        data_dict = pivot.to_dict()
        months = []
        values = []
        for month in data_dict:
            months.append(month)
            values.append(data_dict[month]['Amount'])

        bar_set = QBarSet("Default")
        bar_set.append(values)
        bar_series = QBarSeries()
        bar_series.append(bar_set)
        self.addSeries(bar_series)

        axis_x = QBarCategoryAxis()
        axis_x.append(months)
        self.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        bar_series.attachAxis(axis_x)

        axis_y = QValueAxis()
        max_y = (max(values) // 500) * 500 + 500
        min_y = (min(values) // 500) * 500 - 500
        axis_y.setRange(min_y, max_y)
        axis_y.setTickCount(int((abs(min_y) + abs(max_y)) // 500 + 1))
        axis_y.setMinorTickCount(1)
        self.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        bar_series.attachAxis(axis_y)

        self.setMinimumSize(QSizeF(1800, 1000))


class HistoryByMonth(QChart):
    def __init__(self, data, start_balance, width, height):
        super().__init__()

        self.setTitle('Balance History By Month')
        self.legend().setVisible(False)
        self.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        self.createDefaultAxes()

        # Prepare the data
        df = pandas.DataFrame.from_records(data, columns=['Month', 'Amount'])
        pivot = df.pivot_table(values=['Amount'], columns=['Month'], aggfunc=numpy.sum)
        data_dict = pivot.to_dict()
        months = []
        values = []
        previous_value = start_balance
        for month in data_dict:
            months.append(month)
            accumulated_value = data_dict[month]['Amount'] + previous_value
            values.append(round(accumulated_value, 2))
            previous_value = accumulated_value

        series = QLineSeries()
        for idx, value in enumerate(values):
            series.append(idx, value)

        self.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(months)
        self.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        max_y = max(values)
        min_y = min(values)
        axis_y.setRange(min_y, max_y)
        axis_y.setTickCount(7)
        self.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_y)

        self.setMinimumSize(QSizeF(width - 70, height - 150))
        print(width, height)
