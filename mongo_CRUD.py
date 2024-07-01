from pymongo import MongoClient, errors
from pymongo.server_api import ServerApi

# Database
client = MongoClient(
    "mongodb+srv://goit_alex:Nt2B9uK6Ir6MOhOW@mongocluster.1rpmrqh.mongodb.net/?retryWrites=true&w=majority&appName=MongoCluster",
    server_api=ServerApi('1')
)
db = client.book

# Створення унікального індексу для поля 'name' у колекції 'cats' (якщо треба унікальні імена)
# db.cats.create_index([("name", 1)], unique=True)


# Create  ------

# Функція створення барсика
def add_barsik():
    try:
        result = db.cats.insert_one(
            {
                "name": "barsik",
                "age": 3,
                "features": ["ходить в капці", "дає себе гладити", "рудий"],
            }
        )
        print("Created one:", result.inserted_id)
    
    except errors.ConnectionFailure:
        print("Failed to connect to the database. Please check your connection settings.")
    
    except errors.OperationFailure as e:
        print(f"An error occurred during the insert operation: {e}")

    except errors.DuplicateKeyError:
        print("A cat with the same key already exists.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# виклик функції
add_barsik()

# Функція створення одного
def add_one(name, age, features):
    try:
        result = db.cats.insert_one(
            {
                "name": name,
                "age": age,
                "features": features,
            }
        )
        print("Created one:", result.inserted_id)
    
    except errors.ConnectionFailure:
        print("Failed to connect to the database. Please check your connection settings.")
    
    except errors.OperationFailure as e:
        print(f"An error occurred during the insert operation: {e}")

    except errors.DuplicateKeyError:
        print("A document with the same key already exists.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# виклик функції
add_one("Boris", 12, ["ходить в капці", "не дає себе гладити", "сірий"])



# Функція створення багато
def add_many():
    try:
        result = db.cats.insert_many(
            [
                {
                    "name": "Lama",
                    "age": 2,
                    "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
                },
                {
                    "name": "Liza",
                    "age": 4,
                    "features": ["ходить в лоток", "дає себе гладити", "білий"],
                },
            ]
        )
        print("Created: ", result.inserted_ids)
    
    except errors.ConnectionFailure:
        print("Failed to connect to the database. Please check your connection settings.")
   
    except errors.BulkWriteError as bwe:
        for error in bwe.details['writeErrors']:
            print(f"Error inserting document: {error['errmsg']}")
    
    except errors.OperationFailure as e:
        print(f"An error occurred during the insert operation: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# виклик функції
add_many()


# Read -----------

# Функція виведення всіх записів із колекції.
def get_all():
    try:
        result = db.cats.find({}, {"_id": 0})
        
        # Виведення всіх котів та їх характеристик
        for el in result:
            print(el["name"], "-", el["age"], "years")
            for feature in el["features"]:
                print("    ", feature)
    
    except errors.ConnectionFailure:
        print("Failed to connect to the database. Please check your connection settings.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# виклик функції
get_all()

    # Функція, яка дозволяє користувачеві ввести ім'я кота та виводить інформацію про цього кота.
def get_by_name(name):
    try:
        cat = db.cats.find_one({"name": name}, {"_id": 0})
        
        # Перевірка, чи був знайдений кіт з таким іменем
        if cat:
            print(cat["name"], "-", cat["age"], "years")
            for feature in cat["features"]:
                print("    ", feature)
        else:
            print(f"No cat found with the name '{name}'.")

    except errors.ConnectionFailure:
        print("Failed to connect to the database. Please check your connection settings.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# виклик функції
get_by_name("Lama")


# Update --------
    # Функція, яка дозволяє користувачеві оновити вік кота за ім'ям.
def update_age(name, new_age):
    try:
        # Виконання оновлення
        result = db.cats.update_one({"name": name}, {"$set": {"age": new_age}})
        # Перевірка, чи був оновлений документ
        if result.modified_count == 0:
            if result.matched_count == 0:
                print(f"No documents were updated. It's possible that no document with the name {name} exists.")
            else:
                print(f"No documents were updated. It's possible the age was already set to {new_age}.")
        else:
            print(f"{name}'s age was updated to {new_age}.")
    
    except errors.ConnectionFailure:
        print("Failed to connect to the database. Please check your connection settings.")
    
    except errors.OperationFailure as e:
        print(f"An error occurred during the update operation: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

update_age("barsik", 1)

    # Функція, яка дозволяє додати нову характеристику до списку features кота за ім'ям.
def add_feature(name, new_feature):
    try:
        # Виконання оновлення
        result = db.cats.update_one(
            {"name": name},
            {"$push": {"features": new_feature}}
        )
        
        # Перевірка, чи був оновлений документ
        if result.matched_count == 0:
            print(f"No documents found with the name {name}.")
        elif result.modified_count == 0:
            print(f"No changes were made. It's possible that the feature {new_feature} already exists.")
        else:
            print(f"The feature '{new_feature}' was added to {name}'s features.")
    
    except errors.ConnectionFailure:
        print("Failed to connect to the database. Please check your connection settings.")
    
    except errors.OperationFailure as e:
        print(f"An error occurred during the update operation: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# виклик функції
add_feature("barsik", "боїться мишей")
# get_by_name("barsik")  # перевірка




# Delete -------

# Функція для видалення запису з колекції за ім'ям тварини.
def delete_cat_by_name(name):
    try:
        # Виконання видалення
        result = db.cats.delete_one({"name": name})
        
        # Перевірка, чи був видалений документ
        if result.deleted_count == 0:
            print(f"No documents found with the name {name}.")
        else:
            print(f"Document with the name {name} was successfully deleted.")
    
    except errors.ConnectionFailure:
        print("Failed to connect to the database. Please check your connection settings.")
    
    except errors.OperationFailure as e:
        print(f"An error occurred during the delete operation: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# виклик функції
delete_cat_by_name("Liza")

    # Функція для видалення всіх записів із колекції.
def delete_all_cats():
    try:
        # Виконання видалення всіх документів
        result = db.cats.delete_many({})
        
        # Виведення кількості видалених документів
        print(f"Deleted {result.deleted_count} documents from the collection.")
    
    except errors.ConnectionFailure:
        print("Failed to connect to the database. Please check your connection settings.")
    
    except errors.OperationFailure as e:
        print(f"An error occurred during the delete operation: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# виклик функції
# delete_all_cats()
# get_all()






