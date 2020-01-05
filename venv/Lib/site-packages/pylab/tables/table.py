import warnings
from column import Column

class Table():

    def __init__(self):
        self.columns = []
        self.measured = False

    def table_add(self, name, unit, callback):
        if self.measured:
            warnings.warn("Already measured, cannot add another column.")
        else:
            self.columns.append(Column(name, unit, callback))
            self._table_add()

    def tablesave(self):
        self.measured = True
        for device in self.columns:
            device.measure()
        self._tablesave()

    def _table_add(self):
        pass

    def _table_add(self):
        pass
