import operator
from django.shortcuts import render
from django.http import HttpResponse
from .models import RecipeList, RecipeIngredient, RecipeContent2, IngredientList
from django.db.models import Q
import itertools



# Create your views here.
def search_recipes_form(request):


    ingredients_name_list = IngredientList.objects.all()

    #print ingredients_name_list

    for i in ingredients_name_list:
        print i.ingredient_name
    
    return render(request, 'search_form.html',
        {'ingredients_name_list': ingredients_name_list
        })

def search_recipes(request):
    search_list = []
    search_list_temp = []
    checks_list = []
    split_q_nonull = []
    split_q_nonull2 = []
    delete_list = []
    other_list = []
    q2=""

    ingredients_name_list = IngredientList.objects.all()


    if request.method == 'GET':
        if request.GET.getlist('checks[]'):
            checks_list = request.GET.getlist('checks[]')
            search_list_temp.extend(checks_list)

        if request.GET.getlist('other'):

            other_list = request.GET.getlist('other')
            search_list_temp.extend(other_list)

            print "====== other_list ======"
            print other_list

        if request.GET.getlist('add'):

            add_list = request.GET.getlist('add')
            search_list_temp.extend(add_list)

            print "====== add_list ======"
            print add_list

    
        """if 'q' in request.GET:
            q = request.GET['q']
            q_encode=q.encode('utf8')
            split_q = q_encode.split(",")
            split_q_nonull = [x for x in split_q if x]
            search_list_temp.extend(split_q_nonull)

            print "====== Q ======"
            print q"""

        if 'q2' in request.GET:
            q2 = request.GET['q2']
            q_encode2=q2.encode('utf8')
            split_q2 = q_encode2.split(",")
            split_q_nonull2 = [x for x in split_q2 if x]
            search_list_temp.extend(split_q_nonull2)
            
            
            print "**** Q2 ****"
            print q2

        if 'delete' in request.GET:
            delete_list = request.GET.getlist('delete')

            print "-- DEL LIST --"
            print delete_list

            #for d in delete_list:
             #   search_list.remove(d)
            
        
    for s in search_list_temp:
        search_list.append(s.lower())

    print "-- search_list -- "
    print search_list

    recipe_ingredients_table = RecipeIngredient.objects.filter(reduce(lambda x, y: x | y, [Q(ingredient__contains=word) for word in search_list]))
        
    recipe_list = []
    for r in recipe_ingredients_table:
        recipe_list.append(r.recipe_name)
        
    recipe_list_unique = list(set(recipe_list))
    recipe_name_table = RecipeList.objects.filter(reduce(lambda x, y: x | y, [Q(recipe_name__iexact=word) for word in recipe_list_unique]))

    ######### RANKING RECIPES ######################
    recipe_content = RecipeContent2.objects.filter(reduce(lambda x, y: x | y, [Q(recipe_name__iexact=word) for word in recipe_list_unique]))


    search_set = set(search_list)

    print " == SEARCH SET =="
    print search_set

    s_len = len(search_set)

    rank_dic = {}
    #for i in xrange(s_len, 0, -1):
    for i in range(1, s_len+1):
        subsets = set(itertools.combinations(search_set, i))
        for x in subsets:
            recipe_content_rankwise = recipe_content.filter(reduce(lambda x, y: x | y, [Q(content__contains=word) for word in x]))
            qs = recipe_content.filter(reduce(operator.and_, (Q(content__contains=word) for word in x)))

            for temp in qs:
                rank_dic[temp.recipe_name] = i
                
    #print "--- RANK DICTIONARY --"
    sorted_rank_dic = sorted(rank_dic.items(), key=operator.itemgetter(1), reverse=True)
    #print sorted_rank_dic
    ######### END RANKING RECIPES ######################

    ##########################################################
    # Meal type - main, entree, soups, desserts, congee, etc
    recipe_name_mealtype_table = []
    meal_type = []
    meal_type_list = []
    if request.GET.getlist('meal_type'):
            
        meal_type = request.GET.getlist('meal_type')
           
        if meal_type[0] == "Desserts":
            meal_type_list.append("dessert")
        elif meal_type[0] == "Soups":
            meal_type_list.append("soup")
        elif meal_type[0] == "Congee":
            meal_type_list.append("congee")
        elif meal_type[0] == "Entree + Main":
            meal_type_list.append("entree")
            meal_type_list.append("main")
        elif meal_type[0] == "All":
            meal_type_list.append("entree")
            meal_type_list.append("soup")
            meal_type_list.append("congee")
            meal_type_list.append("main")
            meal_type_list.append("dessert")
            meal_type_list.append("")

            #recipe_name_mealtype_table = recipe_name_table.filter(reduce(lambda x, y: x | y, [Q(category__iexact=word) for word in meal_type_list]))
    else:
        meal_type_list.append("entree")
        meal_type_list.append("soup")
        meal_type_list.append("congee")
        meal_type_list.append("main")
        meal_type_list.append("dessert")
        meal_type_list.append("")

            
    recipe_name_mealtype_table = recipe_name_table.filter(reduce(lambda x, y: x | y, [Q(category__iexact=word) for word in meal_type_list]))


    ##########################################################
    # Cuisine type - Australian, Chinese, Indian, etc
    recipe_name_cuisinetype_table = []
    cuisine_type = []
    cuisine_type_list = []
    if request.GET.getlist('cuisine_type'):
            
        cuisine_type = request.GET.getlist('cuisine_type')
           
        if cuisine_type[0] == "Australian":
            cuisine_type_list.append("Australian")
        elif cuisine_type[0] == "Chinese":
            cuisine_type_list.append("Chinese")
        elif cuisine_type[0] == "Indian":
            cuisine_type_list.append("Indian")
        elif cuisine_type[0] == "All":
            cuisine_type_list.append("Australian")
            cuisine_type_list.append("Chinese")
            cuisine_type_list.append("Indian")
          
        #recipe_name_cuisinetype_table = recipe_name_mealtype_table.filter(reduce(lambda x, y: x | y, [Q(recipe_type__iexact=word) for word in cuisine_type_list]))

    else:
        cuisine_type_list.append("Australian")
        cuisine_type_list.append("Chinese")
        cuisine_type_list.append("Indian")

            
    recipe_name_cuisinetype_table = recipe_name_mealtype_table.filter(reduce(lambda x, y: x | y, [Q(recipe_type__iexact=word) for word in cuisine_type_list]))

    # Flavour type - Mixed, Spicy & Flavor, Thick & Creamy etc
    recipe_name_tastetype_table = []
    taste_type = []
    taste_type_list = []
    if request.GET.getlist('taste[]'):
        taste_type = request.GET.getlist('taste[]')
        print "*********"
        print taste_type

        if "spicy&hot" in taste_type:
            taste_type_list.append("spicy&hot")
        elif "thick&creamy" in taste_type:
            taste_type_list.append("thick&creamy")
        elif "light&refresh" in taste_type:
            taste_type_list.append("light&refresh")
        elif "crispy&crunchy" in taste_type:
            taste_type_list.append("crispy&crunchy")
        elif "mixed" in taste_type:
            taste_type_list.append("spicy&hot")
            taste_type_list.append("thick&creamy")
            taste_type_list.append("light&refresh")
            taste_type_list.append("")

    recipe_name_tastetype_table = recipe_name_cuisinetype_table.filter(reduce(lambda x, y: x | y, [Q(taste__iexact=word) for word in taste_type_list]))

   
    #CATEGORY
    main_recipes_table = recipe_name_tastetype_table.filter(category__iexact="main")
    entree_recipes_table = recipe_name_tastetype_table.filter(category__iexact="entree")
    dessert_recipes_table = recipe_name_tastetype_table.filter(category__iexact="dessert")
    soup_recipes_table = recipe_name_tastetype_table.filter(category__iexact="soup")
    congee_recipes_table = recipe_name_tastetype_table.filter(category__iexact="congee")

    
    main_rank_dictionary = {}
    for m in main_recipes_table:
        recp =  m.recipe_name
        if(recp in rank_dic.keys()):
            main_rank_dictionary[recp] = rank_dic[recp]

    sorted_main_rank_dic = sorted(main_rank_dictionary.items(), key=operator.itemgetter(1), reverse=True)
   
    entree_rank_dictionary = {}
    for m in entree_recipes_table:
        recp =  m.recipe_name
        if(recp in rank_dic.keys()):
            entree_rank_dictionary[recp] = rank_dic[recp]

    sorted_entree_rank_dic = sorted(entree_rank_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    dessert_rank_dictionary = {}
    for m in dessert_recipes_table:
        recp =  m.recipe_name
        if(recp in rank_dic.keys()):
            dessert_rank_dictionary[recp] = rank_dic[recp]

    sorted_dessert_rank_dic = sorted(dessert_rank_dictionary.items(), key=operator.itemgetter(1), reverse=True)


    soup_rank_dictionary = {}
    for m in soup_recipes_table:
        recp =  m.recipe_name
        if(recp in rank_dic.keys()):
            soup_rank_dictionary[recp] = rank_dic[recp]

    sorted_soup_rank_dic = sorted(soup_rank_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    congee_rank_dictionary = {}
    for m in congee_recipes_table:
        recp =  m.recipe_name
        if(recp in rank_dic.keys()):
            congee_rank_dictionary[recp] = rank_dic[recp]

    sorted_congee_rank_dic = sorted(congee_rank_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'search_results.html',
            {'ingredients_name_list': ingredients_name_list,
            'checks_list': checks_list,
            'recipe_name_table': recipe_name_table,
            'recipe_name_tastetype_table': recipe_name_tastetype_table,
            'meal_type': meal_type,
            'cuisine_type': cuisine_type,
            'taste_type': taste_type,
            'q2': q2,
            'search_set':search_set,
            'delete_list':delete_list,
            'other_list':other_list,
            'sorted_main_rank_dic':sorted_main_rank_dic,
            'sorted_entree_rank_dic':sorted_entree_rank_dic,
            'sorted_dessert_rank_dic':sorted_dessert_rank_dic,
            'sorted_soup_rank_dic':sorted_soup_rank_dic,
            'sorted_congee_rank_dic':sorted_congee_rank_dic
            })
        
    #message = 'Hello Anushi'
    #return HttpResponse(message)



def search_recipes_copy(request):
    #if 'q' in request.GET:
     #   message = 'You searched for: %r' % request.GET['q']
    #else:
     #   message = 'You submitted an empty form.'
    #return HttpResponse(message)
    request_temp = request

    message = "Hello"
    if request.method == 'GET':
        message = 'Welcome'
        search_list = []
        taste_search_list = []
        checks_list = []
        if request.GET.getlist('checks[]'):
            checks_list = request.GET.getlist('checks[]')
            search_list.extend(checks_list)

        print "#############################"
        print checks_list

        if request.GET['q']:
            q = request.GET['q']
            q_encode=q.encode('utf8')
            split_q = q_encode.split(",")
            split_q_nonull = [x for x in split_q if x]
            search_list.extend(split_q_nonull)

        


        if request.GET.getlist('taste[]'):
            print "**** TASTE *****"
            taste_list = request.GET.getlist('taste[]')
            taste_search_list.extend(taste_list)

            if "" in taste_search_list: 
                
                if 'spicy&hot' not in taste_search_list:
                    taste_search_list.append('spicy&hot')
                
                if 'thick&creamy' not in taste_search_list:   
                    taste_search_list.append('thick&creamy')

                if 'light&refresh' not in taste_search_list:
                    taste_search_list.append('light&refresh')

                if 'crispy&crunchy' not in taste_search_list:
                    taste_search_list.append('crispy&crunchy')

        print taste_search_list
        print "---------------------------"
        
        recipe_ingredients_table = RecipeIngredient.objects.filter(reduce(lambda x, y: x | y, [Q(ingredient__contains=word) for word in search_list]))
        
        recipe_list = []
        for r in recipe_ingredients_table:
            recipe_list.append(r.recipe_name)
        
        recipe_list_unique = list(set(recipe_list))
        
       
        recipe_name_table = RecipeList.objects.filter(reduce(lambda x, y: x | y, [Q(recipe_name__iexact=word) for word in recipe_list_unique]))
        
        #TASTE
        recipe_name_taste_table = recipe_name_table.filter(reduce(lambda x, y: x | y, [Q(taste__iexact=word) for word in taste_search_list]))

        #CATEGORY
        main_recipes_table = recipe_name_taste_table.filter(category__iexact="main")
        entree_recipes_table = recipe_name_taste_table.filter(category__iexact="entree")
        
        
        return render(request, 'search_results.html',
            {'main_recipes_table': main_recipes_table, 'entree_recipes_table': entree_recipes_table,'query': search_list, 'request_temp': request_temp, 'checks_list': checks_list})
        

   
def get_full_recipe(request,recipe_name_arg):
    
    
    recipe_name_list = RecipeList.objects.filter(recipe_name=recipe_name_arg)
    recipe_ingredients_list = RecipeIngredient.objects.filter(recipe_name=recipe_name_arg)
    recipe_content = RecipeContent2.objects.filter(recipe_name=recipe_name_arg)
    

    #html = "<html><body>Recipe is :  %s </body></html>" % recipe_name 
    #return HttpResponse(html)
   
    return render(request, 'get_full_recipe.html', {'recipe_name_list': recipe_name_list,'recipe_ingredients_list' : recipe_ingredients_list, 'recipe_content': recipe_content})