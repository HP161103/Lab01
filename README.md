# Lab 01 - MLOps CI/CD Pipeline

**Author:** Heet Patel  
**Course:** MLOps (IE-7374)  
**Institution:** Northeastern University  

## 📋 Overview

This project demonstrates a complete MLOps workflow with automated testing using GitHub Actions. It features a calculator application with comprehensive test coverage and continuous integration/continuous deployment (CI/CD) pipeline.

## 🎯 Key Features

### Calculator Functions
- ✅ **fun1**: Addition of two numbers
- ✅ **fun2**: Subtraction of two numbers
- ✅ **fun3**: Multiplication of two numbers
- ✅ **fun4**: Sum of three numbers
- ✅ **fun5**: Division with zero-division error handling *(Added)*
- ✅ **fun6**: Power/Exponent calculation *(Added)*
- ✅ **fun7**: Modulo operation with error handling *(Added)*
- ✅ **fun8**: Factorial calculation with validation *(Added)*

### Testing & CI/CD
- Dual testing frameworks: **pytest** and **unittest**
- Automated testing on every push via **GitHub Actions**
- Comprehensive test coverage including edge cases and error handling
- Input validation and type checking

## 📁 Project Structure
```
Lab01/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml      # Pytest automation workflow
│       └── unittest_action.yml    # Unittest automation workflow
├── src/
│   ├── __init__.py
│   └── calculator.py              # Main calculator functions
├── test/
│   ├── __init__.py
│   ├── test_pytest.py             # Pytest test cases
│   └── test_unittest.py           # Unittest test cases
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip
- Git

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/HP161103/Lab01.git
   cd Lab01
```

2. **Create virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

## 🧪 Running Tests

### Using Pytest
```bash
pytest test/test_pytest.py -v
```

### Using Unittest
```bash
python -m unittest test.test_unittest
```

### Run All Tests
```bash
pytest test/ -v
```

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** for automated testing:

- **Pytest Workflow**: Runs pytest suite on every push
- **Unittest Workflow**: Runs unittest suite on every push

View workflow status: [Actions Tab](https://github.com/HP161103/Lab01/actions)

### Workflow Features
- ✅ Automatic test execution on push
- ✅ Test result artifacts generation
- ✅ Success/failure notifications
- ✅ Support for multiple branches

## 💡 Unique Modifications

This implementation extends the original lab requirements with:

1. **Additional Mathematical Functions**
   - Division with zero-division handling
   - Power/exponent calculations
   - Modulo operations
   - Factorial computation

2. **Enhanced Error Handling**
   - Type validation for all inputs
   - Custom error messages
   - Edge case handling (zero division, negative factorials)

3. **Comprehensive Testing**
   - 20+ test cases across both frameworks
   - Error condition testing
   - Edge case validation

## 📊 Test Coverage

| Function | Test Cases | Error Handling |
|----------|-----------|----------------|
| fun1-fun4 | 12 tests | ✅ Type validation |
| fun5 (Division) | 5 tests | ✅ Zero division |
| fun6 (Power) | 4 tests | ✅ Type validation |
| fun7 (Modulo) | 4 tests | ✅ Zero modulo |
| fun8 (Factorial) | 6 tests | ✅ Negative numbers |

## 🛠️ Technologies Used

- **Language**: Python 3.8
- **Testing**: pytest, unittest
- **CI/CD**: GitHub Actions
- **Version Control**: Git & GitHub

## 📝 Future Enhancements

- [ ] Add test coverage reports
- [ ] Implement advanced mathematical functions (sqrt, logarithm)
- [ ] Add performance benchmarking
- [ ] Create REST API wrapper

## 📧 Contact

**Heet Patel**  
GitHub: [@HP161103](https://github.com/HP161103)

---

*This project is part of the MLOps course at Northeastern University.*