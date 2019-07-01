1.  First step: identify code that repeats.

### Headers

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
      i = detect_header_tags(i)
```

Instead of describing each type of header in a separate statement, we  
need a function (abstraction) that maps any header to its corresponding tag  
(generalises the behaviour to the set of all headers).

```python
def detect_header_tags(l=''):
    for k,v in HEADERS.items():
        line_with_header = re.match(f'{k} (.*)', l)
        if line_with_header:
            rest_string = line_with_header.group(1)
            return OPENING_TAG + v + '>' + rest_string + CLOSING_TAG + v + '>'
    return l
...

for i in lines:
      i = detect_header_tags(i)
```

### Bold text

```python
is_bold = False
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

Both blocks of code describe the same behaviour:  
they map all strings surrounded by `__ __` to strings in `<strong> </strong>` tag.

**Lessons**:
• during the refactor, do not change names of variables too early.  
Changing `i` to `line_with_headers` might improve readability, but at an early  
stage, it will likely break something down the line (especially if the function you're refactoring
is a long pipeline of operations). Cost me at least 15 mins of debugging and printing.  
• in `re.match()`, the `(.*)` each corresponds to one `group`. If `re` matches a phrase, this phrase splits the string
into groups. It's fairly useful for parsing text.

```
m = re.match('(.*)__(.*)__(.*)', curr)
```

gives 3 groups.
You can refer to them as `m.group(1)`, `m.group(2)` etc.
