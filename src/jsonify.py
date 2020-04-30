
def wine_jsonify(wine):
    return {
        'country': wine.country,
        'description': wine.description,
        'designation': wine.designation,
        'points': wine.points,
        'price': wine.price,
        'province': wine.province,
        'region_1': wine.region_1,
        'region_2': wine.region_2,
        'taster_name': wine.taster_name,
        'taster_twitter_handle': wine.taster_twitter_handle,
        'title': wine.title,
        'variety': wine.variety,
        'winery': wine.winery
    }
