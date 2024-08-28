# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
# from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
# from database.queryset import * 


# menu_kb = ReplyKeyboardMarkup(
#     keyboard =[
#       [KeyboardButton(text='Category')], [KeyboardButton(text = 'All games')]], resize_keyboard=True, input_field_placeholder='Choose button', one_time_keyboard=True
# )


# # inline_test = InlineKeyboardMarkup(
# #     inline_keyboard= [
# #         [InlineKeyboardButton(text = 'I want eat', callback_data='button1')],
# #         [InlineKeyboardButton(text = 'I want eooat', callback_data='button2')],
# #         [InlineKeyboardButton(text = 'I want ekkat', callback_data='button3')]

# #     ])


# async def categorues_kb():
#     builder = InlineKeyboardBuilder()
#     categories = await get_category()
#     for category in categories:
#         builder.add(InlineKeyboardButton(
#             text = category.name,
#             callback_data= f'category_{category.id}'
#         ))
#     return builder.adjust(2).as_markup()






# async def categorues_kb2():
#     builder = InlineKeyboardBuilder()
#     categories = await get_category()
#     for category in categories:
#         builder.add(InlineKeyboardButton(
#             text = category.name,
#             callback_data= f'category2_{category.id}'
#         ))
#     return builder.adjust(2).as_markup()
















# async def games_kb():
#     builder = InlineKeyboardBuilder()
#     games = await get_games()
#     for game in games:
#         builder.add(InlineKeyboardButton(
#             text = game.name,
#             callback_data= f'game_{game.id}'
#         ))
#     return builder.adjust(2).as_markup()




# async def game_kb(category_id):
#     builder = InlineKeyboardBuilder()
#     games = await get_game(category_id)
#     for game in games:
#         builder.add(InlineKeyboardButton(
#             text = game.name,
#             callback_data= f'game_{game.id}'
#         ))
#     return builder.adjust(2).as_markup()

# async def game_key_kb(game_id):
#     builder = InlineKeyboardBuilder()
#     game = await get_game_key(game_id)
#     builder.add(InlineKeyboardButton(
#         text = f'Купить ключ к игре {game.count} - {game.price}$',
#         callback_data = f'game_key_{game.id}'
#     ))
#     return builder.adjust(1).as_markup()



# from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
#                            KeyboardButton, ReplyKeyboardMarkup)
# from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
# from database.queryset import *




# menu_kb = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Категории')],[KeyboardButton(text ='Все игры')]
# ],resize_keyboard=True,input_field_placeholder='Выберите пункт меню',
#                               one_time_keyboard=True)

# # inline_test = InlineKeyboardMarkup(inline_keyboard=[
# #     [InlineKeyboardButton(text='Аркада',callback_data='button1')],
# #     [InlineKeyboardButton(text='Шутер',callback_data='button2')],
# #     [InlineKeyboardButton(text='Аркада',callback_data='button3')]
    
# # ])


# async def categories_kb():
#     builder = InlineKeyboardBuilder()
#     categories = await get_categories()
#     for category in categories:
#         builder.add(InlineKeyboardButton(
#             text = category.name,
#             callback_data= f'category_{category.id}' #== 'category_1'
#         ))
#     return builder.adjust(2).as_markup()

# async def categories_kb2():
#     builder = InlineKeyboardBuilder()
#     categories = await get_categories()
#     for category in categories:
#         builder.add(InlineKeyboardButton(
#             text = category.name,
#             callback_data= f'category2_{category.id}' #== 'category2_1'
#         ))
#     return builder.adjust(2).as_markup()

# async def games_kb(category_id):
#     builder = InlineKeyboardBuilder()
#     games = await get_games(category_id)
#     for game in games:
#         builder.add(InlineKeyboardButton(
#             text = game.name,
#             callback_data= f'game_{game.id}' #== 'game_1'
#         ))
#     builder.add(InlineKeyboardButton(
#         text = 'Back to categories',
#         callback_data= 'back_to_caregories'
#     ))
#     return builder.adjust(2).as_markup
    




# async def back_to_categories_kb():
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text = 'Back',
#         callback_data='back_to_categories'
#     ))

#     return builder.adjust(1).as_markup



from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from database.queryset import *

menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Categories')],[KeyboardButton(text ='All games')]
],resize_keyboard=True,input_field_placeholder='Выберите пункт меню',
                              one_time_keyboard=True)

# inline_test = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Аркада',callback_data='button1')],
#     [InlineKeyboardButton(text='Шутер',callback_data='button2')],
#     [InlineKeyboardButton(text='Аркада',callback_data='button3')]
    
# ])



async def categories_kb():
    builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        builder.add(InlineKeyboardButton(
            text = category.name,
            callback_data= f'category_{category.id}' #== 'category_1'
        ))
    return builder.adjust(2).as_markup()

async def categories_kb2():
    builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        builder.add(InlineKeyboardButton(
            text = category.name,
            callback_data= f'category2_{category.id}' #== 'category2_1'
        ))
    return builder.adjust(2).as_markup()


