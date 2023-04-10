from flask import Blueprint, request,jsonify,Flask

from .data.search_data import USERS

app = Flask(__name__)

bp = Blueprint("search", __name__, url_prefix="/search/")


@bp.route("")
def search():

    return search_users(request.args.to_dict()), 200
def search_users(args):
    # first of all sorry for grammatical english error i made in comments 
    # i declare variable s_p , sp stand for search parameters and i request arguments to the dictionary
    s_p = request.args.to_dict()
    # i declare empty list to append
    final = []

    if s_p:
        # i condition id if is in s_p and if there i declare id_val to index s_p by the string id
        # i use next function to iterate 1 by one and finally append user_with_id in final list
        if 'id' in s_p:
            id_val = s_p['id']
            user_with_id = next((user for user in USERS if user['id'] == id_val), None)
            if user_with_id:
                final.append(user_with_id)
        # same as situation on the name i index name string in lower case so that like in the given instruction in typing doe name
        if 'name' in s_p:
            name_val = s_p['name'].lower()
            for user in USERS:
                if 'name' in user and name_val in user['name'].lower():
                    if user not in final:
                        final.append(user)
        # i condition age in USERS if >= to age_val and same as user <= + 1
        if 'age' in s_p:
            age_val = int(s_p['age'])
            for user in USERS:
                if 'age' in user and user['age'] >= age_val - 1 and user['age'] <= age_val + 1:
                    if user not in final:
                        final.append(user)
        if 'occupation' in s_p:
            occupation_val = s_p['occupation'].lower()
            for user in USERS:
                if 'occupation' in user and occupation_val in user['occupation'].lower():
                    if user not in final:
                        final.append(user)
        # returning all the possible outcome of the condition
        return final
    else:
        # else for search
        return USERS

