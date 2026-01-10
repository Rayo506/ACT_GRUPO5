# API Scripts

This directory contains helpful scripts for testing and demonstrating the Computer Products API.

## Available Scripts

### 1. load_sample_data.sh

Loads 16 sample computer products into the API and demonstrates various API operations.

**Products loaded:**
- 3 Laptops (Dell, Apple, Lenovo)
- 2 Monitors (Samsung, LG)
- 2 Keyboards (Logitech, Razer)
- 2 Mice (Logitech, Razer)
- 2 Storage Devices (Samsung, Western Digital)
- 2 RAM modules (Corsair, G.Skill)
- 2 Processors (AMD, Intel)
- 2 Graphics Cards (NVIDIA, AMD)

**Usage:**

```bash
# Make sure the API is running first
cd /path/to/apiservices
make run

# In another terminal, run the script
./scripts/load_sample_data.sh
```

**Features:**
- Color-coded output for better readability
- Health check before loading data
- Demonstrates CREATE, READ, UPDATE operations
- Shows search by category and brand
- Demonstrates pagination
- Pretty-printed JSON output

### 2. api_examples.sh

Quick reference guide showing common API operations with curl commands.

**Usage:**

```bash
# Make sure the API is running first
cd /path/to/apiservices
make run

# In another terminal, run the script
./scripts/api_examples.sh
```

**Demonstrates:**
1. Health check
2. Create a product (Gaming Laptop)
3. List all products
4. Get a specific product by ID
5. Update product (price and stock)
6. Search by category
7. Search by brand
8. Pagination
9. Delete a product
10. Verify deletion (404 error)

## Prerequisites

Before running these scripts, ensure:

1. **API is running:**
   ```bash
   make run
   # Or manually:
   # source venv/bin/activate
   # uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Python 3 is installed** (for json.tool formatting)

3. **curl is installed** (usually pre-installed on macOS/Linux)

## Testing the API

### Option 1: Use the scripts
```bash
# Load comprehensive sample data
./scripts/load_sample_data.sh

# Or run quick examples
./scripts/api_examples.sh
```

### Option 2: Manual curl commands

**Create a product:**
```bash
curl -X POST "http://localhost:8000/products/" \
  -H "Content-Type: application/json" \
  -d '{
    "product_name": "Logitech MX Master 3",
    "description": "Advanced wireless mouse",
    "unit_of_measure": "unit",
    "category": "mouse",
    "price": 99.99,
    "brand": "Logitech",
    "stock_quantity": 50,
    "specifications": {
      "connectivity": "Bluetooth/USB",
      "dpi": "4000",
      "buttons": "7"
    }
  }'
```

**List all products:**
```bash
curl http://localhost:8000/products/
```

**Get a specific product:**
```bash
curl http://localhost:8000/products/1
```

**Update a product:**
```bash
curl -X PUT "http://localhost:8000/products/1" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 89.99,
    "stock_quantity": 45
  }'
```

**Search by category:**
```bash
curl "http://localhost:8000/products/search/?category=laptop"
```

**Search by brand:**
```bash
curl "http://localhost:8000/products/search/?brand=Dell"
```

**Pagination:**
```bash
curl "http://localhost:8000/products/?skip=0&limit=10"
```

**Delete a product:**
```bash
curl -X DELETE "http://localhost:8000/products/1"
```

### Option 3: Interactive API Documentation

Visit the auto-generated API documentation in your browser:

- **Swagger UI:** http://localhost:8000/docs
  - Interactive interface to test all endpoints
  - Try out requests directly from the browser
  - See request/response schemas

- **ReDoc:** http://localhost:8000/redoc
  - Clean, responsive API documentation
  - Easy to read and navigate

## Tips

1. **Format JSON output:**
   ```bash
   curl http://localhost:8000/products/ | python3 -m json.tool
   ```

2. **Save response to file:**
   ```bash
   curl http://localhost:8000/products/ > products.json
   ```

3. **Show HTTP status code:**
   ```bash
   curl -w "\nHTTP Status: %{http_code}\n" http://localhost:8000/products/1
   ```

4. **Verbose output (see headers):**
   ```bash
   curl -v http://localhost:8000/products/
   ```

## Troubleshooting

**Error: "Could not connect to localhost:8000"**
- Make sure the API is running: `make run`
- Check if port 8000 is already in use
- Verify the API started successfully (check terminal output)

**Error: "API is not running"** (from load_sample_data.sh)
- Start the API first: `make run` in the apiservices directory
- Wait a few seconds for the API to initialize

**JSON formatting not working:**
- Ensure Python 3 is installed: `python3 --version`
- Try using `jq` instead: `curl http://localhost:8000/products/ | jq`

## Next Steps

After loading sample data:
1. Explore the API using Swagger UI at http://localhost:8000/docs
2. Run the test suite: `make test`
3. Try modifying the scripts to add your own products
4. Experiment with different search and filter combinations
