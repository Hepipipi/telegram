# from aiogram import Router, F
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message, CallbackQuery
# from database.queryset import * 
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.filters import Command

# admin_router = Router()

# class AddCategory(StatesGroup):
#     name = State()


# @admin_router.message(Command('add_category'))
# async def add_category(message:Message, state:FSMContext):
#     await message.answer('Enter a category name')
#     await state.set_state(AddCategory.name)




# @admin_router.message(AddCategory.name)
# async def add_name(message:Message, state:FSMContext):
#     await add_category_name(message.text)
#     await message.answer('Category added')
#     await state.clear()




# class AddKey(StatesGroup):
#     key = State()
#     count = State()
#     price = State()

# @admin_router.message(Command('add_key'))
# async def add_key(message: Message, state:FSMContext):
#     await message.answer('Enter a key')
#     await state.set_state(AddKey.key)



# @admin_router.message(AddKey.key)
# async def add_count(message: Message, state:FSMContext):
#     await state.update_data(key=message.text)
#     await message.answer('Enter a count')
#     await state.set_state(AddKey.count)

# @admin_router.message(AddKey.count)
# async def add_price(message: Message, state:FSMContext):
#     await state.update_data(count=int(message.text))
#     await message.answer('Enter a price')
#     await state.set_state(AddKey.price)

# from database.models import GameKey

# @admin_router.message(AddKey.price)
# async def add_price(message: Message, state:FSMContext):
#     await state.update_data(price = int(message.text))
#     data = await state.get_data()
#     game_key = GameKey(
#         key=data['key'],
#         count = data['count'],
#         price=data['price']
#     )
#     await add_key_db(game_key)
#     await message.answer('Key is added')
#     await state.clear()



# class AddGame(StatesGroup):
#     name = State()
#     description = State()
#     image = State()
#     category_id = State()
#     key_id = State()

# @admin_router.message(Command('add_game'))
# async def add_name(message: Message, state:FSMContext):
#     await message.answer('Введите название игры')
#     await state.set_state(AddGame.name)

# @admin_router.message(AddGame.name)
# async def add_description(message: Message, state:FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer('Введите описание игры')
#     await state.set_state(AddGame.description)

# @admin_router.message(AddGame.description)
# async def add_image(message: Message, state:FSMContext):
#     await state.update_data(description=message.text)
#     await message.answer('Добавьте изображение')
#     await state.set_state(AddGame.image)


# from keyboards import categorues_kb


# @admin_router.message(AddGame.image)
# async def add_image(message: Message, state:FSMContext):
#     await state.update_data(image = message.photo[0].file_id)
#     await message.answer('Choose category', reply_markup=await categorues_kb())
#     await state.set_state(AddGame.category_id)



# @admin_router.callback_query(AddGame.category_id)
# async def add_category_game(callback :CallbackQuery):
#     category_id = 



# from aiogram import Router,F
# from aiogram.fsm.context import FSMContext
# from aiogram.types import Message,CallbackQuery
# from aiogram.filters import Command
# from database.queryset import *
# from aiogram.fsm.state import StatesGroup, State
# from config import ADMIN_ID




# admin_router = Router()


# class AddCategory(StatesGroup):
#     name = State()


# async def check_admin(message: Message) -> bool:
#     return message.from_user.id == ADMIN_ID
         









# @admin_router.message(Command('add_category'))
# async def add_category(message: Message,state:FSMContext):
#     if not await check_admin(message):
#         await message.answer('Its commands for admin')
#         return 


#     await message.answer("Введите название категории")
#     await state.set_state(AddCategory.name)

# @admin_router.message(AddCategory.name)
# async def add_name(message: Message, state:FSMContext):
#     await add_category_name(message.text)
#     await message.answer("Категория добавлена")
#     await state.clear()

# class AddGame(StatesGroup):
#     name = State()
#     description = State()
#     image = State()
#     key = State()
#     count = State()
#     price = State()
#     category_id = State()
    

# @admin_router.message(Command('add_game'))
# async def add_name(message: Message, state:FSMContext):
#     if not await check_admin(message):
#         await message.answer('Its commands for admin')
#         return 

#     await message.answer('Введите название игры')
#     await state.set_state(AddGame.name)

# @admin_router.message(AddGame.name)
# async def add_description(message: Message, state:FSMContext):
#     await state.update_data(name=message.text)
#     await message.answer('Введите описание игры')
#     await state.set_state(AddGame.description)

# @admin_router.message(AddGame.description)
# async def add_image(message: Message, state:FSMContext):
#     await state.update_data(description=message.text)
#     await message.answer('Добавьте изображение')
#     await state.set_state(AddGame.image)


# @admin_router.message(AddGame.image)
# async def add_image(message: Message, state:FSMContext):
#     await state.update_data(image = message.photo[0].file_id)
#     await message.answer('Введите ключ от игры')
#     await state.set_state(AddGame.key)

# @admin_router.message(AddGame.key)
# async def add_key(message: Message, state:FSMContext):
#     await state.update_data(key=message.text)
#     await message.answer('Введите количество игр')
#     await state.set_state(AddGame.count)

