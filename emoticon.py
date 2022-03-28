"""
###################################################
#                                                 #
#   Made by moontr3, 2022. All rights reserved.   #
#                                                 #
###################################################

 _   _                 _                           
| | | | _____      __ | |_ ___    _   _ ___  ___ _ 
| |_| |/ _ \ \ /\ / / | __/ _ \  | | | / __|/ _ (_)
|  _  | (_) \ V  V /  | || (_) | | |_| \__ \  __/_ 
|_| |_|\___/ \_/\_/    \__\___/   \__,_|___/\___(_)

----------------------------------

emoticon.get_emoticon(text=str, is_sitting=bool, left_hand_up=bool, right_hand_up=bool, round_message=bool)
Return emoticon (string) with text <text>

emoticon.print_emoticon(text=str, is_sitting=bool, left_hand_up=bool, right_hand_up=bool, round_message=bool)
Print emoticon with text <text>

----------------------------------
==================================
----------------------------------
 _____                           _                      _        
| ____|_  ____ _ _ __ ___  _ __ | | ___    ___ ___   __| | ___ _ 
|  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \  / __/ _ \ / _` |/ _ (_)
| |___ >  < (_| | | | | | | |_) | |  __/ | (_| (_) | (_| |  __/_ 
|_____/_/\_\__,_|_| |_| |_| .__/|_|\___|  \___\___/ \__,_|\___(_)
                          |_|

----------------------------------
==================================
import emoticon

text = emoticon.get_emoticon("Hello world!")
----------------------------------
Putting emoticon with text "Hello world!" into the variable


----------------------------------
==================================
import emoticon

emoticon.print_emoticon("Hello world")
----------------------------------
Putting emoticon with text "Hello world!" into the variable


----------------------------------
==================================
import emoticon

text = emoticon.get_emoticon("Hello world!", is_sitting=True)
print(text)
----------------------------------
Putting emoticon that are sitting with text "Hello world!" into the variable and then printing it
"""

###################################################

def get_emoticon(text="How to use: get_emoticon(text=str, is_sitting=bool, left_hand_up=bool, right_hand_up=bool, round_message=bool)", is_sitting=False, left_hand_up=False, right_hand_up=False, round_message=True):
    top_part = " O  "
    middle_part = "/|\ "
    bottom_part = "/ \ "

    if is_sitting == False:
        pass
    elif is_sitting == True:
        bottom_part = "<-> "
    else:
        return "is_sitting isn't a boolean variable."

    if left_hand_up == False and right_hand_up == False:
        pass
    elif left_hand_up == True and right_hand_up == False:
        top_part = "\O  "
        middle_part = " |\ "
    elif left_hand_up == False and right_hand_up == True:
        top_part = " O/ "
        middle_part = "/|  "
    elif left_hand_up == True and right_hand_up == True:
        top_part = "\O/ "
        middle_part = " |  "
    else:
        return "left_hand_up and/or right_hand_up isn't a boolean variable(-s)."

    if "\n" in text:
        return "Text cannot be multiline."

    if round_message == False:
        message_outline = "=" * len(text)

        text = f'''
            {message_outline}
           <{text}>
            {message_outline}
            /
        {top_part}
        {middle_part}
        {bottom_part}
        '''
    elif round_message == True:
        message_outline = "-" * (len(text)-1)

        text = f'''
        ,{message_outline}-,
        |{text}|
        `v{message_outline}`
         
        {top_part}
        {middle_part}
        {bottom_part}
        '''
    else:
        return "round_message isn't a boolean variable."

    return text

###################################################

def print_emoticon(text="How to use: print_emoticon(text=str, is_sitting=bool, left_hand_up=bool, right_hand_up=bool, round_message=bool)", is_sitting=False, left_hand_up=False, right_hand_up=False, round_message=True):
    top_part = " O  "
    middle_part = "/|\ "
    bottom_part = "/ \ "

    if is_sitting == False:
        pass
    elif is_sitting == True:
        bottom_part = "<-> "
    else:
        print("is_sitting isn't a boolean variable.")

    if left_hand_up == False and right_hand_up == False:
        pass
    elif left_hand_up == True and right_hand_up == False:
        top_part = "\O  "
        middle_part = " |\ "
    elif left_hand_up == False and right_hand_up == True:
        top_part = " O/ "
        middle_part = "/|  "
    elif left_hand_up == True and right_hand_up == True:
        top_part = "\O/ "
        middle_part = " |  "
    else:
        print("left_hand_up and/or right_hand_up isn't a boolean variable(-s).")

    if "\n" in text:
        print("Text cannot be multiline.")

    if round_message == False:
        message_outline = "=" * len(text)

        text = f'''
    {message_outline}
   <{text}>
    {message_outline}
    /
{top_part}
{middle_part}
{bottom_part}
        '''
    elif round_message == True:
        message_outline = "-" * (len(text)-1)

        text = f'''
,{message_outline}-,
|{text}|
`v{message_outline}`
         
{top_part}
{middle_part}
{bottom_part}
        '''
    else:
        print("round_message isn't a boolean variable.")

    print(text)

###################################################
