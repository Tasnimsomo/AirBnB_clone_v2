import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Determine the storage type based on the environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

# Create an instance of the appropriate storage class
if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

# Execute the reload method on the storage instance
storage.reload()
