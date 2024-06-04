from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3100)


app = FastAPI()

dior = {
    1: {
        "name": "\n                            Junon\n                            ",
        "price": "20.0",
        "price_sign": "£",
        "currency": "GBP",
        "image_link": "https://www.dior.com/beauty/version-5.1432748111912/resize-image/ep/0/214/90/0/v6_packshots_sku_pdg%252FPDG_Y0002959-F000355494.jpg",
        "product_link": "https://www.dior.com/beauty/en_gb/fragrance-beauty/makeup/nails/nail-lacquers/pr-naillacquers-y0002959_f000355494-couture-colour-gel-shine-long-wear.html",
        "website_link": "https://www.dior.com",
        "description": "Discover the new-generation Dior Vernis and its ingenious formula that plays up the gel effect.",
        "rating": None,
        "category": None,
        "product_type": "nail_polish"
    },
    2: {
        "name": "\n                            Matte\n                            ",
        "price": "20.0",
        "price_sign": "£",
        "currency": "GBP",
        "image_link": "https://www.dior.com/beauty/version-5.1432748111912/resize-image/ep/0/214/90/0/v6_packshots_sku_pdg%252FPDG_Y0002959-F000355999.jpg",
        "product_link": "https://www.dior.com/beauty/en_gb/fragrance-beauty/makeup/nails/nail-lacquers/pr-naillacquers-y0003759_f000375999-couture-colour-long-wear-nail-lacquer.html",
        "website_link": "https://www.dior.com",
        "description": "Discover the new-generation Dior Vernis and its ingenious formula that accentuates the gel effect.",
        "rating": None,
        "category": None,
        "product_type": "nail_polish"
    },
    3: {
        "name": "\n                            Poison Metal\n                            ",
        "price": "20.0",
        "price_sign": "£",
        "currency": "GBP",
        "image_link": "https://www.dior.com/beauty/version-5.1432748111912/resize-image/ep/0/214/90/0/packshots%252FPDG_Y0003559_F000355979.jpg",
        "product_link": "https://www.dior.com/beauty/en_gb/fragrance-beauty/makeup/nails/nail-lacquers/pr-naillacquers-y0003759_f000355979-couture-colour-long-wear-nail-lacquer.html",
        "website_link": "https://www.dior.com",
        "description": "Discover the new-generation Dior Vernis and its ingenious formula that accentuates the gel effect.",
        "rating": None,
        "category": None,
        "product_type": "nail_polish"
    },
    4: {
        "name": "\n                            Jungle Matte\n                            ",
        "price": "20.0",
        "price_sign": "£",
        "currency": "GBP",
        "image_link": "https://www.dior.com/beauty/version-5.1432748111912/resize-image/ep/0/214/90/0/packshots%252FPDG_Y0003759_F000355614.jpg",
        "product_link": "https://www.dior.com/beauty/en_gb/fragrance-beauty/makeup/nails/nail-lacquers/pr-naillacquers-y0003759_f000355614-couture-colour-long-wear-nail-lacquer.html",
        "website_link": "https://www.dior.com",
        "description": "Discover the new-generation Dior Vernis and its ingenious formula that accentuates the gel effect.",
        "rating": None,
        "category": None,
        "product_type": "nail_polish"
    },
    5: {
        "name": "\n                            Miss Satin\n                            ",
        "price": "20.0",
        "price_sign": "£",
        "currency": "GBP",
        "image_link": "https://www.dior.com/beauty/version-5.1432748111912/resize-image/ep/0/214/90/0/packshots%252FPDG_Y0003759_F000355162.jpg",
        "product_link": "https://www.dior.com/beauty/en_gb/fragrance-beauty/makeup/nails/nail-lacquers/pr-naillacquers-y0003759_f000355162-couture-colour-long-wear-nail-lacquer.html",
        "website_link": "https://www.dior.com",
        "description": "Discover the new-generation Dior Vernis and its ingenious formula that accentuates the gel effect.",
        "rating": None,
        "category": None,
        "product_type": "nail_polish"
    }
}

class Product(BaseModel):
    name: str
    price: str
    price_sign: str
    currency: str
    image_link: str
    product_link: str
    website_link: str
    description: Optional[str] = None
    rating: Optional[float] = None
    category: Optional[str] = None
    product_type: str

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[str] = None
    price_sign: Optional[str] = None
    currency: Optional[str] = None
    image_link: Optional[str] = None
    product_link: Optional[str] = None
    website_link: Optional[str] = None
    description: Optional[str] = None
    rating: Optional[float] = None
    category: Optional[str] = None
    product_type: Optional[str] = None

# Get all products
@app.get("/products/")
def read_products():
    return dior

# Get product by id
@app.get("/products/{product_id}")
def read_product_by_id(product_id: int):
    if product_id not in dior:
        return {"error": "Product not found"}
    return dior[product_id]

# Get product price by id
@app.get("/products/{product_id}/price")
def read_product_price_by_id(product_id: int):
    if product_id not in dior:
        return {"error": "Product not found"}
    return {"price": dior[product_id]["price"]}

# Get product name use query parameter
@app.get("/products/name/")
def read_product_name(name: str):
    for product_id, product in dior.items():
        if product["name"].strip() == name.strip():
            return product
    return {"error": "Product not found"}

# Create a new product
@app.post("/products/")
def create_product(product: Product):
    product_id = len(dior) + 1
    dior[product_id] = product.dict()
    return {"message": "Product created successfully"}

# Update a product
@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductUpdate):
    if product_id not in dior:
        return {"error": "Product not found"}
    update_data = product.dict(exclude_unset=True)
    dior[product_id].update(update_data)
    return {"message": "Product updated successfully"}

# Delete a product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    if product_id not in dior:
        return {"error": "Product not found"}
    del dior[product_id]
    return {"message": "Product deleted successfully"}
