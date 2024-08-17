# views.py
from django.shortcuts import render

def index(request):
    # FIRST FOR
    menu_items = [
        {'name': 'Home', 'active': True},
        {'name': 'Company', 'active': False},
        {'name': 'About Sports', 'active': False},
        {'name': 'Subscription', 'active': False},
        {'name': 'Contact Us', 'active': False},
    ]
    # sec for
    activities = [
        {
            'title': 'Riding Mountain Bike',
            'description': 'Aenean cursus imperdiet nisl id fermentum. Aliquam pharetra dui laoreet vulputate dignissim. Sed id metus id quam auctor molestie eget ut augue.',
            'image': 'static/images/graph-04.svg',
            'image_width': 110,
            'image_height': None,
        },
        {
            'title': 'Volley Ball Intense Training',
            'description': 'Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat.',
            'image': 'static/images/graph-03.svg',
            'image_width': 90,
            'image_height': None,
        },
        {
            'title': 'Learn Surfing From Experts',
            'description': 'Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat.',
            'image': 'static/images/graph-02.svg',
            'image_width': None,
            'image_height': 84,
        },
        {
            'title': 'Archers Club',
            'description': 'Maecenas eu dictum felis, a dignissim nibh. Mauris rhoncus felis odio, ut volutpat massa placerat ac. Curabitur dapibus iaculis mi gravida luctus. Aliquam erat volutpat.',
            'image': 'static/images/graph-01.svg',
            'image_width': None,
            'image_height': 71,
        },
    ]
    # THIRD FOR
    testimonials = [
        {
            'image': 'static/images/logo-1.png',
            'image_height': 84,
            'image_width': 124,
            'text': 'Sed vestibulum scelerisque urna, eu finibus leo facilisis sit amet. Proin id dignissim magna. Sed varius urna et pulvinar venenatis.'
        },
        {
            'image': 'static/images/logo-2.png',
            'image_height': 90,
            'image_width': 148,
            'text': 'Donec euismod dolor ut ultricies consequat. Vivamus urna ipsum, rhoncus molestie neque ac, mollis eleifend nibh.'
        },
        {
            'image': 'static/images/logo-3.png',
            'image_height': 100,
            'image_width': 100,
            'text': 'In efficitur in velit et tempus. Duis nec odio dapibus, suscipit erat fringilla, imperdiet nibh. Morbi tempus auctor felis ac vehicula.'
        },
        {
            'image': 'static/images/logo-4.png',
            'image_height': 50,
            'image_width': 108,
            'text': 'Fusce pharetra erat id odio blandit, nec pharetra eros venenatis. Pellentesque porttitor cursus massa et vestibulum.'
        }
    ]
    # FOURTH FOR
    pricing_plans = [
        {
            'name': 'Students',
            'price': 8,
            'features': ['Personal License'],
        },
        {
            'name': 'Professional',
            'price': 19,
            'features': ['Professional License', 'Email Support'],
        },
        {
            'name': 'Agency',
            'price': 49,
            'features': ['1-12 Team Members', 'Phone Support'],
            'recommended': True,
        },
        {
            'name': 'Enterprise',
            'price': 79,
            'features': ['Unlimited Team Members', '24/7 Phone Support'],
        }
    ]



    return render(request, 'index.html', {'menu_items': menu_items,'activities': activities,'testimonials':testimonials,'pricing_plans':pricing_plans})
