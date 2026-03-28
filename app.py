import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


class CsvReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_csv(self, chunksize):
        return pd.read_csv(self.file_path, chunksize=chunksize)


class CsvProcessor:
    def __init__(self, file_path, chunksize):
        self.reader = CsvReader(file_path)
        self.chunks = self.reader.read_csv(chunksize)
        self.iterable_chunks = iter(self.chunks)

    def transform_chunk(self, chunk):
        transformed_chunk = chunk.iloc[:, 3:]
        return transformed_chunk

    def get_next_chunk(self):
        try:
            chunk = next(self.iterable_chunks)
            return self.transform_chunk(chunk)
        except StopIteration:
            return None

    def get_next_chunk_as_json(self):
        chunk = self.get_next_chunk()
        if chunk is None:
            return None
        return chunk.to_dict(orient="records")


csv_file_path = "data/telecom.csv"
processor = CsvProcessor(csv_file_path, 1000)


@app.route("/api/v1/telecom", methods=["GET"])
def get_json():
    try:
        json_chunk = processor.get_next_chunk_as_json()

        if json_chunk is None:
            return jsonify({"message": "No more data"}), 200

        return jsonify(json_chunk), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)