from django import template
from ..models import HostelReview
register = template.Library()

@register.simple_tag
def avg_review(reviews):
    hostel_avg = 0
    food_avg = 0
    locality_avg = 0
    for i in reviews:
        hostel_avg += i.hostel_rate
        food_avg += i.food_rate
        locality_avg += i.locality_rate

    hostel_avg = hostel_avg/len(reviews)
    food_avg = food_avg/len(reviews)
    locality_avg = locality_avg/len(reviews)
    print(hostel_avg, food_avg, locality_avg)
    print(((50*hostel_avg/100) + (35*food_avg/100) + (15*locality_avg/100))/2, '--------------------------------------------')
    return "{:.1f}".format(((50*hostel_avg/100) + (35*food_avg/100) + (15*locality_avg/100))/2)
