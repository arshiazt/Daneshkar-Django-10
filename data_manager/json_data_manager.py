import json
import os

class DataManager:

    def make_dir(self, path):
        os.makedirs(path, exist_ok=True)

    def make_json_file(self, path):
        directory = os.path.dirname(path)

        if directory:
            self.make_dir(directory)

        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as file:
                json.dump([], file, ensure_ascii=False, indent=4)

    def load_data(self, path):
        self.make_json_file(path)

        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_data(self, path, data):
        self.make_json_file(path)

        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)