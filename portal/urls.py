from django.urls import path
from . import views

app_name = "portal"

urlpatterns = [

    # ==============================
    # 🔐 AUTHENTICATION
    # ==============================
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),

    # ==============================
    # 🌐 LANGUAGE & CROPS
    # ==============================
    path("select-language/", views.select_language, name="select_language"),
    path("select-crops/", views.select_crops, name="select_crops"),

    # ==============================
    # 🏠 HOME / DASHBOARD
    # ==============================
    path("", views.home, name="home"),

    # ==============================
    # 👤 USER
    # ==============================
    path("profile/", views.profile_view, name="profile"),
    path("settings/", views.settings_view, name="settings"),

    # ==============================
    # 🛒 MARKET & CART
    # ==============================
    path("market/", views.market, name="market"),

    # 🔥 PRODUCT DETAIL (VERY IMPORTANT)
    path("product/<int:id>/", views.product_detail, name="product_detail"),

    path("cart/", views.cart, name="cart"),
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove-from-cart/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("update-cart/<int:product_id>/", views.update_cart_quantity, name="update_cart_quantity"),

    # ==============================
    # 💳 CHECKOUT
    # ==============================
    path("checkout/", views.checkout, name="checkout"),
    path("place-order/", views.place_order, name="place_order"),
    path("order-success/<int:order_id>/", views.order_success, name="order_success"),

    # ==============================
    # 🌾 FARMING TOOLS
    # ==============================
    path("weather/", views.weather_view, name="weather"),
    path("soil-analysis/", views.soil_analysis_view, name="soil_analysis"),
    path("crop-advice/", views.crop_advice_view, name="crop_advice"),

    # ==============================
    # 🌱 SOIL DETECTOR
    # ==============================
    path("soil/", views.soil_detector, name="soil_detector"),
    path("api/soil/", views.soil_api, name="soil_api"),

    # ==============================
    # 🌿 DISEASE DETECTION
    # ==============================
    path("disease/", views.disease_detection, name="disease_detection"),
    path("detect-disease/", views.disease_detection, name="detect_disease"),
    path("disease-result/", views.disease_result, name="disease_result"),

    # ==============================
    # 🧮 FERTILIZER
    # ==============================
    path("fertilizer/", views.fertilizer_calculator, name="fertilizer_calculator"),

    # ==============================
    # 📅 CROP CALENDAR
    # ==============================
    path("calendar/", views.crop_calendar, name="crop_calendar"),
    path("calendar/calculator/", views.crop_calendar_calculator, name="crop_calendar_calculator"),
    path("calendar/delete/<int:event_id>/", views.delete_crop_event, name="delete_crop_event"),
    path("calendar/toggle/<int:event_id>/", views.toggle_event_complete, name="toggle_event_complete"),

    path("performance/", views.crop_performance, name="crop_performance"),

    # ==============================
    # 🌍 COMMUNITY
    # ==============================
    path("community/", views.community, name="community"),
    path("community/post/", views.create_post, name="create_post"),
    path("community/like/<int:post_id>/", views.like_post, name="like_post"),
    path("community/comment/<int:post_id>/", views.add_comment, name="comment"),

    # ==============================
    # 🧪 PESTICIDE
    # ==============================
    path("pesticide/", views.pesticide_home, name="pesticide_home"),
]