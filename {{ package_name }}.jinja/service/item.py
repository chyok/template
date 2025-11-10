from fastapi import Depends
from {{ package_name }}.service.abc.i_item import IItemService
from {{ package_name }}.repository.abc.i_item import IItemRepository
from {{ package_name }}.repository.item import ItemRepositoryImpl
from {{ package_name }}.schema.model.item import Item
from {{ package_name }}.schema.request.item import ItemCreate


class ItemServiceImpl(IItemService):
    def __init__(self, item_repo: IItemRepository = Depends(ItemRepositoryImpl)):
        self._item_repo = item_repo

    def get_item(self, item_id: int) -> Item | None:
        return self._item_repo.get_item(item_id)

    def create_item(self, item_create: ItemCreate) -> Item:
        # Here you could add business logic, e.g., validation, calculations, etc.
        return self._item_repo.create_item(item_create)
