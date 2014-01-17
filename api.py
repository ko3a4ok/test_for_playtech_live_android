__author__ = 'ko3a4ok'
import webapp2
import json
from random import choice, sample

M = 'male'
F = 'female'
C = 'child'
TYPE = 'type'
NAME = 'name'
CAR = 'car'
CHILDREN = 'children'
CHILDREN_COUNT = 'childrenCount'
FATHER = 'father'
MOTHER = 'mother'
COLOR = "color_bg"
male_names = ['Mr. Misha', 'Mr. Grisha', 'Mr. Tolya', 'Mr. Opanas', 'Mr. Dron']
child_names = ['Johnny Cage', 'Kano', 'Lui Kang', 'Raiden', 'Reptile', 'Scorpion', 'Shang Tsung', 'Sonya Blade', 'Sub-Zero']
female_names = ['Ms. Lyusya', 'Ms. Dusya', 'Ms. Zyuzya', 'Ms. Masha', 'Ms. Dasha', 'Ms. Pasha', 'Ms. rUSHA']
colors = ['#aaaabb', '#cc00aa', '#ffaaaa', '#aaaaff', '#aaffaa']
cars = ['Infinity', 'Zhiguli', 'Parovoz', 'Bebently', 'Ololopel', 'KamaZ']




class ApiHandler(webapp2.RequestHandler):

    def gen_child(self):
        return {
            TYPE: C,
            NAME: choice(child_names),
            FATHER: choice(male_names),
            MOTHER: choice(female_names)
        }

    def gen_male(self):
        return {
            TYPE: M,
            NAME: choice(male_names),
            CAR: choice(cars),
            CHILDREN_COUNT: choice([1, 2, 3, 4, 5])
        }

    def gen_female(self):
        return {
            TYPE: F,
            NAME: choice(female_names),
            CHILDREN: sample(child_names, choice([1, 2, 3, 4, 5]))
        }


    def api_response(self):
        types = self.request.get('types');

        support_type = types.split('|');
        support_type = list(set([M, F, C]).intersection(support_type));
        if not support_type: return [];
        creator = {M : self.gen_male, F : self.gen_female, C : self.gen_child}
        result = [];
        for i in range(0, 50) :
            r = creator[choice(support_type)]()
            r[COLOR] = choice(colors)
            result.append(r);

        return json.dumps(result, indent=4)

    def get(self):
        self.response.write(self.api_response());
