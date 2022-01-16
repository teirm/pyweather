"""
Data collected to test API.
"""
#pylint: disable=line-too-long

current_weather = {
    "location": {
        "name": "London",
        "region": "City of London, Greater London",
        "country": "United Kingdom",
        "lat": 51.52,
        "lon": -0.11,
        "tz_id": "Europe/London",
        "localtime_epoch": 1641867810,
        "localtime": "2022-01-11 2:23"
    },
    "current": {
        "last_updated_epoch": 1641867300,
        "last_updated": "2022-01-11 02:15",
        "temp_c": 9.0,
        "temp_f": 48.2,
        "is_day": 0,
        "condition": {
            "text": "Overcast",
            "icon": "//cdn.weatherapi.com/weather/64x64/night/122.png",
            "code": 1009
        },
        "wind_mph": 6.9,
        "wind_kph": 11.2,
        "wind_degree": 190,
        "wind_dir": "S",
        "pressure_mb": 1026.0,
        "pressure_in": 30.3,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 93,
        "cloud": 100,
        "feelslike_c": 7.4,
        "feelslike_f": 45.2,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 1.0,
        "gust_mph": 10.5,
        "gust_kph": 16.9
    }
}

forecast = {
    "location": {
        "name": "London",
        "region": "City of London, Greater London",
        "country": "United Kingdom",
        "lat": 51.52,
        "lon": -0.11,
        "tz_id": "Europe/London",
        "localtime_epoch": 1641868059,
        "localtime": "2022-01-11 2:27"
    },
    "current": {
        "last_updated_epoch": 1641867300,
        "last_updated": "2022-01-11 02:15",
        "temp_c": 9.0,
        "temp_f": 48.2,
        "is_day": 0,
        "condition": {
            "text": "Overcast",
            "icon": "//cdn.weatherapi.com/weather/64x64/night/122.png",
            "code": 1009
        },
        "wind_mph": 6.9,
        "wind_kph": 11.2,
        "wind_degree": 190,
        "wind_dir": "S",
        "pressure_mb": 1026.0,
        "pressure_in": 30.3,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 93,
        "cloud": 100,
        "feelslike_c": 7.4,
        "feelslike_f": 45.2,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 1.0,
        "gust_mph": 10.5,
        "gust_kph": 16.9
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2022-01-11",
                "date_epoch": 1641859200,
                "day": {
                    "maxtemp_c": 8.3,
                    "maxtemp_f": 46.9,
                    "mintemp_c": 6.5,
                    "mintemp_f": 43.7,
                    "avgtemp_c": 7.6,
                    "avgtemp_f": 45.6,
                    "maxwind_mph": 8.7,
                    "maxwind_kph": 14.0,
                    "totalprecip_mm": 3.7,
                    "totalprecip_in": 0.15,
                    "avgvis_km": 7.3,
                    "avgvis_miles": 4.0,
                    "avghumidity": 92.0,
                    "daily_will_it_rain": 1,
                    "daily_chance_of_rain": 92,
                    "daily_will_it_snow": 0,
                    "daily_chance_of_snow": 0,
                    "condition": {
                        "text": "Patchy rain possible",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
                        "code": 1063
                    },
                    "uv": 1.0
                },
                "astro": {
                    "sunrise": "08:02 AM",
                    "sunset": "04:15 PM", "moonrise": "12:03 PM", "moonset": "01:52 AM",
                    "moon_phase": "First Quarter",
                    "moon_illumination": "57"
                },
            },
            {
                "date": "2022-01-12",
                "date_epoch": 1641945600,
                "day": {
                    "maxtemp_c": 9.8,
                    "maxtemp_f": 49.6,
                    "mintemp_c": 2.8,
                    "mintemp_f": 37.0,
                    "avgtemp_c": 5.6,
                    "avgtemp_f": 42.1,
                    "maxwind_mph": 4.9,
                    "maxwind_kph": 7.9,
                    "totalprecip_mm": 0.2,
                    "totalprecip_in": 0.01,
                    "avgvis_km": 10.0,
                    "avgvis_miles": 6.0,
                    "avghumidity": 74.0,
                    "daily_will_it_rain": 1,
                    "daily_chance_of_rain": 82,
                    "daily_will_it_snow": 0,
                    "daily_chance_of_snow": 0,
                    "condition": {
                        "text": "Patchy rain possible",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
                        "code": 1063
                    },
                    "uv": 1.0
                },
                "astro": {
                    "sunrise": "08:02 AM",
                    "sunset": "04:16 PM",
                    "moonrise": "12:20 PM",
                    "moonset": "03:03 AM",
                    "moon_phase": "First Quarter",
                    "moon_illumination": "64"
                },
            },
            {
                "date": "2022-01-13",
                "date_epoch": 1642032000,
                "day": {
                    "maxtemp_c": 9.4,
                    "maxtemp_f": 48.9,
                    "mintemp_c": 3.0,
                    "mintemp_f": 37.4,
                    "avgtemp_c": 5.5,
                    "avgtemp_f": 41.8,
                    "maxwind_mph": 2.5,
                    "maxwind_kph": 4.0,
                    "totalprecip_mm": 0.0,
                    "totalprecip_in": 0.0,
                    "avgvis_km": 10.0,
                    "avgvis_miles": 6.0,
                    "avghumidity": 78.0,
                    "daily_will_it_rain": 0,
                    "daily_chance_of_rain": 0,
                    "daily_will_it_snow": 0,
                    "daily_chance_of_snow": 0,
                    "condition": {
                        "text": "Sunny",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
                        "code": 1000
                    },
                    "uv": 1.0
                },
                "astro": {
                    "sunrise": "08:01 AM",
                    "sunset": "04:17 PM",
                    "moonrise": "12:42 PM",
                    "moonset": "04:13 AM",
                    "moon_phase": "Waxing Gibbous",
                    "moon_illumination": "71"
                },
            }
        ]
    }
}

