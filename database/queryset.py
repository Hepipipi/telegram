# from .models import * 

# from sqlalchemy import select,delete,update,insert,join

# async def get_category():
#     async with async_session() as session:
#         result = await session.scalars(select(Category))
#         return result 
    



# async def get_games():
#     async with async_session() as session:
#         result1 = await session.scalars(select(Game))
#         return result1 
    


# async def get_game(category_id):
#     async with async_session() as session:
#         result2 = await session.scalars(select(Game).where(
#             Game.category_id == category_id))
        
#         return result2 
    
    
# async def get_game1(game_id):
#     async with async_session() as session:
#         result3 = await session.scalar(select(Game).where(
#             Game.id == game_id))
        
#         return result3
        


# async def get_price(game_id):
#     async with async_session() as session:
#         result2 = await session.scalars(select(Game).where(
#             Game.key_id == game_id))
        
#         return result2 


# async def get_game_key(game_id):
#     async with async_session() as session:
#        result = await session.scalar(select(GameKey).where(
#            GameKey.id == game_id))
#        return result
    

# async def add_category_name(category_name):
#     async with async_session() as session:
#         category = Category(name=category_name)
#         session.add(category)
#         await session.commit()
#         await session.refresh(category)
#         return category
    

# async def add_key_db(key):
#     async with async_session() as session:
#         session.add(key)
#         await session.commit()
#         await session.refresh(key)
#         return key
    

from .models import *

from sqlalchemy import select,delete,update

async def get_categories():
    async with async_session() as session:
       result = await session.scalars(select(Category))
       return result

# async def get_games(category_id, offset, limit):
#     async with async_session() as session:
#        result = await session.scalars(select(Game).where(
#            Game.category_id == category_id).offset(offset).limit(limit))
#        return result.all()


async def get_all_games(game_id, offset,limit):
    async with async_session() as session:
       result = await session.scalars(select(Game).where(
           Game.game_id == game_id).offset(offset).limit(limit))
       
       return result.all()
    






async def get_games(category_id,offset,limit):
    async with async_session() as session:
       result = await session.scalars(select(Game).where(
           Game.category_id == category_id).offset(offset).limit(limit))
       
       return result.all()


async def get_game(game_id):
    async with async_session() as session:
       result = await session.scalar(select(Game).where(
           Game.id == game_id))
       return result

async def add_category_name(category_name):
    async with async_session() as session:
        category = Category(name=category_name)
        session.add(category)
        await session.commit()
        await session.refresh(category)
        return category
    
async def add_game_db(game):
    async with async_session() as session:
        
        session.add(game)
        await session.commit()
        await session.refresh(game)
        return game
    

async def delete_categories(category_id):
    async with async_session() as session:
        await session.execute(delete(Category).where(
        Category.id == category_id))
        await session.commit()
    

    


async def delete_game(game_id):
    async with async_session() as session:
        await session.execute(delete(Game).where(
        Game.id == game_id))
        await session.commit()

    
# async def get_games(category_id,offset,limit):
#     async with async_session() as session:
#        result = await session.scalars(select(Game).where(
#            Game.category_id == category_id).offset(offset).limit(limit))
       
#        return result.all()