async def categories_kb3():
    builder = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        builder.add(InlineKeyboardButton(
            text = category.name,
            callback_data= f'category3_{category.id}' #== 'category2_1'
        ))
    return builder.adjust(2).as_markup()



# PAGE_SIZE = 2
# async def games_kb(category_id, page):
#     offset = (page - 1) * PAGE_SIZE
#     builder = InlineKeyboardBuilder()
#     all_game = await get_games(category_id, offset=offset, limit = PAGE_SIZE)
#     for game in all_game:
#         builder.add(InlineKeyboardButton(
#             text = game.name,
#             callback_data=f'game_{game.id}'

#         ))

#     if page > 1:
#         builder.add(InlineKeyboardButton(
#         text = '<<',
#         callback_data= f'page_{category_id}_{page-1}'
#         ))

#     if len(all_game) == PAGE_SIZE:
#         builder.add(InlineKeyboardBuilder(
#             text = '>>',
#             callback_data = f'page_{category_id}_{page+1}'
#         ))

    

#     return builder.adjust(2).as_markup()


PAGE_SIZE = 2
async def games_kb(category_id,page):
    offset = (page - 1) * PAGE_SIZE
    builder = InlineKeyboardBuilder()
    all_games = await get_games(category_id,offset=offset,limit=PAGE_SIZE)
    for game in all_games:
        builder.add(InlineKeyboardButton(
            text = game.name,
            callback_data = f'game_{game.id}'
        ))
    if page > 1:
        builder.add(InlineKeyboardButton(
            text = '<<',
            callback_data= f'page_{category_id}_{page-1}'
        ))
    if len(all_games) == PAGE_SIZE:
        builder.add(InlineKeyboardButton(
            text = '>>',
            callback_data=f'page_{category_id}_{page+1}'
        ))
        
    return builder.adjust(2).as_markup()
    
    



PAGE_SIZE = 2
async def games_kb_paginate(category_id,page):
    offset = (page - 1) * PAGE_SIZE
    builder = InlineKeyboardBuilder()
    all_games_paginate = await get_games(category_id,offset=offset,limit=PAGE_SIZE)
    for game in all_games_paginate:
        builder.add(InlineKeyboardButton(
            text = game.name,
            callback_data = f'all_game_{game.id}'
        ))
    if page > 1:
        builder.add(InlineKeyboardButton(
            text = '<<',
            callback_data= f'all_page_{page-1}'
        ))
    if len(all_games_paginate) == PAGE_SIZE:
        builder.add(InlineKeyboardButton(
            text = '>>',
            callback_data=f'all_page_{page+1}'
        ))
        
    return builder.adjust(2).as_markup()


    
    


    # builder = InlineKeyboardBuilder()
    # games = await get_games(category_id)
    # for game in games:
    #     builder.add(InlineKeyboardButton(
    #         text = game.name,
    #         callback_data= f'game_{game.id}' #== 'game_1'
    #     ))
    # builder.add(InlineKeyboardButton(
    #     text = 'Назад к категориям',
    #     callback_data= 'back_to_categories' 
    # ))
    # return builder.adjust(2).as_markup()
 



# async def game_delete_kb(game_id):
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text = 'Delete',
#         callback_data=f'delete_{game_id}'
#     ))
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text = 'Назад к категории',
#         callback_data= 'back_to_categories'
#     ))
#     builder.add(InlineKeyboardButton(
#         text = 'Купить',
#         callback_data= f'buy_game'
#     ))
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text = 'Delete',
#         callback_data=f'delete_{game_id}'
#     ))
#     return builder.adjust(2).as_markup()



    

# async def back_to_categories_kb():
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text = 'Назад',
#         callback_data= 'back_to_categories' 
#     ))
#     return builder.adjust(1).as_markup()




# async def back_to_categories_kb(game_id):
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text = 'Назад к категории',
#         callback_data= 'back_to_categories'
#     ))
#     builder.add(InlineKeyboardButton(
#         text = 'Удалить игру',
#         callback_data= f'delete_{game_id}'
#     ))
#     builder.add(InlineKeyboardButton(
#         text = 'Купить',
#         callback_data= f'buy_game'
#     ))
#     return builder.adjust(2).as_markup()



# async def del_game_kb():
#     builder = InlineKeyboardBuilder()
#     builder.add(InlineKeyboardButton(
#         text = 'Удалить игру',
#         callback_data= 'back_to_game' 
#     ))
#     return builder.adjust(1).as_markup()


async def back_to_categories_kb(game_id):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text = 'Назад к категории',
        callback_data= 'back_to_categories'
    ))
    builder.add(InlineKeyboardButton(
        text = 'Удалить игру',
        callback_data= f'delete_{game_id}'
    ))
    builder.add(InlineKeyboardButton(
        text = 'Купить',
        callback_data= f'buy_game_{game_id}'
    ))
    return builder.adjust(2).as_markup()

