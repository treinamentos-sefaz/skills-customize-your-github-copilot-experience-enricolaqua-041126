from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Testing FastAPI Endpoints with Pytest")


class Item(BaseModel):
    id: int
    name: str
    price: float


items: list[Item] = []


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/items")
def create_item(item: Item) -> dict[str, Item]:
    items.append(item)
    return {"item": item}


@app.get("/items")
def list_items() -> dict[str, list[Item]]:
    return {"items": items}


@app.get("/items/{item_id}")
def get_item(item_id: int) -> dict[str, Item]:
    for item in items:
        if item.id == item_id:
            return {"item": item}
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
