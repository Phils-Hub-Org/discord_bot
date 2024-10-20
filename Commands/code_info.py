# ...

# Get the code info based on language and info type

gsc_code_info = {
    "function": "This is a sample Game Script Code (GSC) function snippet:\n```cpp\ninit()\n{\n    // Sample GSC Code here\n}\n```",
    "variable": "This is a sample Game Script Code (GSC) variable snippet:\n```cpp\ni = 0;\n```",
    "thread": "This is a sample Game Script Code (GSC) thread snippet:\n```cpp\nthread()\n{\n    // Sample GSC Code here\n}\n```",
    "while loop": "This is a sample Game Script Code (GSC) loop snippet:\n```cpp\nwhile (true)\n{\n    // Sample GSC Code here\n}\n```",
    "for loop": "This is a sample Game Script Code (GSC) loop snippet:\n```cpp\nfor (i = 0; i < 10; i++)\n{\n    // Sample GSC Code here\n}\n```",
    "if statement": "This is a sample Game Script Code (GSC) if snippet:\n```cpp\nif (true)\n{\n    // Sample GSC Code here\n}\n```",
    "switch": "This is a sample Game Script Code (GSC) switch snippet:\n```cpp\nswitch (i)\n{\n    case 0:\n        // Sample GSC Code here\n        break;\n    default:\n        break;\n}\n```",
    "import statement": "This is a sample Game Script Code (GSC) import snippet:\n```cpp\n#include maps\\_zombiemode_utility;\n```",
    "array": 'This is a sample Game Script Code (GSC) array snippet:\n```cpp\nmyArray = [];\nmyArray[0] = "zombie_thompson";\nmyArray[1] = "zombie_mp40";\n```',
    "function with parameters": "This is a sample Game Script Code (GSC) function with parameters snippet:\n```cpp\nmyFunction(param1, param2)\n{\n    // Sample GSC Code here\n}\n```",
    "return statement": "This is a sample Game Script Code (GSC) return snippet:\n```cpp\nreturn;\n```",
    "break statement": "This is a sample Game Script Code (GSC) break snippet:\n```cpp\nfor (i = 0; i < 10; i++)\n{\n    if (i == 5) break;\n}\n```",
    "continue statement": "This is a sample Game Script Code (GSC) continue snippet:\n```cpp\nfor (i = 0; i < 10; i++)\n{\n    if (i % 2 == 0) continue;\n}\n```",
    "function call": "This is a sample Game Script Code (GSC) function call snippet:\n```cpp\nmyFunction(1, 2);\n```",
    "nested if statement": "This is a sample Game Script Code (GSC) nested if snippet:\n```cpp\nif (a > b)\n{\n    if (b > c)\n    {\n        // Sample GSC Code here\n    }\n}\n```",
    "ternary operator": "This is a sample Game Script Code (GSC) ternary operator snippet:\n```cpp\nresult = (a > b) ? a : b;\n```",
    "single line comment": "This is a sample Game Script Code (GSC) comment snippet:\n```cpp\n// This is a single line comment\n```",
    "multi line comment": "This is a sample Game Script Code (GSC) comment snippet:\n```cpp\n/*\nThis is a\nmulti-line comment\n*/\n```",
    "function returning a value": "This is a sample Game Script Code (GSC) function returning a value snippet:\n```cpp\ngetValue()\n{\n    return 42;\n}\n```",
}

python_code_info = {
    "function": "This is a sample Python code snippet:\n```python\ndef my_function():\n    # Sample Python code here\n```",
    "variable": "This is a sample Python code snippet:\n```python\nx = 5\n```",
    "class": "This is a sample Python code snippet:\n```python\nclass MyClass:\n    # Sample Python code here\n```",
    "for loop": "This is a sample Python code snippet:\n```python\nfor i in range(10):\n    # Sample Python code here\n```",
    "if statement": "This is a sample Python code snippet:\n```python\nif x > 0:\n    # Sample Python code here\n```",
    "while loop": "This is a sample Python code snippet:\n```python\nwhile True:\n    # Sample Python code here\n```",
    "import statement": "This is a sample Python code snippet:\n```python\nimport os\n```",
    "try-except block": "This is a sample Python code snippet:\n```python\ntry:\n    # Sample code that might fail\nexcept Exception as e:\n    # Handle exception here\n```",
    "list comprehension": "This is a sample Python code snippet:\n```python\nsquares = [x**2 for x in range(10)]\n```",
    "lambda function": "This is a sample Python code snippet:\n```python\nadd = lambda x, y: x + y\n```",
    "dictionary": "This is a sample Python code snippet:\n```python\nmy_dict = {'key': 'value'}\n```",
    "set": "This is a sample Python code snippet:\n```python\nmy_set = {1, 2, 3}\n```",
    "function with parameters": "This is a sample Python code snippet:\n```python\ndef greet(name):\n    return f'Hello, {name}!'\n```",
    "default parameter": "This is a sample Python code snippet:\n```python\ndef greet(name='World'):\n    return f'Hello, {name}!'\n```",
    "list method": "This is a sample Python code snippet:\n```python\nmy_list = [1, 2, 3]\nmy_list.append(4)\n```",
    "string formatting": "This is a sample Python code snippet:\n```python\nname = 'Alice'\nformatted = f'Hello, {name}!'\n```",
    "open file": "This is a sample Python code snippet:\n```python\nwith open('file.txt', 'r') as f:\n    content = f.read()\n```",
    "return statement": "This is a sample Python code snippet:\n```python\ndef add(x, y):\n    return x + y\n```",
    "tuple": "This is a sample Python code snippet:\n```python\nmy_tuple = (1, 2, 3)\n```",
    "enumerate": "This is a sample Python code snippet:\n```python\nfor index, value in enumerate(my_list):\n    print(index, value)\n```",
    "list slicing": "This is a sample Python code snippet:\n```python\nmy_list = [1, 2, 3, 4, 5]\nsliced = my_list[1:3]\n```",
    "map function": "This is a sample Python code snippet:\n```python\nsquared = list(map(lambda x: x**2, my_list))\n```",
    "filter function": "This is a sample Python code snippet:\n```python\neven_numbers = list(filter(lambda x: x % 2 == 0, my_list))\n```",
    "class inheritance": "This is a sample Python code snippet:\n```python\nclass MySubclass(MyClass):\n    # Inherited methods here\n```",
    "staticmethod": "This is a sample Python code snippet:\n```python\nclass MyClass:\n    @staticmethod\n    def my_static_method():\n        pass\n```",
}

