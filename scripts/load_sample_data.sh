#!/bin/bash

# Sample Data Loader and API Demo Script
# This script loads sample computer products and demonstrates API functionality

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# API Base URL
BASE_URL="http://localhost:8000"

# Function to print section headers
print_header() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

# Function to print success messages
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

# Function to print info messages
print_info() {
    echo -e "${YELLOW}→ $1${NC}"
}

# Function to check if API is running
check_api() {
    print_header "Checking API Health"
    response=$(curl -s -o /dev/null -w "%{http_code}" "$BASE_URL/health")
    if [ "$response" -eq 200 ]; then
        print_success "API is running and healthy!"
        curl -s "$BASE_URL/health" | python3 -m json.tool
    else
        echo -e "${RED}✗ API is not running. Please start it with 'make run'${NC}"
        exit 1
    fi
}

# Function to create a product
create_product() {
    local name="$1"
    local description="$2"
    local category="$3"
    local price="$4"
    local brand="$5"
    local stock="$6"
    local specs="$7"

    print_info "Creating product: $name"
    response=$(curl -s -X POST "$BASE_URL/products/" \
        -H "Content-Type: application/json" \
        -d "{
            \"product_name\": \"$name\",
            \"description\": \"$description\",
            \"unit_of_measure\": \"unit\",
            \"category\": \"$category\",
            \"price\": $price,
            \"brand\": \"$brand\",
            \"stock_quantity\": $stock,
            \"specifications\": $specs
        }")
    echo "$response" | python3 -m json.tool
    print_success "Product created successfully!\n"
}

# Check if API is running
check_api

# Load Sample Data
print_header "Loading Sample Computer Products"

# Laptops
create_product \
    "Dell XPS 15" \
    "High-performance laptop with 15.6-inch 4K display, perfect for professionals and creators" \
    "laptop" \
    1599.99 \
    "Dell" \
    25 \
    '{"processor": "Intel Core i7-12700H", "ram": "16GB DDR5", "storage": "512GB NVMe SSD", "display": "15.6 inch 4K OLED", "graphics": "NVIDIA RTX 3050 Ti"}'

create_product \
    "MacBook Pro 14" \
    "Apple M2 Pro powered laptop with stunning Liquid Retina XDR display" \
    "laptop" \
    1999.99 \
    "Apple" \
    15 \
    '{"processor": "Apple M2 Pro", "ram": "16GB Unified Memory", "storage": "512GB SSD", "display": "14.2 inch Liquid Retina XDR", "battery": "Up to 18 hours"}'

create_product \
    "Lenovo ThinkPad X1 Carbon" \
    "Ultra-lightweight business laptop with enterprise-grade security" \
    "laptop" \
    1399.99 \
    "Lenovo" \
    20 \
    '{"processor": "Intel Core i7-1260P", "ram": "16GB LPDDR5", "storage": "1TB PCIe SSD", "display": "14 inch FHD+", "weight": "2.48 lbs"}'

# Monitors
create_product \
    "Samsung Odyssey G7" \
    "32-inch curved gaming monitor with 240Hz refresh rate and 1ms response time" \
    "monitor" \
    699.99 \
    "Samsung" \
    12 \
    '{"size": "32 inches", "resolution": "2560x1440", "refresh_rate": "240Hz", "panel": "VA Curved", "response_time": "1ms"}'

create_product \
    "LG UltraFine 4K" \
    "27-inch 4K IPS monitor with USB-C connectivity and 99% sRGB coverage" \
    "monitor" \
    499.99 \
    "LG" \
    18 \
    '{"size": "27 inches", "resolution": "3840x2160", "panel": "IPS", "color_gamut": "99% sRGB", "ports": "USB-C, HDMI, DisplayPort"}'

# Keyboards
create_product \
    "Logitech MX Keys" \
    "Wireless illuminated keyboard with smart backlighting and multi-device support" \
    "keyboard" \
    99.99 \
    "Logitech" \
    45 \
    '{"type": "Membrane", "connectivity": "Bluetooth/USB Receiver", "backlight": "Smart illumination", "battery": "Up to 10 days"}'

create_product \
    "Razer BlackWidow V3" \
    "Mechanical gaming keyboard with Razer Green switches and RGB Chroma lighting" \
    "keyboard" \
    139.99 \
    "Razer" \
    30 \
    '{"type": "Mechanical", "switches": "Razer Green", "rgb": "Chroma RGB", "features": "Programmable macros"}'

# Mice
create_product \
    "Logitech MX Master 3S" \
    "Advanced wireless mouse with ultra-fast scrolling and ergonomic design" \
    "mouse" \
    99.99 \
    "Logitech" \
    50 \
    '{"type": "Wireless", "dpi": "8000", "buttons": "7", "connectivity": "Bluetooth/USB Receiver", "battery": "Up to 70 days"}'

create_product \
    "Razer DeathAdder V3" \
    "Ergonomic gaming mouse with Focus Pro 30K optical sensor" \
    "mouse" \
    69.99 \
    "Razer" \
    35 \
    '{"type": "Wired/Wireless", "dpi": "30000", "buttons": "8", "sensor": "Focus Pro 30K", "weight": "59g"}'

