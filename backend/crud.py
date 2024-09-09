from sqlalchemy.orm import Session
from database.schemas import ProductCreate, ProductUpdate
from database.models import ProductModel

# select * from products
def get_products(db: Session):
    return db.query(ProductModel).all()


# select * from products where id = product_id
def get_product(db: Session, product_id: int):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

# insert into products
def create_product(db: Session, product: ProductCreate):
    # transformar view para ORM
    db_product = ProductModel(**product.model_dump())
    
    # adicionar na tabela
    db.add(db_product)
    
    # commit
    db.commit()
    
    # refresh do db
    db.refresh(db_product)
    
    return db_product


# delete from products where id = product_id
def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


# update set 
def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    
    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name
        
    if product.description is not None:
        db_product.description = product.description
        
    if product.price is not None:
        db_product.price = product.price
        
    if product.category is not None:
        db_product.category = product.category
        
    if product.supplier_email is not None:
        db_product.supplier_email = product.supplier_email
        
    db.commit()
    db.refresh()
    
    return db_product