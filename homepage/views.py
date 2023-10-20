from crud.models import Product
from django.shortcuts import render
from user_registration.models import UserProfile

def about_us(request):
    return render(request, 'temp-files/about-us/index.html')


def shop(request):
    products = Product.objects.all()
    return render(request, 'temp-files/shop/index.html', {'products': products})

def blog_grid(request):
    return render(request, 'temp-files/blog-grid/index.html')


def blog_standard(request):
    return render(request, 'temp-files/blog-standard/index.html')

def blog_standard1(request):
    return render(request, 'temp-files/blog-standard/page/2/index.html')


def contact(request):
    return render(request, 'temp-files/contact/index.html')


def accessories(request):
    return render(request, 'temp-files/product-category/accessories/index.html')


def antiques(request):
    return render(request, 'temp-files/product-category/antiques/index.html')


def cars(request):
    return render(request, 'temp-files/product-category/cars/index.html')


def electronics(request):
    return render(request, 'temp-files/product-category/electronics/index.html')


def fashion(request):
    return render(request, 'temp-files/product-category/fashion/index.html')


def music(request):
    return render(request, 'temp-files/product-category/music/index.html')


def trading_card(request):
    return render(request, 'temp-files/product-category/trading-card/index.html')



def vehicles(request):
    return render(request, 'temp-files/product-category/vehicles/index.html')



def virtual_worlds(request):
    return render(request, 'temp-files/product-category/virtual_worlds/index.html')



def watches(request):
    return render(request, 'temp-files/product-category/watches/index.html')


def how_it_works(request):
    return render(request, 'temp-files/how-it-works/index.html')


def alarm_clock_1990s(request):
    return render(request, 'temp-files/product/alarm-clock-1990s/index.html')


def black_analogue_watch(request):
    return render(request, 'temp-files/product/black-analogue-watch/index.html')


def brand_new_honda_cbr_600_special_sale_2022(request):
    return render(request, 'temp-files/product/brand-new-honda-cbr-600-special-sale-2022/index.html')


def creative_fashion_ribbon_digital_sun_class_s22(request):
    return render(request, 'temp-files/product/creative-fashion-ribbon-digital-sun-class-s22/index.html')


def ford_shelby_white_car(request):
    return render(request, 'temp-files/product/ford-shelby-white-car/index.html')


def havit_hv_g61_usb_black_double_game_vibrat(request):
    return render(request, 'temp-files/product/havit_hv_g61_usb_black_double_game_vibrat/index.html')


def iphone_11_pro_max_available_for_special_sale(request):
    return render(request, 'temp-files/product/iphone-11-pro-max-available-for-special-sale/index.html')


def leather_digital_watch(request):
    return render(request, 'temp-files/product/leather-digital-watch/index.html')


def macbook_pro_2018(request):
    return render(request, 'temp-files/product/macbook-pro-2018/index.html')


def premium_1998_typewriter(request):
    return render(request, 'temp-files/product/premium-1998-typewriter/index.html')


def red_color_special_lighter_2_2_for_saleing_offer(request):
    return render(request, 'temp-files/product/red-color-special-lighter-2-2-for-saleing-offer/index.html')


def stylish_digital_airpods(request):
    return render(request, 'temp-files/product/stylish-digital-airpods/index.html')


def toyota_aigid_a_class_hatchback_2017_2021(request):
    return render(request, 'temp-files/product/toyota-aigid-a-class-hatchback-2017-2021/index.html')


def wedding_couple_ring(request):
    return render(request, 'temp-files/product/wedding-couple-ring/index.html')


def a_brand_for_a_company_is_like_for_a_person(request):
    return render(request, 'temp-files/a-brand-for-a-company-is-like-for-a-person/index.html')


def faq(request):
    return render(request, 'temp-files/faq/index.html')


def not_found(request):
    return render(request, 'temp-files/404.html')


def wishlist(request):
    return render(request, 'temp-files/wishlist/index.html')


def david_droga_still_has_faith_in_online_creative_copy_copy(request):
    return render(request, 'temp-files/david-droga-still-has-faith-in-online-creative-copy-copy/index.html')


def david_droga_still_has_faith_in_online_creative_copy(request):
    return render(request, 'temp-files/david-droga-still-has-faith-in-online-creative-copy/index.html')


def david_droga_still_has_faith_in_online_creative(request):
    return render(request, 'temp-files/david-droga-still-has-faith-in-online-creative/index.html')


def a_brand_for_a_company_is_like_for_a_person(request):
    return render(request, 'temp-files/a-brand-for-a-company-is-like-for-a-person/index.html')


def productivity_strategies_backed_by_science(request):
    return render(request, 'temp-files/10-productivity-strategies-backed-by-science/index.html')


def lost_password(request):
    return render(request, 'temp-files/register/lost-password/index.html')


def home(request):
    vendors = UserProfile.objects.filter(role='vendor')
    products = Product.objects.all()
    return render(request, 'temp-files/homepage/index.html', {'vendors': vendors, 'products': products})


def store_listing(request):
    vendors = UserProfile.objects.filter(role='vendor')
    vendor_count = vendors.count()
    return render(request, 'temp-files/store-listing/index.html', {'vendors': vendors, 'vendor_count': vendor_count})