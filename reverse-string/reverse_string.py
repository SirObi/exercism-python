def reverse(text):
    return text[::-1]

def reverse_no_step(text):
    '''For interviewers who want a less fancy solution'''
    r_text = ''
    for i in range(len(text)):
        r_text += text[(len(text) - 1) - i]
    return r_text
