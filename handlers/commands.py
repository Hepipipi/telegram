# from aiogram import Router, F
# from aiogram.filters import Command, CommandStart
# from aiogram.types import Message, CallbackQuery, FSInputFile
# from .keyboards import * 

# router = Router()

# @router.message(CommandStart())
# async def start(message: Message):
#     await message.answer(f'Hello, i am bot for buying keys {message.from_user.full_name}!', reply_markup=menu_kb)

# # @router.message(Command('help'))
# # async def help(message: Message):
# #     await message.answer_photo('C:\Users\User\OneDrive\Рабочий стол\telegram\database\kkkk.png')

# # @router.message(Command('help'))
# # async def help(message: Message):
# #     await message.answer_dice('dice')

# @router.message(F.text.lower() == 'hello')
# async def hello(message:Message):
#     await message.answer('Hello, how are you?')



# @router.message(F.text.startswith('Bye'))
# async def bye(message:Message):
#     await message.answer('GoodBye')




# @router.message(F.text == 'Are you good?')
# async def good(message:Message):
#     await message.answer('Yeah')




# @router.message(F.text == 'Category')
# async def cat(message:Message):
#     await message.answer('Choose Categories:  ', reply_markup= await categorues_kb())



# @router.message(F.text == 'All games')
# async def games(message:Message):
#     await message.answer('Choose games :', reply_markup= await games_kb())




# @router.message(Command('phone'))
# async def phone(message: Message):
#     await message.answer(' our phone +997 67 56 445')



# @router.message(Command('id'))
# async def id(message: Message):
#      await message.answer(f'Your id and username {message.from_user.id}, {message.from_user.username} ')

    

# @router.callback_query(F.data.startswith('category_'))
# async def category_game(callback: CallbackQuery):
#     category_i = callback.data.split('_')[1]
#     category_id = int(category_i)  
#     await callback.message.answer(f'You choose category {category_id}', reply_markup=await game_kb(category_id)) 


# from database.queryset import get_game1

# from database.queryset import get_price


# @router.callback_query(F.data.startswith('game_'))
# async def game(callback: CallbackQuery):
#     game_i = callback.data.split('_')[1]
#     game_id = int(game_i)
#     game = await get_game1(game_id)
#     # if game.image.startswith('https') or game.image.startswith('AgAC'):
#     #     image = game.image
#     # else:
#     #     image = FSInputFile(game.image)
#     image = FSInputFile(game.image)
#     await callback.message.answer_photo(photo=image, caption=f'{game.name} \n {game.description}', reply_markup=await game_key_kb(game_id))





# from aiogram import Router,F
# from aiogram.filters import Command,CommandStart
# from aiogram.types import Message, CallbackQuery,FSInputFile
# from .keyboards import * 

# router = Router()

# @router.message(Command('start'))
# async def start(message: Message):
#     await message.answer(f"""Привет {message.from_user.full_name}, 
#     я бот продавец ключей для игр \n чем могу помочь?""",reply_markup=menu_kb)


# # @router.message(F.text.lower() == 'привет')
# # async def hello(message: Message):
# #     await message.answer('Привет, как дела?')

# # @router.message(F.text.startswith('пока'))
# # async def byebye(message: Message):
# #     await message.answer('До свидания ')



# @router.message(F.text == 'Category') 
# async def categories(message: Message): 
#     await message.answer('Выберите категорию:',reply_markup= await categories_kb())


# @router.message(F.text == 'All games') 
# async def games(message: Message): 
#     await message.answer('Выберите игру:', reply_markup= await games_kb())


# @router.message(Command("help"))
# async def help(message: Message):
#     await message.answer('<h1> dice </h1> hello')
 
# @router.callback_query(F.data == 'Back')
# async def back_to_categories(callback: CallbackQuery):
#     await callback.message.delete()
#     await callback.message.answer('Choose category', reply_markup= await categories_kb())



# @router.callback_query(F.data.startswith('category_'))
# async def category_game(callback: CallbackQuery):
#     await callback.message.delete()
#     category_id = int(callback.data.split('_')[1])

#     await callback.message.answer('Игры по этой категории: ',
#         reply_markup=await games_kb(category_id))
   


    
# from database.queryset import get_game

# @router.callback_query(F.data.startswith('game_'))
# async def game(callback: CallbackQuery):
#     await callback.message.delete()
#     game_id = int(callback.data.split('_')[1])
#     game = await get_game(game_id)
#     if game.image.startswith('http') or game.image.startswith('AgAC'):
#         image = game.image
#     else:
#         image = FSInputFile(game.image)
#     await callback.message.answer_photo(photo=image,caption=f'{game.name} \n {game.description}'
#                            )

# # Напишите кнопку для покупки в детальной информации о игре
# # В кнопке должно находиться колличество ключей (50) и сумма в $
# # Кнопка находиться под описанием к игре



