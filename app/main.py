from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import products

app = FastAPI(
    title="FigursAPI",
    description="Web service para figuras de anime y comic",
    version="1.0.0"
)

# CORS para tu web
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a FigursAPI", "docs": "/docs"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
