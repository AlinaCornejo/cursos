from data_handlers import JsonDataHandler, CsvDataHandler

class CsvToJsonAdapter:
    def __init__(self, csv_handler: CsvDataHandler):
        self.csv_handler = csv_handler

    def load_data(self, file_path):
        csv_data = self.csv_handler.load_data(file_path)
        return [dict(row) for row in csv_data]