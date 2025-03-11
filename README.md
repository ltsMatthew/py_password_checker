# 🔐 Password Strength Checker

## 📌 Project Description
This is a simple command-line tool that evaluates the strength of a password based on five security rules:

✅ Minimum 8 characters

✅ At least one uppercase letter

✅ At least one lowercase letter

✅ At least one digit

✅ At least one special character (!@#$%^&*(),.?":{}|<>)


It uses regular expressions (re module) for pattern matching and secure password input (getpass module) to hide the password while typing.

---------------------------------------------------------------------------------------------------------------

🚀 How to Run the Program

## 1️⃣ Prerequisites
Make sure you have Python 3 installed on your system. You can check by running:

```python --version```

or

```python3 --version```

---------------------------------------------------------------------------------------------------------------

## 2️⃣ Clone the Repositor

```git clone https://github.com/ltsMatthew/py_password_checker.git```

```cd py_password_checker```

---------------------------------------------------------------------------------------------------------------

## 3️⃣ Run the Script

```python password_checker.py```

or

```python3 password_checker.py```

---------------------------------------------------------------------------------------------------------------

## 🎯 Example Output

>Enter your password: ********
>
>Password Strength Analysis:
>
>- Length: Pass
>  
>-  Uppercase: Fail
>  
>- Lowercase: Pass
>  
>- Digit: Pass
>  
>- Special: Fail
>
>Moderate Password – Consider Making it Stronger!

---------------------------------------------------------------------------------------------------------------

If the password is weak, it will recommend changing it:

>Weak Password! Change it Immediately!

---------------------------------------------------------------------------------------------------------------

If the password is strong it will display:

```Strong Password!```

---------------------------------------------------------------------------------------------------------------

## 📜 Technologies Used

* Python 🐍
* Regular Expressions (re) for pattern matching
* getpass for secure password input
