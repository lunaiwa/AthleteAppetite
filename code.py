from flask import Flask, render_template, request

import requests
app = Flask(__name__)

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "<YOUR_RAPID_API_KEY>",
  }

random_joke = "food/jokes/random"
find = "recipes/findByIngredients"
randomFind = "recipes/random"

@app.route('/')
def search_page():
  joke_response = str(requests.request("GET", url + random_joke, headers=headers).json()['text'])
  return render_template('search.html', joke=joke_response)

if __name__ == '__main__':
  app.run()
  
@app.route('/recipes')
def get_recipes():
  if (str(request.args['ingridients']).strip() != ""):
      # If there is a list of ingridients -> list
      querystring = {"number":"5","ranking":"1","ignorePantry":"false","ingredients":request.args['ingridients']}
      response = requests.request("GET", url + find, headers=headers, params=querystring).json()
      return render_template('recipes.html', recipes=response)
  else:
      # Random recipes
      querystring = {"number":"5"}
      response = requests.request("GET", url + randomFind, headers=headers, params=querystring).json()
      print(response)
      return render_template('recipes.html', recipes=response['recipes'])
    
    
{% extends 'base.html' %}
{% block title %} Recipes searcher {% endblock %}
{% block body %}
<h2 style="text-align: center"> <a href="/" style="text-decoration: none; color:red"> Recipes for you: </a></h2>
<div style="margin-left:35%;">
  <ul class="list-unstyled">
      {% for recipe in recipes %}
          <li class="media">
              <img src="{{recipe['image']}}" class="align-self-center mr-3" alt="..." width="15%" height="15%">
              <div class="media-body">
                  <h5 class="mt-0 mb-1"><a href="/recipe?id={{ recipe['id'] }}">{{ recipe['title'] }}</a></h5>
                  {% if 'likes' not in recipe%}
                      How many minutes for preparation? {{recipe['preparationMinutes']}} <br>
                      How many minutes for cooking? {{recipe['cookingMinutes']}}  <br>
                      How many likes has this recipe? {{recipe['aggregateLikes']}}  <br>
                  {% else %}
                      How many your ingridients? {{recipe['usedIngredientCount']}} <br>
                      How many missed ingridients? {{recipe['missedIngredientCount']}}  <br>
                      How many likes has this recipe? {{recipe['likes']}}  <br>
                  {% endif %}
              </div>
          </li> <br>
      {% endfor %}
  </ul>
</div >
{% endblock %}


@app.route('/recipe')
def get_recipe():
  recipe_id = request.args['id']
  recipe_info_endpoint = "recipes/{0}/information".format(recipe_id)
  ingedientsWidget = "recipes/{0}/ingredientWidget".format(recipe_id)
  equipmentWidget = "recipes/{0}/equipmentWidget".format(recipe_id)

  recipe_info = requests.request("GET", url + recipe_info_endpoint, headers=headers).json()
    
  recipe_headers = {
      'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
      'x-rapidapi-key': "3ed9e61dfbmshf4204c64a95df10p1b411bjsn032842b8e1d4",
      'accept': "text/html"
  }
  querystring = {"defaultCss":"true", "showBacklink":"false"}

  recipe_info['inregdientsWidget'] = requests.request("GET", url + ingedientsWidget, headers=recipe_headers, params=querystring).text
  recipe_info['equipmentWidget'] = requests.request("GET", url + equipmentWidget, headers=recipe_headers, params=querystring).text
    
  return render_template('recipe.html', recipe=recipe_info)

{% extends 'base.html' %}
{% block title %} {{recipe['title']}} {% endblock %}
{% block body %}