# @admin_router.message(AddGame.count)
# async def add_count(message: Message, state:FSMContext):
#     await state.update_data(count=int(message.text))
#     await message.answer('Введите цену игры')
#     await state.set_state(AddGame.price)

# from .keyboards import categories_kb2

# @admin_router.message(AddGame.price)
# async def add_price(message: Message, state:FSMContext):
#     await state.update_data(price=int(message.text))
#     await message.answer('Выберите категорию',reply_markup=await categories_kb2())
#     await state.set_state(AddGame.category_id) 





# from database.models import Game   

# @admin_router.callback_query(AddGame.category_id)
# async def add_category_id(callback: CallbackQuery, state:FSMContext):
#     category_id=callback.data.split('_')[1]
#     data = await state.get_data()
#     game = Game(
#         name = data['name'],
#         description = data['description'],
#         image = data['image'],
#         key = data['key'],
#         count = data['count'],
#         price = data['price'],
#         category_id = int(category_id)
        
#     )
#     await add_game_db(game)
#     await callback.message.answer('Игра добавлена')
#     await state.clear()




# # class DeleteCategories(StatesGroup):
# #     category = State()

# @admin_router.message(Command('delete_category'))
# async def delete_cat(message: Message):
#     if not await check_admin(message):
#         await message.answer('Its commands for admin')
#         return 

#     await message.answer('Выберите категорию',reply_markup=await categories_kb3())

# @admin_router.callback_query(F.data.startswith('category2_'))
# async def del_category(callback: CallbackQuery):
#     category_id = int(callback.data.split('_')[1])
#     await delete_categories(category_id)
#     await callback.message.answer('Категория удалена')







from aiogram import Router,F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message,CallbackQuery
from aiogram.filters import Command
from database.queryset import *
from aiogram.fsm.state import StatesGroup, State
from config import ADMIN_ID


admin_router = Router()


class AddCategory(StatesGroup):
    name = State()

async def check_admin(message:Message) -> bool:
    return message.from_user.id == ADMIN_ID  
        
         

@admin_router.message(Command('add_category'))#,F.func(check_admin)
async def add_category(message: Message,state:FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для администратора")
        return    
    await message.answer("Введите название категории")
    await state.set_state(AddCategory.name)

@admin_router.message(AddCategory.name)
async def add_name(message: Message, state:FSMContext):
    await add_category_name(message.text)
    await message.answer("Категория добавлена")
    await state.clear()


class AddGame(StatesGroup):
    name = State()
    description = State()
    image = State()
    key = State()
    count = State()
    price = State()
    category_id = State()
    

@admin_router.message(Command('add_game'))
async def add_name(message: Message, state:FSMContext):
    if not await check_admin(message):
        await message.answer("Это команда только для администратора")
        return    
    await message.answer('Введите название игры')
    await state.set_state(AddGame.name)

@admin_router.message(AddGame.name)
async def add_description(message: Message, state:FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите описание игры')
    await state.set_state(AddGame.description)

@admin_router.message(AddGame.description)
async def add_image(message: Message, state:FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Добавьте изображение')
    await state.set_state(AddGame.image)


@admin_router.message(AddGame.image)
async def add_image(message: Message, state:FSMContext):
    await state.update_data(image = message.photo[0].file_id)
    await message.answer('Введите ключ от игры')
    await state.set_state(AddGame.key)

@admin_router.message(AddGame.key)
async def add_key(message: Message, state:FSMContext):
    await state.update_data(key=message.text)
    await message.answer('Введите количество игр')
    await state.set_state(AddGame.count)

@admin_router.message(AddGame.count)
async def add_count(message: Message, state:FSMContext):
    await state.update_data(count=message.text)
    await message.answer('Введите цену игры')
    await state.set_state(AddGame.price)

from .keyboards import categories_kb2

@admin_router.message(AddGame.price)
async def add_price(message: Message, state:FSMContext):
    await state.update_data(price=message.text)
    await message.answer('Выберите категорию',reply_markup=await categories_kb2())
    await state.set_state(AddGame.category_id)    

from database.models import Game

@admin_router.callback_query(AddGame.category_id)
async def add_category_id(callback: CallbackQuery, state:FSMContext):
    await state.update_data(category_id=callback.data.split('_')[1])
    data = await state.get_data()
    game = Game(
        name =data['name'],
        description=data['description'],
        image=data['image'],
        key=data['key'],
        count=int(data['count']),
        price=int(data['price']),
        category_id=int(data['category_id'])
    )
    await add_game_db(game)
    await callback.message.answer('Игра добавлена')
    await state.clear()
    


# class DeleteCategory(StatesGroup):
#     category = State()

from .keyboards import categories_kb3

@admin_router.message(Command('delete_category'))
async def delete_cat(message: Message):
    if not await check_admin(message):
        await message.answer("Это команда только для администратора")
        return   
    await message.answer('Выберите категорию',reply_markup=await categories_kb3())




# @admin_router.callback_query(DeleteCategory.category) 
# async def del_category(callback : CallbackQuery):
#     category_id = int(callback.data.split('_')[1])
#     await delete_category(category_id)

