from fastapi import APIRouter
from api.services.redis_service import get_top_products
from api.services.mongo_service import get_product_info

router = APIRouter(prefix="/recommend", tags=["Recommender"])

@router.get("/{user_id}")
def recommend(user_id: int):
    top_products = get_top_products(user_id)

    recommendations = []
    for product_id, score in top_products:
        product = get_product_info(product_id)
        if product:
            product["score"] = score
            recommendations.append(product)

    return {
        "user_id": user_id,
        "recommendations": recommendations
    }
