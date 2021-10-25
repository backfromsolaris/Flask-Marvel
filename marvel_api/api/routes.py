from flask import Blueprint, request, jsonify
from marvel_api.helpers import token_required
from marvel_api.models import db, Hero, hero_schema, heroes_schema


api = Blueprint('api', __name__, url_prefix='/api')

# test
# @api.route('/getdata')
# def getdata():
#     return {'some_value': 99999, 'another_value': 77777}


# create a hero
@api.route('/heroes', methods = ['POST'])
@token_required
def create_hero(current_user_token):
    hero_name = request.json['hero_name']
    description = request.json['description']
    comics_appeared_in = request.json['comics_appeared_in']
    super_power = request.json['super_power']
    owner_token = current_user_token.owner_token

    hero = Hero(hero_name, description, comics_appeared_in, super_power, owner_token=owner_token)

    db.session.add(hero)
    db.session.commit()

    response = hero_schema.dump(hero)
    return jsonify(response)

# retrieve all heroes
@api.route('/heroes', methods = ['GET'])
@token_required
def get_heroes(current_user_token):
    owner = current_user_token.owner_token
    heroes = Hero.query.filter_by(owner_token = owner).all()
    response = heroes_schema.dump(heroes)
    return jsonify(response)

# retrieve one hero
@api.route('/heroes/<id>')
@token_required
def get_hero(current_user_token, id):
    hero = Hero.query.get(id)
    response = hero_schema.dump(hero)
    return jsonify(response)

# update a hero's data
@api.route('/heroes/<id>', methods = ['POST'])
@token_required
def update_hero(current_user_token, id):
    hero = Hero.query.get(id)
    if hero:
        hero = Hero.query.get(id)
        hero.hero_name = request.json['hero_name']
        hero.description = request.json['description']
        hero.comics_appeared_in = request.json['comics_appeared_in']
        hero.super_power = request.json['super_power']
        hero.owner_token = current_user_token.owner_token
        db.session.commit()

        response = hero_schema.dump(hero)
        return jsonify(response)
    else:
        return jsonify({'Sorry, we do not see that hero in the database!'})

# delete hero
@api.route('/heroes/<id>', methods = ['DELETE'])
@token_required
def delete_hero(current_user_token, id):
    hero = Hero.query.get(id)
    if hero:
        db.session.delete(hero)
        db.session.commit()
        response = hero_schema.dump(hero)
        return jsonify(response)
    else:
        return jsonify({'Sorry, we do not see that hero in the database!'})