csharp_code_info = {
    "function": "This is a sample C# code snippet:\n```csharp\nvoid MyFunction() {\n    // Sample C# code here\n}\n```",
    "variable": "This is a sample C# code snippet:\n```csharp\nint x = 5;\n```",
    "class": "This is a sample C# code snippet:\n```csharp\nclass MyClass {\n    // Sample C# code here\n}\n```",
    "for loop": "This is a sample C# code snippet:\n```csharp\nfor (int i = 0; i < 10; i++) {\n    // Sample C# code here\n}\n```",
    "if statement": "This is a sample C# code snippet:\n```csharp\nif (x > 0) {\n    // Sample C# code here\n}\n```",
    "while loop": "This is a sample C# code snippet:\n```csharp\nwhile (true) {\n    // Sample C# code here\n}\n```",
    "using statement": "This is a sample C# code snippet:\n```csharp\nusing System;\n```",
    "try-catch": "This is a sample C# code snippet:\n```csharp\ntry {\n    // Code that may throw an exception\n} catch (Exception ex) {\n    // Handle exception\n}\n```",
    "interface": "This is a sample C# code snippet:\n```csharp\ninterface IMyInterface {\n    void MyMethod();\n}\n```",
    "delegate": "This is a sample C# code snippet:\n```csharp\ndelegate void MyDelegate(string message);\n```",
    "event": "This is a sample C# code snippet:\n```csharp\nclass MyClass {\n    public event EventHandler MyEvent;\n}\n```",
    "property": "This is a sample C# code snippet:\n```csharp\nclass MyClass {\n    public int MyProperty { get; set; }\n}\n```",
    "list": "This is a sample C# code snippet:\n```csharp\nList<int> numbers = new List<int>();\n```",
    "foreach loop": "This is a sample C# code snippet:\n```csharp\nforeach (var number in numbers) {\n    // Sample C# code here\n}\n```",
    "switch statement": "This is a sample C# code snippet:\n```csharp\nswitch (x) {\n    case 1:\n        // Case 1 code here\n        break;\n    case 2:\n        // Case 2 code here\n        break;\n    default:\n        // Default case code here\n        break;\n}\n```",
    "async-await": "This is a sample C# code snippet:\n```csharp\nasync Task MyAsyncMethod() {\n    await Task.Delay(1000);\n}\n```",
    "LINQ query": "This is a sample C# code snippet:\n```csharp\nvar results = from n in numbers where n > 5 select n;\n```",
    "struct": "This is a sample C# code snippet:\n```csharp\nstruct MyStruct {\n    public int MyField;\n}\n```",
    "enum": "This is a sample C# code snippet:\n```csharp\nenum MyEnum {\n    Value1,\n    Value2,\n    Value3\n}\n```",
    "lambda expression": "This is a sample C# code snippet:\n```csharp\nFunc<int, int> square = x => x * x;\n```",
    "extension method": "This is a sample C# code snippet:\n```csharp\npublic static class MyExtensions {\n    public static int Add(this int x, int y) {\n        return x + y;\n    }\n}\n```",
}

class CodeInfo:
    @staticmethod
    async def code_info(ctx, lang, info):
        # Normalize the inputs
        lang = lang.lower()
        info = info.lower().strip()
        
        # Determine the code info based on language and info type
        if lang == "gsc":
            response = gsc_code_info.get(info, None)
        elif lang == "python":
            response = python_code_info.get(info, None)
        elif lang == 'c#':
            response = csharp_code_info.get(info, None)
        else:
            await ctx.send(f"Sorry, I don't support the language `{lang}`.")
            return
        
        if response:
            await ctx.send(response)
        else:
            await ctx.send(f"Sorry, I don't have any information on `{info}` for `{lang}`.")