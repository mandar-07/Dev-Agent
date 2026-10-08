from fastapi import FastAPI


app = FastAPI(
    title="DevAgent",
    description="AI-Native Software Engineering Agent",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "name": "DevAgent",
        "status": "running",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }