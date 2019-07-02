1.  First step: identify code that repeats.

    #### Headers

    ```python
    for i in lines:
        if re.match('###### (.*)', i) is not None:
            i = '<h6>' + i[7:] + '</h6>'
        elif re.match('## (.*)', i) is not None:
            i = '<h2>' + i[3:] + '</h2>'
        elif re.match('# (.*)', i) is not None:
            i = '<h1>' + i[2:] + '</h1>'
    ```

    should be:

    ```python
    for i in lines:
          i = replace_header_tags(i)
    ```

    Instead of describing each type of header in a separate statement, we  
    need a function (abstraction) that maps any header to its corresponding tag  
    (generalises the behaviour to the set of all headers).

    ```python
    def replace_header_tags(l=''):
        for k,v in HEADERS.items():
            line_with_header = re.match(f'{k} (.*)', l)
            if line_with_header:
                rest_string = line_with_header.group(1)
                return OPENING_TAG + v + '>' + rest_string + CLOSING_TAG + v + '>'
        return l
    ...

    for i in lines:
          i = replace_header_tags(i)
    ```

    #### Bold and italic text

    ```python
    is_bold = False
    is_italic = False
    curr = m.group(1)
    ...

    m1 = re.match('(.*)__(.*)__(.*)', curr)
            if m1:
                curr = m1.group(1) + '<strong>' + \
                    m1.group(2) + '</strong>' + m1.group(3)
                is_bold = True
            m1 = re.match('(.*)_(.*)_(.*)', curr)
    ...

    m1 = re.match('(.*)__(.*)__(.*)', curr)
            if m1:
                is_bold = True
            m1 = re.match('(.*)_(.*)_(.*)', curr)
    # and:
    if is_bold:
        curr = m1.group(1) + '<strong>' + \
            m1.group(2) + '</strong>' + m1.group(3)
    ```

    should be:

    ```python
    curr = m.group(1)
    curr = replace_bold_tags(curr)
    ```

    Both blocks of code describe the same behaviour:  
    they map all strings surrounded by `__ __` to strings in `<strong> </strong>` tag.
    Same goes for italic tags.

    ```python
    def replace_bold_tags(l=''):
        line_with_bold = re.match('(.*)__(.*)__(.*)', l)
        if line_with_bold:
            return line_with_bold.group(1) + '<strong>' + \
                line_with_bold.group(2) + '</strong>' + line_with_bold.group(3)
        return l

    def replace_bold_tags(l=''): # same deal
    ...

    curr = m.group(1)
    curr = replace_bold_tags(curr)
    curr = replace_italic_tags(curr)
    ```

    Now we can actually have those two mappings applied only once in the entire script and remove them from elsewhere:

    ```python
    for i in lines:
          i = replace_header_tags(i)
          i = replace_bold_tags(i)
          i = replace_italic_tags(i)
    ```

2.  Second step: reduce number variables tracking state

    It's hard for a human user to keep in mind the state of the application while reading the code.  
    Now that we have `replace_bold_tags` and `replace_italic_tags`, there is no need to keep track of the state,  
    so `is_bold` and `is_italic` can be removed.

    By now, the script looks like this:

    ```python
    def parse(markdown):
        lines = markdown.split('\n')
        res = ''
        in_list = False
        in_list_append = False
        for i in lines:
            i = replace_header_tags(i)
            i = replace_bold_tags(i)
            i = replace_italic_tags(i)
            m = re.match(r'\* (.*)', i)
            if m:
                if not in_list:
                    in_list = True
                    curr = m.group(1)
                    i = '<ul><li>' + curr + '</li>'
                else:
                    curr = m.group(1)
                    i = '<li>' + curr + '</li>'
            else:
                if in_list:
                    in_list_append = True
                    in_list = False

            m = re.match('<h|<ul|<p|<li', i)
            if not m:
                i = '<p>' + i + '</p>'
            if in_list_append:
                i = '</ul>' + i
                in_list_append = False
            res += i
        if in_list:
            res += '</ul>'
        return res
    ```

    It's still quite hard to follow the code, given the `in_list` and `in_list_append` state variables.  
    They are used to track whether we're inside a list (`<ul>` tag opened but not closed) and whether we are ready  
    to append a closing tag `</ul>`.

    We can instead have one variable to store the unordered list. We can then generate the whole list first,
    and then append it to the result string, rather than appending list items piece-by-piece:

    ```python
    def parse(markdown):
        lines = markdown.split('\n')
        res = ''
        unordered_list = ''
        for i in lines:
            line = replace_header_tags(i)
            line = replace_bold_tags(line)
            line = replace_italic_tags(line)
            m = check_if_list_item(line)
            if m:
                unordered_list += m
                res += U_LIST.format(unordered_list) if is_last_line(i, lines) else ''
                continue
            elif not m and unordered_list:
                res += U_LIST.format(unordered_list)
                unordered_list = ''

            line = catch_all_in_p_tag(line)
            res += line
        return res
    ```

3.  Replace `continue` with code in an if/else block  
    Using `continue` makes reading the code more difficult.
    Now we have:

    ```python
    def parse(markdown):
        lines = markdown.split('\n')
        res = ''
        current_list = ''
        for i in lines:
            line = replace_header_tags(i)
            line = replace_bold_tags(line)
            line = replace_italic_tags(line)

            list_item = check_if_list_item(line)
            if list_item:
                current_list += list_item
                res += U_LIST.format(current_list) if is_last_line(i, lines) else ''
            else:
                res += U_LIST.format(current_list) if current_list else ''
                current_list = ''
                res += apply_p_tag_if_no_tag(line)
        return res
    ```

    One could still try to pack the last `if` block into a function with a descriptive name,  
    but it's unclear whether it would be a good use of time.

4.  Cosmetic  
    At this point, if you have time, you may want to make your code look prettier.  
    For example, use constants and formatted strings instead of putting strings in functions.  
    (This relates to Sandie Metz's concept of a "squint test").

    Example:

    ```python
    line_with_ital.group(1) + ITALIC.format(line_with_ital.group(2)) + line_with_ital.group(3)
    ```

    instead of:

    ```python
    line_with_ital.group(1) + '<em>' + line_with_ital.group(2)) + '<em>'+ line_with_ital.group(3)
    ```

**Lessons**:  
• during the refactor, do not change names of variables too early.  
Changing `i` to `line_with_headers` might improve readability, but at an early  
stage, it will likely break something down the line (especially if the function you're refactoring
is a long pipeline of operations). Cost me at least 15 mins of debugging and printing.  
• in `re.match()`, the `(.*)` each corresponds to one `group`. If `re` matches a phrase, this phrase splits the string
into groups. It's fairly useful for parsing text.

```
m = re.match('(._)\_\_(._)\_\_(.\*)', curr)
```

gives 3 groups.
You can refer to them as `m.group(1)`, `m.group(2)` etc.

• each if-else block is usually a sign it can be refactored into a function that makes a decision (performs
some kind of mapping)  
• when mapping a list to another list, it may make sense to not mutate the original list, and
save each item into a new variable:

```python
for i in lines:
    line = replace_header_tags(i)
    line = replace_bold_tags(line)
    # etc.
```

• even better, if possible, you can use the `map` operation on the list, to make the code more functional
