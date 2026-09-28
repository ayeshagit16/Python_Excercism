'''
Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and all pairs are matched and nested correctly. Any other characters should be ignored.
'''

def is_paired(input_string):
    '''
    Remove unwanted string data except for the required.
    Replace all the braces with empty string in the filtered string
    Check if the remaining string is empty
    '''
    
    filtered_text = "".join(char for char in input_string if char in "(){}[]")

    while "()" in filtered_text or "{}" in filtered_text or "[]" in filtered_text:
        filtered_text = filtered_text.replace("()", "")
        filtered_text = filtered_text.replace("{}", "")
        filtered_text = filtered_text.replace("[]", "")

    return filtered_text == ""
