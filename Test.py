from pymongo import MongoClient

# Replace with your MongoDB connection string
mongo_uri = "mongodb+srv://Chathura:FKciTuoXPqaXcQ4L@cluster0.k9osu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to MongoDB
client = MongoClient(mongo_uri)

# Select the database
db = client["EtaBetaPiAPIDB"]  # Replace with your database name

# Select the collection (table)
collection = db["EtaBetaPiAPICL"]  # Replace with your collection name
data = collection.find()

# Print retrieved documents
for record in data:
    print(record)