# Storage (Disks)
create_product \
    "Samsung 980 PRO" \
    "PCIe 4.0 NVMe M.2 SSD with exceptional speed for gaming and heavy workloads" \
    "disk" \
    149.99 \
    "Samsung" \
    40 \
    '{"capacity": "1TB", "interface": "NVMe PCIe 4.0", "read_speed": "7000 MB/s", "write_speed": "5000 MB/s", "form_factor": "M.2 2280"}'

create_product \
    "WD Black SN850X" \
    "High-performance NVMe SSD optimized for gaming with Game Mode 2.0" \
    "disk" \
    129.99 \
    "Western Digital" \
    28 \
    '{"capacity": "1TB", "interface": "NVMe PCIe 4.0", "read_speed": "7300 MB/s", "write_speed": "6300 MB/s", "features": "Game Mode 2.0"}'

# RAM
create_product \
    "Corsair Vengeance RGB PRO" \
    "High-performance DDR4 memory with dynamic RGB lighting" \
    "ram" \
    89.99 \
    "Corsair" \
    55 \
    '{"type": "DDR4", "capacity": "16GB (2x8GB)", "speed": "3200MHz", "rgb": "Dynamic RGB lighting", "latency": "CL16"}'

create_product \
    "G.Skill Trident Z5 RGB" \
    "Premium DDR5 memory with stunning RGB and extreme performance" \
    "ram" \
    159.99 \
    "G.Skill" \
    32 \
    '{"type": "DDR5", "capacity": "32GB (2x16GB)", "speed": "6000MHz", "rgb": "Full RGB lighting", "latency": "CL36"}'

# Processors
create_product \
    "AMD Ryzen 9 7950X" \
    "16-core, 32-thread desktop processor with exceptional multi-threaded performance" \
    "processor" \
    699.99 \
    "AMD" \
    8 \
    '{"cores": "16", "threads": "32", "base_clock": "4.5 GHz", "boost_clock": "5.7 GHz", "socket": "AM5", "tdp": "170W"}'

create_product \
    "Intel Core i9-13900K" \
    "24-core hybrid processor with industry-leading gaming performance" \
    "processor" \
    589.99 \
    "Intel" \
    10 \
    '{"cores": "24 (8P+16E)", "threads": "32", "base_clock": "3.0 GHz", "boost_clock": "5.8 GHz", "socket": "LGA1700", "tdp": "125W"}'

# Graphics Cards
create_product \
    "NVIDIA GeForce RTX 4080" \
    "High-end graphics card with ray tracing and DLSS 3 for 4K gaming" \
    "graphics_card" \
    1199.99 \
    "NVIDIA" \
    6 \
    '{"memory": "16GB GDDR6X", "cuda_cores": "9728", "boost_clock": "2505 MHz", "power": "320W", "features": "Ray Tracing, DLSS 3"}'

create_product \
    "AMD Radeon RX 7900 XTX" \
    "Flagship RDNA 3 graphics card for extreme gaming and content creation" \
    "graphics_card" \
    999.99 \
    "AMD" \
    7 \
    '{"memory": "24GB GDDR6", "stream_processors": "6144", "boost_clock": "2500 MHz", "power": "355W", "features": "Ray Tracing, FSR 3"}'

print_success "Sample data loaded successfully!"

# API Demonstrations
print_header "API Demonstration - List All Products"
print_info "GET $BASE_URL/products/"
curl -s "$BASE_URL/products/" | python3 -m json.tool | head -50
echo -e "\n${YELLOW}... (showing first 50 lines)${NC}\n"

print_header "API Demonstration - Get Specific Product"
print_info "GET $BASE_URL/products/1"
curl -s "$BASE_URL/products/1" | python3 -m json.tool

print_header "API Demonstration - Search by Category (Laptops)"
print_info "GET $BASE_URL/products/search/?category=laptop"
curl -s "$BASE_URL/products/search/?category=laptop" | python3 -m json.tool

print_header "API Demonstration - Search by Brand (Logitech)"
print_info "GET $BASE_URL/products/search/?brand=Logitech"
curl -s "$BASE_URL/products/search/?brand=Logitech" | python3 -m json.tool

print_header "API Demonstration - Pagination (First 5 Products)"
print_info "GET $BASE_URL/products/?skip=0&limit=5"
curl -s "$BASE_URL/products/?skip=0&limit=5" | python3 -m json.tool

print_header "API Demonstration - Update Product Price"
print_info "PUT $BASE_URL/products/1 (Update Dell XPS 15 price to 1499.99)"
curl -s -X PUT "$BASE_URL/products/1" \
    -H "Content-Type: application/json" \
    -d '{"price": 1499.99}' | python3 -m json.tool

print_header "API Demonstration - Verify Price Update"
print_info "GET $BASE_URL/products/1"
curl -s "$BASE_URL/products/1" | python3 -m json.tool

print_header "Summary"
print_success "Loaded 16 sample products covering all categories"
print_success "Demonstrated GET, POST, PUT operations"
print_success "Showed search and pagination features"
echo -e "\n${GREEN}API Documentation available at:${NC}"
echo -e "  ${BLUE}Swagger UI: $BASE_URL/docs${NC}"
echo -e "  ${BLUE}ReDoc:      $BASE_URL/redoc${NC}\n"
