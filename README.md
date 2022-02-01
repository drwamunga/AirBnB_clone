## AirBnB Clone - The Console
The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

Functionalities of this command interpreter:
Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc...
Do operations on objects (count, compute stats, etc...)
Update attributes of an object
Destroy an object

Usage
The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

Command	Example
Run the console	./console.py
Quit the console	(hbnb) quit
Display the help for a command	(hbnb) help <command>
Create an object (prints its id)	(hbnb) create <class>
Show an object	(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
Destroy an object	(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
Show all objects, or all instances of a class	(hbnb) all or (hbnb) all <class>
Update an attribute of an object	(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>")
Non-interactive mode example

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
Models
The folder models contains all the classes used in this project.

File	Description	Attributes
base_model.py	BaseModel class for all the other classes	id, created_at, updated_at
user.py	User class for future user information	email, password, first_name, last_name
amenity.py	Amenity class for future amenity information	name
city.py	City class for future location information	state_id, name
state.py	State class for future location information	name
place.py	Place class for future accomodation information	city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids
review.py	Review class for future user/host review information	place_id, user_id, text
File storage
The folder engine manages the serialization and deserialization of all the data, following a JSON format.

A FileStorage class is defined in file_storage.py with methods to follow this flow: <object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>

The init.py file contains the instantiation of the FileStorage class called storage, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.