from aiogram import Router,F
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, CallbackQuery,FSInputFile
from .keyboards import *
from .admin import * 
from config import * 

async def check_admin(message: Message) -> bool:
    return message.from_user.id == ADMIN_ID
         


router = Router()

@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"""Привет {message.from_user.id}, 
    я бот продавец ключей для игр \n чем могу помочь?""",reply_markup=menu_kb)


# @router.message(F.text.lower() == 'привет')
# async def hello(message: Message):
#     await message.answer('Привет, как дела?')

# @router.message(F.text.startswith('пока'))
# async def byebye(message: Message):
#     await message.answer('До свидания ')

@router.message(F.text == 'Category') 
async def categories(message: Message): 
    await message.answer('Выберите категорию:',reply_markup= await categories_kb()) 

@router.message(F.text == 'All games') 
async def games(message: Message): 
    await message.answer('Выберите игру:')



@router.message(F.text == 'All games') 
async def games(message: Message): 
    await message.answer('Выберите игру:', reply_markup=games_kb_paginate(page=1))




@router.message(F.text == 'Категории') 
async def categories(message: Message): 
    await message.answer('Выберите категорию:',reply_markup= await categories_kb()) 



@router.message(F.text == 'Categories') 
async def categories(message: Message): 
    await message.answer('Выберите категорию:',reply_markup= await categories_kb()) 




@router.message(F.text == 'Все игры') 
async def games(message: Message): 
    await message.answer('Выберите игру:')




# @router.message(Command("help"))
# async def help(message: Message):
#     await message.answer('<h1> dice </h1> hello')
 

@router.callback_query(F.data == 'back_to_categories')
async def back_to_categories(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer('Выберите категорию:', 
    reply_markup= await categories_kb())


@router.callback_query(F.data.startswith('delete_')) 
async def del_game(callback: CallbackQuery):
    # if not await check_admin(message):
    #     await message.answer('Its commands for admin')
    #     return 
    game_id = int(callback.data.split('_')[1])
    await delete_game(game_id)
    await callback.message.answer('Game deleted')


# @router.callback_query(F.data.startswith('category_'))
# async def category_game(callback: CallbackQuery):
#     await callback.message.delete()
#     category_id = int(callback.data.split('_')[1])
#     await callback.message.answer('Игры по этой категории: ',
#         reply_markup=await games_kb(category_id, page=1))
    

@router.callback_query(F.data.startswith('category_'))
async def category_game(callback: CallbackQuery):
    await callback.message.delete()
    category_id = int(callback.data.split('_')[1])
    await callback.message.answer('Игры по этой категории: ',
        reply_markup=await games_kb(category_id,page=1))

@router.callback_query(F.data.startswith('page_'))
async def game_paginate(callback: CallbackQuery):
    # await callback.message.delete()
    data = callback.data.split('_')
    category_id = int(data[1])
    page = int(data[2])
    await callback.message.edit_reply_markup(
        reply_markup= await games_kb(category_id,page)
    )





@router.callback_query(F.data.startswith('all_page_'))
async def all_game_paginate(callback: CallbackQuery):
    # await callback.message.delete()
    data = callback.data.split('_')
    category_id = int(data[1])
    page = int(data[2])
    await callback.message.edit_reply_markup(
        reply_markup= await games_kb_paginate(page=1)
    )


# @router.callback_query(F.data.startswith('page_'))
# async def game_paginate(callback: CallbackQuery):
#     # await callback.message.delete()
#     data = callback.data.split('_')
#     category_id = data[1]
#     page = int(data[2])
#     await callback.message.edit_reply_markup(
#         reply_markup= await games_kb(category_id, page)
#     )
    
from database.queryset import get_game

@router.callback_query(F.data.startswith('game_'))
async def game(callback: CallbackQuery):
    # if not await check_admin(callback.message):
    #     await callback.message.answer('Its commands for admin')
    #     return 
    await callback.message.delete()
    game_id = int(callback.data.split('_')[1])
    game = await get_game(game_id)
    if game.image.startswith('http') or game.image.startswith('AgAC'):
        image = game.image
    else:
        image = FSInputFile(game.image)
    await callback.message.answer_photo(photo=image,caption=f'{game.name} \n {game.description}', reply_markup= await back_to_categories_kb(game_id) #await back_to_categories_kb()
                           )




# Напишите кнопку для покупки в детальной информации о игре
# В кнопке должно находиться колличество ключей (50) и сумма в $
# Кнопка находиться под описанием к игре

from database.payment import create_payment

@router.callback_query(F.data.startswith('buy_game_'))

async def buy(callback: CallbackQuery):
    game_id = int(callback.data.split('_')[2])
    game = await get_game(game_id)

    payment = await create_payment(game.price, f'Byuing game{game.name}')
    await callback.message.answer(f'link for payment {payment.confirmation.confirmation_url}')










