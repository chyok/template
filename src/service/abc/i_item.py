from abc import ABC, abstractmethod
from typing import Optional
from src.schema.model.item import Item
from src.schema.request.item import ItemCreate


class IItemService(ABC):
    @abstractmethod
    def get_item(self, item_id: int) -> Optional[Item]:
        raise NotImplementedError

    @abstractmethod
    def create_item(self, item_create: ItemCreate) -> Item:
        raise NotImplementedError
