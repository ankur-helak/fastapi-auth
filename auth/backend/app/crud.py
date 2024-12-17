from sqlalchemy.orm import Session
from . import models, schemas

# CRUD operations for Product

def create_product(db: Session, product: schemas.ProductSchema):
    """Create a new product in the database."""
    db_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_product(db: Session, product_id: int):
    """Retrieve a product by its ID."""
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def update_product(db: Session, product_id: int, product: schemas.ProductSchema):
    """Update an existing product."""
    db_product = get_product(db, product_id)
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.stock = product.stock
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    """Delete a product by its ID."""
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# CRUD operations for User

def create_user(db: Session, user: schemas.UserSchema):
    """Create a new user in the database."""
    db_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=user.password  # Assume password is already hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    """Retrieve a user by their ID."""
    return db.query(models.User).filter(models.User.id == user_id).first()

def update_user(db: Session, user_id: int, user: schemas.UserSchema):
    """Update an existing user."""
    db_user = get_user(db, user_id)
    if db_user:
        db_user.username = user.username
        db_user.email = user.email
        db_user.password_hash = user.password  # Assume password is already hashed
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """Delete a user by their ID."""
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

# CRUD operations for Order

def create_order(db: Session, order: schemas.OrderSchema):
    """Create a new order in the database."""
    db_order = models.Order(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        status='Pending'  # Default status
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):
    """Retrieve an order by its ID."""
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def update_order(db: Session, order_id: int, order: schemas.OrderSchema):
    """Update an existing order."""
    db_order = get_order(db, order_id)
    if db_order:
        db_order.quantity = order.quantity
        db_order.status = order.status
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    """Delete an order by its ID."""
    db_order = get_order(db, order_id)
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order

condition = True

while True:
    # Your code here
    print("This will run at least once.")
    
    # Update the condition
    condition = False  # or some other logic to break the loop
    
    if not condition:
        break



