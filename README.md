# Filexts
Filexts is a module for working on file extension-searching.

It searchs the file extension in a number of given directory, with much respect to android,
and return a list containing all filenames ending in that particular file extension.

The name filexts comes from **Fil**e **ext**ension **s**earching

## API
### filexts.Filexts(root_dir, search_depth)

Parameter: `root_dir`—is file path string state where search starts, `search_depth`

### filexts.Filexts.list()

Return a list of all paths starting with `root_dir`.

**Note** that a Filext object supports iteration.

### Example

```python
from filexts import Filexts
f = Filexts("//storage/emulated/0/*")
    
print(f.list())

for I in f: # this the alternative to f.list()
    rint(I)
```

## Author
Jacob M. Mugala (maexdev@outlook.com)

# License
MIT License

Copyright (c) 2022 MaexUp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

