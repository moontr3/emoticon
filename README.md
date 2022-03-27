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
