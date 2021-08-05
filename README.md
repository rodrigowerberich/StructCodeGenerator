# About
A quick attempt on the 13th exercise of the "The Pragmatic Programmer" book by Andrew Hunt and David Thomas


The ideia is to get the generator code on the example.txt file and convert it to valid "message" structures in different languages.

Currently supporting C and Pascal

Input:
```
# Adiciona um produto
# a lista do 'pedido'

M AddProduct
F id    int
F name  char[30]
F order_code int
E
```

Expected C output:
```
/* Adiciona um produto */
/* a lista do 'pedido' */
typedef struct {
    int id;
    char[30] name;
    int order_code;
} AddProductMsg;
```

Expected C++ output:
```
/* Adiciona um produto */
/* a lista do 'pedido' */
struct AddProductMsg{
    int id;
    std::array<char, 30> name;
    int order_code;
};
```

Expected Pascal output:
```
{  Adiciona um produto }
{  a lista do 'pedido' }
AddProductMsg = packed record
     id:    LongInt;
     name:    array[0..29] of char;
     order_code:    LongInt;
end ;
```
# Notes
This is in no way meant to be a functional complete transpiler or code generator. It only solves this small specific case.
# How to run
Just download and run the main.py
> python3 main.py

To change if the output should be C, C++ or PASCAL change the following line on main.py to the desired output:
> language = Languages.PASCAL
