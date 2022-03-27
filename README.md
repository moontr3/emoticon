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
| text | String | Text for text bubble |
| is_sitting | Boolean (default: False) | Used for sitting down |
| left_hand_up | Boolean (default: False) | Used for raising left hand |
| right_hand_up | Boolean (default: False) | Used for raising right hand |
| round_message | Boolean (default: True) | Used for changing text bubble style |

## Reference
| Attribute | Type | Description |
|-----|-----|-----|
| city | | City name |
| is_sitting | Boolean (default: False) | Used for sitting down |
| left_hand_up | Boolean (default: False) | Used for raising left hand |
| right_hand_up | Boolean (default: False) | Used for raising right hand |
| round_message | Boolean (default: True) | Used for changing text bubble style |
