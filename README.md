# OOP Exam: E-Commerce & Animal Systems

A Python-based Object-Oriented Programming project demonstrating core OOP principles including Inheritance, Polymorphism, Encapsulation, and Interfaces (using Abstract Base Classes). 

## 📦 Project Structure

This repository is divided into two main sections:

### 1. Customer Order Management System (Main)
An e-commerce order processing system handling different types of orders and customers.
* **`Item.py`**: Represents a product with a name and price.
* **`Customer.py`**: Manages customer details and their associated orders.
* **`Order.py`**: Base class for standard customer orders.
* **`VipOrder.py`**: Inherits from `Order`, applying special business logic/discounts for VIPs.
* **`Gift.py`**: Handles gift-specific order logic.
* **`main.py`**: The entry point to test the e-commerce system.

### 2. Animal & Pet Hierarchy (Bonus)
An implementation of a classic UML diagram using Python's `abc` module to simulate interfaces and abstract classes.
* **`Animal.py`**: Abstract base class with a protected `legs` attribute and abstract `eat()` method.
* **`Pet.py`**: Abstract class acting as an interface with `getName()`, `setName()`, and `play()` methods.
* **`Spider.py`**: Inherits from `Animal`.
* **`Cat.py` & `Fish.py`**: Inherit from `Animal` and implement the `Pet` interface, showcasing multiple inheritance and method overriding.
* **`bonus/main_for_bonus.py`**: The entry point to test polymorphism across the animal hierarchy.
