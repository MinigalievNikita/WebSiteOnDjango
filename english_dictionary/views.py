"""
Framework for better connection to html files
"""
from django.shortcuts import render
from django.core.cache import cache
from . import definitions_work


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def guide(request):
    return render(request, "guide.html")


def words_list(request):
    definitions = definitions_work.get_definitions_for_table()
    return render(request, "words_list.html", context={"definitions": definitions})


def add_word(request):
    return render(request, "add_word.html")


def sphere_choose(request):
    # word, definition = definitions_work.utility.get_definition_for_game()
    # word_definition = {"word": word, "definition": definition}
    # return render(request, "word_check.html", context={"word_definition": word_definition})
    return render(request, "sphere_choose.html")


def word_check(request):
    if request.method == "POST":
        cache.clear()
        chosen_sphere = request.POST.get("chosen_sphere")
        word, definition = definitions_work.utility.get_definition_in_sphere_for_game(chosen_sphere)
        word_definition = {"word": word, "definition": definition}
        return render(request, "word_check.html", context={"word_definition": word_definition})
    return sphere_choose(request)


def send_definition(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        email = request.POST.get("email", "")
        new_word = request.POST.get("new_word", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        new_translation = request.POST.get("new_translation", "").replace(";", ",")
        sphere = request.POST.get("sphere", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Слово должно быть не пустым"
        elif len(new_translation) == 0:
            context["success"] = False
            context["comment"] = "Слово должно быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            definitions_work.write_definition(new_word, new_definition, new_translation, sphere, user_name)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "definition_request.html", context)
    return add_word(request)


def word_answer(request):
    if request.method == "POST":
        cache.clear()
        answer = request.POST.get("answer")
        context = {"user": answer}
        if len(answer) == 0:
            context["success"] = False
            context["comment"] = "Слово должно быть не пустым"
            return render(request, "word_request.html", context)
        context["success"] = True
        context["comment"] = "Ваше ответ принятя"
        result = definitions_work.utility.answer_check(answer)
        context["success"] = result
        context["comment"] = answer
        return render(request, "word_answer.html", context)
    return word_check(request)
