from fastapi import APIRouter
from schemas import Item

router = APIRouter()

item_list = {}

@router.post('/item')
async def post_item(item: Item) -> dict:
    if item_list:
        new_id = str(max((int(i) for i in item_list.keys())))
    else:
        new_id = '1'
    item_list[new_id] = {'name': item.name, 'price': item.price,
                         'description': item.description}
    return {'status': 'success', 'item': item_list[new_id]}


@router.get('/item/{pk}')
async def get_item(pk:int) -> Item:
    if item_list[str(pk)]:
        return item_list[str(pk)]