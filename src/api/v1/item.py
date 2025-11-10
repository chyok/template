from fastapi import APIRouter, Depends, HTTPException
from src.service.abc.i_item import IItemService
from src.service.item import ItemServiceImpl
from src.schema.request.item import ItemCreate
from src.schema.response.item import ItemResponse

router = APIRouter()


@router.get("/items/{item_id}", response_model=ItemResponse)
def read_item(
    item_id: int,
    item_service: IItemService = Depends(ItemServiceImpl)
):
    item = item_service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/items/", response_model=ItemResponse, status_code=201)
def create_item(
    item_create: ItemCreate,
    item_service: IItemService = Depends(ItemServiceImpl)
):
    return item_service.create_item(item_create)
