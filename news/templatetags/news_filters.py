from django import template

register = template.Library()

STRONG_WORDS = ['population', 'climate']

@register.filter()
def censor(value):

   for word in STRONG_WORDS:
       value = value.replace(word[1:], '*' * (len(word)-1))

   return value
