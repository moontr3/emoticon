# emoticon
Simple library that allows you to create stickmans with text bubbles.

## Usage
```py
import emoticon

stickman = emoticon.get_emoticon("Hi!", right_hand_up=True)
print(stickman)

emoticon.print_emoticon("How are you doing?", is_sitting=True)
...
```

- `get_emoticon(text, is_sitting, left_hand_up, right_hand_up, round_message)` - Get a string with emoticon

- `print_emoticon(text, is_sitting, left_hand_up, right_hand_up, round_message)` - Print an emoticon

## Reference
| Attribute | Type | Description |
| -=-=-=- | -=-=-=- | -=-=-=- |
| text | String / str | Text for text bubble |
| is_sitting | Boolean (True/False, default: False) / bool | Used for sitting down |
| left_hand_up | Boolean (True/False, default: False) / bool | Used for raising left hand |
| right_hand_up | Boolean (True/False, default: False) / bool | Used for raising right hand |
| round_message | Boolean (True/False, default: True) / bool | Used for changing text bubble style |

## Reference
| Attribute | Unit | Description |
|-----|-----|-----|
| city | | City name |
| country | | Country name |
| lat | | Latitude in decimal degree |
| lon | | Longitude in decimal degree |
| timezone | UTC | Timezone of the city |
| timezone_name | | Region name of the city's timezone |
| temp | °C | Temperature |
| temp_min | °C | Minimm temperature |
| temp_max | °C | Maximum temperature |
| temp_feelslike | °C | Human perception of weather |
| humidity | % | Humidity as percentage |
| visibility | m | Visibility as meters |
| pressure | mB | Atmospheric pressure as millibars |
| uv | | UV index |
| wind_speed | m/s | Wind speed |
| wind_degree | ° | Wind direction in degrees |
| wind_dir | | Wind direction as 16 point compass |
| gust_speed | m/s | Wind gust speed |
| cloudliness | % | Cloudliness as percentage |
| state_wapi | | Weather state description provided by WeatherAPI |
| state_owm | | Weather state description provided by OpenWeatherMap |
