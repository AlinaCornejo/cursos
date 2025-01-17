from adapters import CsvToJsonAdapter
from data_handlers import JsonDataHandler, CsvDataHandler

def load_and_display_data(data_handler, file_path):
    data = data_handler.load_data(file_path)
    print(data)

if __name__ == "__main__":
    json_handler = JsonDataHandler()
    json_file_path = 'data/sample_data.json'
    load_and_display_data(json_handler, json_file_path)

    csv_handler = CsvDataHandler()
    csv_file_path = 'data/sample_data.csv'
    csv_adapter = CsvToJsonAdapter(csv_handler)
    load_and_display_data(csv_adapter, csv_file_path)