import pymongo
import sha256 as sha256
# Replace with your MongoDB connection string
mongo_uri = 'mongodb+srv://sonadas8april:riyadasdas@cluster0.x0jnn5h.mongodb.net/'

# Create a MongoClient
client = pymongo.MongoClient(mongo_uri)

# Replace with your database name
db = client['HelpDroid']

# Replace with your collection name
collection = db['User']

# Insert a document into the collection

def insert_data(email,password,mobile,name):
    # data = {'email': email, 'password': password,'mobile':mobile, 'name': name}
    # collection.insert_one(data)
    try:
        
        hash = sha256.sha256(password+""+email)
        
        data = {'email': email, 'password': hash,'mobile':mobile, 'name': name}
        collection.insert_one(data)
        print("Inserted")
    except Exception as e:
        print(f"Error:  (An error occurred)")

    # query = {'email': "Jlhn@john"}
def update(email_input,new_pass):
    filter_criteria = {"email": email_input}

    # Define the update operation (e.g., set a new value for a field)
    update_operation = {"$set": {"password": new_pass}}

    # Update the document in the collection
    collection.update_one(filter_criteria, update_operation)

    
def find(query):
   matching_documents = collection.find(query)
   return matching_documents
   
       
def loginotpcheck(email_input):
    query = {'email': email_input}
    matching_documents = collection.find(query)
    for document in matching_documents:
        print(document)
        print("Login Successful")
        return True
    return False

