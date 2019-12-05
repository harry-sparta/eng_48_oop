# OOP Basics

This class is going to cover the basics of OOP

### Covered in this class:

**4 Pillars**:
- Abstractions
- Inheritance
- Polymorphism
- Encapsulation

Other learning outcomes:
- git + GitHub
- Documentation with Markdown 
- Best practices and organisation

### Definitions

Add your definitions:

**Class.**
Is a blue print of an object. It wraps methods and attributes. 
Convention to use capitalisation for classes.

**Methods.**
Just like functions they can take in arguments, run a block of code,
 however, they can only be used by an instance of it's class.
 
 **Attributes.**
 Hold information about our SPECIFIC object. Are set in the def __ init __() method 
 with arguments like any other function.
 
 **__ init __ ().**
 a.k.a - constructor or initialiser. This methods runs every time an object is created. 
 So when you do:
 ````
 animal_1 = Animal('Fred', 10, 2) 
 ````
 
 **Instance/ object.**
 It is an occurrence of an object.

**Self.**
Refers to the object/ instance

**Inheritance.**
Is the ability of classes to inherit characteristic(parameters) and behaviours(methods) from parent class.

**Polymorphsim.**
'Poly' means many and 'morph' means forms. So, polymorphism is many forms. 
Polymorphism in OOP is for the ability to change methods and characteristics of instances fo child classes.
-Method polymorphism (at method level).

**Abstraction.** Is hiding complexity from the user. e.g. heating food in the microwave by pressing a button.
e.g. changing gears in a car via a joystick. e.g. coding languages and binary in computing.

Specific to us, we will:
- Write nice documentation for how to import and use our code
- Use inheritance and importing to hide code
- ultimately we can package it into a module that could be imported PIP (package manager)

## Task:
Create a new project:
- create a class animal:
    - characteristics:
        - alive
        - bones
    - methods:
        - eat
        - sleep 
        - make sound
- create a class Dog()
    - make it inherit from animals
    - give it all the attributes of Animal plus:
        - owner
        - name
        - id_number
        - dog collar
    - methods:
        - all other attributes from Animal
        - eat bone
        - run
        - greet owner
        - polymorth the method to make sound to return 'WOOF!!'
 - one of these methods needs to take an argument. Another method should have a default value.
 - have a separate run file:
    - import all your classes
    - create 2 animals
    - create 2 dogs
    - call some methods on them