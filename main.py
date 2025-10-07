
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session,engine

from sqlalchemy.orm import Session

import database_models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://lolcalhost:3000'],
    allow_methods =['*']
)

database_models.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome MB !"
    

products = [
    Product(id=1,name="Phone",description="iPhone 17 new launch",price=199.9,quantity=12),
    Product(id=2,name="Desktop",description="iPhone 17 new launch",price=199.9,quantity=12),
]


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    
    count = db.query(database_models.Product).count
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        
    db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    
    db_products = db.query(database_models.Product).all()
    return db_products
    return {
                "data": [
                    {
                    "type": "site",
                    "id": "acnlment",
                    "attributes": {
                        "site_created": "2013-08-09",
                        "site_domain": "acnlmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/ACNL.jpg",
                        "site_name": "ACNL"
                    }
                    },
                    {
                    "type": "site",
                    "id": "ahmentor",
                    "attributes": {
                        "site_created": "2023-12-10",
                        "site_domain": "ahmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Adventist_Health.jpg",
                        "site_name": "Adventist Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "mybjcment",
                    "attributes": {
                        "site_created": "2021-07-06",
                        "site_domain": "mybjcmentor.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/BJC_HealthCare.jpg",
                        "site_name": "BJC Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "cshsconn",
                    "attributes": {
                        "site_created": "2020-10-06",
                        "site_domain": "cshsconnects.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Cedars.jpg",
                        "site_name": "Cedars-Sinai"
                    }
                    },
                    {
                    "type": "site",
                    "id": "centracon",
                    "attributes": {
                        "site_created": "2022-01-11",
                        "site_domain": "centraconnects.com",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Centra.jpg",
                        "site_name": "Centra Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "chlaconn",
                    "attributes": {
                        "site_created": "2023-03-16",
                        "site_domain": "chlaconnects.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Childrens_Hospital_LA.jpg",
                        "site_name": "CHLA"
                    }
                    },
                    {
                    "type": "site",
                    "id": "christiana",
                    "attributes": {
                        "site_created": "2022-09-11",
                        "site_domain": "christianacarementoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/ChristinaCare.jpg",
                        "site_name": "ChristianaCare Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "cohmentor",
                    "attributes": {
                        "site_created": "2020-10-07",
                        "site_domain": "cohmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/City_of_Hope.jpg",
                        "site_name": "City of Hope"
                    }
                    },
                    {
                    "type": "site",
                    "id": "cohmentall",
                    "attributes": {
                        "site_created": "2024-11-13",
                        "site_domain": "cohmentoringforall.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/City_of_Hope.jpg",
                        "site_name": "City of Hope/CTCA"
                    }
                    },
                    {
                    "type": "site",
                    "id": "ehleads",
                    "attributes": {
                        "site_created": "2025-05-13",
                        "site_domain": "ehleads.com",
                        "site_logo": "https://lifemoxieempire.com/site-logos/EisenHower_Health.jpg",
                        "site_name": "Eisenhower Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "elcamino",
                    "attributes": {
                        "site_created": "2019-01-26",
                        "site_domain": "elcaminomentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/El_Camino_Health.jpg",
                        "site_name": "El Camino Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "fairfaxc",
                    "attributes": {
                        "site_created": "2015-11-23",
                        "site_domain": "fairfaxcountymentoring.com",
                        "site_logo": "https://lifemoxieempire.com/site-logos/FairFax_County.jpg",
                        "site_name": "Fairfax County"
                    }
                    },
                    {
                    "type": "site",
                    "id": "inspira",
                    "attributes": {
                        "site_created": "2024-11-20",
                        "site_domain": "inspiramentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Inspira_Health.jpg",
                        "site_name": "Inspira Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "johnshop",
                    "attributes": {
                        "site_created": "2023-08-17",
                        "site_domain": "johnshopkinsmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Johns_Hopkins.jpg",
                        "site_name": "Johns Hopkins Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "kpmentor",
                    "attributes": {
                        "site_created": "2013-08-09",
                        "site_domain": "kpmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Kaiser_Permanente.jpg",
                        "site_name": "Kaiser Permanente"
                    }
                    },
                    {
                    "type": "site",
                    "id": "brighammen",
                    "attributes": {
                        "site_created": "2021-01-31",
                        "site_domain": "brighammentors.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Brigham.jpg",
                        "site_name": "Mass General Brigham"
                    }
                    },
                    {
                    "type": "site",
                    "id": "mwdment",
                    "attributes": {
                        "site_created": "2019-07-26",
                        "site_domain": "mwdmentoring.com",
                        "site_logo": "https://lifemoxieempire.com/site-logos/MWD.jpg",
                        "site_name": "Metropolitan Water District - LA"
                    }
                    },
                    {
                    "type": "site",
                    "id": "multicare",
                    "attributes": {
                        "site_created": "2021-07-27",
                        "site_domain": "multicarementoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Multicare.jpg",
                        "site_name": "MultiCare Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "nchmentors",
                    "attributes": {
                        "site_created": "2024-05-31",
                        "site_domain": "nchmentors.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/NCH.jpg",
                        "site_name": "Naples Community Hospital"
                    }
                    },
                    {
                    "type": "site",
                    "id": "mentnem",
                    "attributes": {
                        "site_created": "2025-05-29",
                        "site_domain": "mentoringatnemours.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Nemours.jpg",
                        "site_name": "Nemours Children's Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "nihnurse",
                    "attributes": {
                        "site_created": "2025-01-15",
                        "site_domain": "nihnursementoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/NIH.jpg",
                        "site_name": "NIH"
                    }
                    },
                    {
                    "type": "site",
                    "id": "northside",
                    "attributes": {
                        "site_created": "2024-07-14",
                        "site_domain": "northsidementoring.com",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Northside_Hospital.jpg",
                        "site_name": "Northside Hospital"
                    }
                    },
                    {
                    "type": "site",
                    "id": "ochsnerm",
                    "attributes": {
                        "site_created": "2017-01-17",
                        "site_domain": "ochsnermentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Ochsner.jpg",
                        "site_name": "Ochsner Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "rnmentor",
                    "attributes": {
                        "site_created": "2022-09-29",
                        "site_domain": "rnmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Oregon_Health.jpg",
                        "site_name": "OHSU"
                    }
                    },
                    {
                    "type": "site",
                    "id": "saintlukes",
                    "attributes": {
                        "site_created": "2024-10-20",
                        "site_domain": "saintlukesmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/St_Lukes.jpg",
                        "site_name": "Saint Luke's Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "sharpconn",
                    "attributes": {
                        "site_created": "2020-02-04",
                        "site_domain": "sharpconnects.com",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Sharp.jpg",
                        "site_name": "Sharp HealthCare"
                    }
                    },
                    {
                    "type": "site",
                    "id": "stanford",
                    "attributes": {
                        "site_created": "2017-11-01",
                        "site_domain": "stanfordmentoring.com",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Stanford_Health Care.jpg",
                        "site_name": "Stanford Medicine"
                    }
                    },
                    {
                    "type": "site",
                    "id": "tuftsmedic",
                    "attributes": {
                        "site_created": "2024-05-01",
                        "site_domain": "tuftsmedicinementors.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Tufts.jpg",
                        "site_name": "Tufts Medicine"
                    }
                    },
                    {
                    "type": "site",
                    "id": "uabment",
                    "attributes": {
                        "site_created": "2021-11-21",
                        "site_domain": "uabnursementoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/UAB.jpg",
                        "site_name": "UAB Medicine"
                    }
                    },
                    {
                    "type": "site",
                    "id": "ucdmentor",
                    "attributes": {
                        "site_created": "2022-08-28",
                        "site_domain": "ucdmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/UCDavis.jpg",
                        "site_name": "UC Davis Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "ucsdment",
                    "attributes": {
                        "site_created": "2021-09-12",
                        "site_domain": "ucsdmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/UC_San_Diego.jpg",
                        "site_name": "UC San Diego Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "ucsfment",
                    "attributes": {
                        "site_created": "2021-10-10",
                        "site_domain": "ucsfmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/UCSF.jpg",
                        "site_name": "UC San Francisco Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "utswelev",
                    "attributes": {
                        "site_created": "2022-12-19",
                        "site_domain": "utswelevate.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/UT.jpg",
                        "site_name": "UT Southwestern Medical Center"
                    }
                    },
                    {
                    "type": "site",
                    "id": "wellstarme",
                    "attributes": {
                        "site_created": "2023-07-02",
                        "site_domain": "wellstarmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Wellstar.jpg",
                        "site_name": "Wellstar Health"
                    }
                    },
                    {
                    "type": "site",
                    "id": "westatment",
                    "attributes": {
                        "site_created": "2024-07-02",
                        "site_domain": "westatmentoring.com",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Westat.jpg",
                        "site_name": "Westat"
                    }
                    },
                    {
                    "type": "site",
                    "id": "williams",
                    "attributes": {
                        "site_created": "2017-11-13",
                        "site_domain": "landingcareerdevelopment.com",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Williamsburg Landing.jpg",
                        "site_name": "Williamsburg Landing"
                    }
                    },
                    {
                    "type": "site",
                    "id": "yalenh",
                    "attributes": {
                        "site_created": "2020-02-20",
                        "site_domain": "ynhhsmentoring.org",
                        "site_logo": "https://lifemoxieempire.com/site-logos/Yale_New_Haven.jpg",
                        "site_name": "Yale New Haven Health"
                    }
                    }
                ],
                "meta": {
                    "count": 37
                }
            }

@app.get("/product/{id}")
def get_product_by_id(id: int,db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_products:
        return db_products
    return "product not found"

@app.post("/product")
def add_product(product: Product,db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/product/{id}")
def update_product(id: int, product: Product,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
            db_product.name = product.name
            db_product.description = product.description
            db_product.price = product.price
            db_product.quantity = product.quantity
            db.commit()
            return "Product Updated Successfully"
    else:   
        return "No product Updated"

@app.delete("/product/{id}")
def delete_product(id: int,db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product Deleted Successfully"
    else:
        return "product not found"