current_alerts = {
    "alerts": {
        "alert": [
            {
                "headline": "Environnement Canada",
                "msgtype": "",
                "severity": "",
                "urgency": "",
                "areas": "",
                "category": "Extreme temperature value",
                "certainty": "",
                "event": "extreme cold",
                "note": "",
                "effective": "2022-01-10T20:29:52+00:00",
                "expires": "2022-01-11T12:29:52+00:00",
                "desc": "\n###\n\nRisks are greater for young children, older adults, people with chronic illnesses, people working or exercising outdoors, and those without proper shelter.\n\nExtreme cold warnings are issued when very cold temperatures or wind chill creates an elevated risk to health such as frost bite and hypothermia.\n\nPlease continue to monitor alerts and forecasts issued by Environment Canada. To report severe weather, send an email to QCstorm@ec.gc.ca or tweet reports using #QCStorm.\n",
                "instruction": ""
            },
            {
                "headline": "Wind Chill Warning issued January 10 at 3:05PM EST until January 11 at 3:00PM EST by NWS",
                "msgtype": "Alert",
                "severity": "Moderate",
                "urgency": "Expected",
                "areas": "Eastern Clinton",
                "category": "Met",
                "certainty": "Likely",
                "event": "Wind Chill Warning",
                "note": "Alert for Eastern Clinton (New York) Issued by the National Weather Service",
                "effective": "2022-01-10T19:00:00-05:00",
                "expires": "2022-01-11T15:00:00-05:00",
                "desc": "...WIND CHILL WARNING IN EFFECT FROM 7 PM THIS EVENING TO 3 PM\nEST TUESDAY...\n* WHAT...Dangerously cold wind chills expected. Wind chills as\nlow as 35 below zero.\n* WHERE...In Vermont, Western Franklin County. In New York,\nEastern Clinton County.\n* WHEN...From 7 PM this evening to 3 PM EST Tuesday.\n* IMPACTS...The cold wind chills could cause frostbite on exposed\nskin in as little as 10 minutes.\n* ADDITIONAL DETAILS...The coldest wind chill values will occur\nbetween 2 AM and 11 AM on Tuesday.",
                "instruction": "Avoid outside activities if possible. When outside, make sure you\nwear appropriate clothing, a hat, and gloves."
            },
            {
                "headline": "Wind Chill Warning issued January 10 at 3:05PM EST until January 11 at 3:00PM EST by NWS",
                "msgtype": "Alert",
                "severity": "Moderate",
                "urgency": "Expected",
                "areas": "Western Franklin",
                "category": "Met",
                "certainty": "Likely",
                "event": "Wind Chill Warning",
                "note": "Alert for Western Franklin (Vermont) Issued by the National Weather Service",
                "effective": "2022-01-10T19:00:00-05:00",
                "expires": "2022-01-11T15:00:00-05:00",
                "desc": "...WIND CHILL WARNING IN EFFECT FROM 7 PM THIS EVENING TO 3 PM\nEST TUESDAY...\n* WHAT...Dangerously cold wind chills expected. Wind chills as\nlow as 35 below zero.\n* WHERE...In Vermont, Western Franklin County. In New York,\nEastern Clinton County.\n* WHEN...From 7 PM this evening to 3 PM EST Tuesday.\n* IMPACTS...The cold wind chills could cause frostbite on exposed\nskin in as little as 10 minutes.\n* ADDITIONAL DETAILS...The coldest wind chill values will occur\nbetween 2 AM and 11 AM on Tuesday.",
                "instruction": "Avoid outside activities if possible. When outside, make sure you\nwear appropriate clothing, a hat, and gloves."
            },
            {
                "headline": "NWS Burlington (Northern Vermont and New York)",
                "msgtype": "",
                "severity": "",
                "urgency": "",
                "areas": "",
                "category": "Wind,Extreme temperature value",
                "certainty": "",
                "event": "Wind Chill Advisory",
                "note": "",
                "effective": "2022-01-11T00:00:00+00:00",
                "expires": "2022-01-11T20:00:00+00:00",
                "desc": "...WIND CHILL ADVISORY REMAINS IN EFFECT FROM 7 PM MONDAY TO 3 PM\nEST TUESDAY...\n* WHAT...Very cold wind chills expected. Wind chills as low as\n25 below zero.\n* WHERE...Champlain Valley.\n* WHEN...From 7 PM Monday to 3 PM EST Tuesday.\n* IMPACTS...The cold wind chills could cause frostbite on\nexposed skin in as little as 30 minutes.\n* ADDITIONAL DETAILS...The coldest wind chill values will occur\nbetween 2 AM and 11 AM on Tuesday.",
                "instruction": ""
            }
        ]
    }
}
