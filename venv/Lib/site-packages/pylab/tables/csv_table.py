from table import Table

class CSVTable(Table):

    def __init__(self, savepath):
        self.savepath = savepath
        self.file_created = False
        super().__init__()

    def _table_add(self):
        fieldnames = [column.generate_header()  for column in self.columns]
        with open(self.savepath, mode="w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

    def _tablesave(self):
        fieldnames = [column.generate_header()  for column in self.columns]
        values = {column.generate_header(): column.get_last_value() for column in self.columns}
        with open(self.savepath, mode="a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(values)
