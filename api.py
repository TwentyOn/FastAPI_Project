from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'hello world'}

@app.get('/hello')
async def welcome_user(user: str) -> dict:
    return {'user': f'hello {user}!'}

@app.get('/product')
async def detail_view(product_id: int) -> dict:
    return {'product': f'Stock number {product_id}'}