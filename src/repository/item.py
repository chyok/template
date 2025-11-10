from typing import Dict, Any
from src.repository.abc.i_item import IItemRepository
from src.schema.model.item import Item
from src.schema.request.item import ItemCreate


# This would be your actual database connection/session in a real application.
# For this template, we'll simulate it with a simple in-memory dictionary.
class InMemoryDatabase:
    def __init__(self):
        self.items: Dict[int, Any] = {}
        self.next_id = 1

# A single instance to act as our "database"
db = InMemoryDatabase()

class ItemRepositoryImpl(IItemRepository):
    def __init__(self, database: InMemoryDatabase = db):
        self._db = database

    def get_item(self, item_id: int) -> Item | None:
        item_data = self._db.items.get(item_id)
        if item_data:
            return Item(**item_data)
        return None

    def create_item(self, item_create: ItemCreate) -> Item:
        item_id = self._db.next_id
        item_data = item_create.model_dump()
        item_data["id"] = item_id

        self._db.items[item_id] = item_data
        self._db.next_id += 1

        return Item(**item_data)
