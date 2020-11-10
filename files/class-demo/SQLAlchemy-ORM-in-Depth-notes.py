# Query Methods:

# Select records
# all()
MyModel.query.all()
# Same as doing a SELECT *, fetching all records from the model's table. Returns a list of objects.

# first()
MyModel.query.first()
# Fetches just the first result. Returns either None or an object if found.

# Filtering
# filter_by()
MyModel.query.filter_by(my_table_attribute='some value')
# Similar to doing a SELECT * from ... WHERE SQL statement for filtering data by named attributes.

# Examples:
MyModel.query.filter(MyOtherModel.some_attr='some value')
OrderItem.query.filter(Product.id=3)
# Similar to filter_by, but instead, you specify attributes on a given Model. It is more flexible
# than using filter_by itself, and is especially useful when querying from a joined table where
# you want to filter by attributes that span across multiple models.
# You can filter on equality, inequality, like filtering ("fuzzy" string matching), IN, NOT IN, NULL, NOT NULL, etc.

# Ordering
# order_by()
MyModel.order_by(MyModel.created_at)
MyModel.order_by(db.desc(MyModel.created_at))
# To order the results by a given attribute. Use db.desc to order in descending order.

# limit()
Order.query.limit(100).all()
# limit(max_num_rows) limits the number of returned records from the query. ala LIMIT in SQL.

# Aggregates
# count()
# Example:
query = Task.query.filter(completed=True)
query.count()
# Returns an integer set to the number of records that would have been returned by running the query.

# get()
# Get object by ID
model_id = 3
MyModel.query.get(model_id)
# Returns the object as a result of querying the model by its primary key.

# Bulk Deletes
# Example:
query = Task.query.filter_by(category='Archived')
query.delete()
# delete() does a bulk delete operation that deletes every record matching the given query.

# Joined Queries
# Example:
Driver.query.join('vehicles')
# Query has a method join(<table_name>) for joining one model to another table.


# review

from flask_hello_app import db, Person
# To check out what we have in our Person table
person = Person(name='Brian')
# To get back specific results as an object
Person.query.filter_by(name='Brian')
# To see whats in the object
Person.query.filter_by(name='Brian').all()
# Assign results to a variable
results = Person.query.filter_by(name='Brian').all()
# Query results like any other list
results[0]
results[0].name
results[0].id
# Add new objects to the database
# Instance object
person = Person(name='Bob 2')
db.session.add(person)
# Commit the add
db.session.commit()
# View the change
Person.query.all()
# Add multiple objects at once
person1 = Person(name='Sam')
person2 = Person(name='Cookie')
db.session.add_all([person1, person2])
db.session.commit()
Person.query.all()
# View the first object in the database
Person.query.first()


# Model.query

# Similar to doing a select statment with a where clause
Person.query.filter_by(name='Brian')
# Similar to doing a select * statment
Person.query.all()
# Similar to doing a group by count statment
Person.query.count()
# A flexable way of filtering results
Person.query.filter(Person.name == 'Brian')
# filter by multiple models across multiple tables
Person.query.filter(Person.name == 'Brian', Team.name == 'Udacity')
# Gets by primary key
Person.query.get(1)
# Bulk operations
# Query, filter, and then delete results
Product.query.filter_by(category='Misc').delete()







