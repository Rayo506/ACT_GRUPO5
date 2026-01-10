#!/bin/bash

# Quick API Examples using curl
# Base URL for the API
BASE_URL="http://localhost:8000"

echo "========================================="
echo "Computer Products API - Quick Examples"
echo "========================================="
echo ""

# 1. Health Check
echo "1. Health Check"
echo "   curl $BASE_URL/health"
curl -s "$BASE_URL/health" | python3 -m json.tool
echo ""
echo ""

# 2. Create a Product
echo "2. Create a Product (Laptop)"
echo "   curl -X POST $BASE_URL/products/ -H 'Content-Type: application/json' -d '{...}'"
curl -s -X POST "$BASE_URL/products/" \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "ASUS ROG Strix G15",
    "description": "Gaming laptop with AMD Ryzen 9 and RTX 3070",
    "unit_of_measure": "unit",
    "category": "laptop",
    "price": 1499.99,
    "brand": "ASUS",
    "stock_quantity": 15,
    "specifications": {
      "processor": "AMD Ryzen 9 5900HX",
      "ram": "16GB DDR4",
      "storage": "1TB SSD",
      "gpu": "NVIDIA RTX 3070"
    }
  }' | python3 -m json.tool
echo ""
echo ""

# 3. List All Products
echo "3. List All Products"
echo "   curl $BASE_URL/products/"
curl -s "$BASE_URL/products/" | python3 -m json.tool
echo ""
echo ""

# 4. Get Specific Product
echo "4. Get Product by ID (ID=1)"
echo "   curl $BASE_URL/products/1"
curl -s "$BASE_URL/products/1" | python3 -m json.tool
echo ""
echo ""

# 5. Update Product
echo "5. Update Product (Update price and stock)"
echo "   curl -X PUT $BASE_URL/products/1 -H 'Content-Type: application/json' -d '{...}'"
curl -s -X PUT "$BASE_URL/products/1" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 1399.99,
    "stock_quantity": 12
  }' | python3 -m json.tool
echo ""
echo ""

# 6. Search by Category
echo "6. Search Products by Category (laptop)"
echo "   curl $BASE_URL/products/search/?category=laptop"
curl -s "$BASE_URL/products/search/?category=laptop" | python3 -m json.tool
echo ""
echo ""

# 7. Search by Brand
echo "7. Search Products by Brand (ASUS)"
echo "   curl $BASE_URL/products/search/?brand=ASUS"
curl -s "$BASE_URL/products/search/?brand=ASUS" | python3 -m json.tool
echo ""
echo ""

# 8. Pagination
echo "8. Get Products with Pagination (skip=0, limit=3)"
echo "   curl $BASE_URL/products/?skip=0&limit=3"
curl -s "$BASE_URL/products/?skip=0&limit=3" | python3 -m json.tool
echo ""
echo ""

# 9. Delete Product
echo "9. Delete Product (ID=1)"
echo "   curl -X DELETE $BASE_URL/products/1"
curl -s -X DELETE "$BASE_URL/products/1" -w "\nHTTP Status: %{http_code}\n"
echo ""
echo ""

# 10. Try to Get Deleted Product (Should return 404)
echo "10. Verify Product Deleted (Should return 404)"
echo "    curl $BASE_URL/products/1"
curl -s "$BASE_URL/products/1" -w "\nHTTP Status: %{http_code}\n" | python3 -m json.tool
echo ""
echo ""

echo "========================================="
echo "For more examples, see:"
echo "  - Swagger UI: $BASE_URL/docs"
echo "  - ReDoc:      $BASE_URL/redoc"
echo "========================================="
