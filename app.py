from flask import Flask, Response, jsonify
from pymongo import MongoClient
import pandas as pd
import io
import os

app = Flask(__name__)

# MongoDB Connection String (Replace with your credentials)
mongo_uri = os.getenv("MONGO_URI", "mongodb+srv://Chathura:FKciTuoXPqaXcQ4L@cluster0.k9osu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = MongoClient(mongo_uri)

# Select database and collection
db = client["EtaBetaPiAPIDB"]  # Replace with your database name
collection = db["EtaBetaPiAPICL"]  # Replace with your collection name

@app.route('/export_csv', methods=['GET'])
def export_csv():
    try:
        # Fetch all documents from MongoDB (Exclude "_id" for clean CSV format)
        data = list(collection.find({}, {"_id": 0}))

        # Convert to Pandas DataFrame
        df = pd.DataFrame(data)

        # Convert DataFrame to CSV in memory
        csv_output = io.StringIO()
        df.to_csv(csv_output, index=False)

        # Prepare response
        response = Response(csv_output.getvalue(), content_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=data_export.csv"
        return response

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)