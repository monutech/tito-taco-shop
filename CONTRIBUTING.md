# Contributing to Tito Taco Shop 🌮

Thank you for your interest in contributing to Tito Taco Shop! Whether it's improving code, adding new features, or updating documentation, your efforts are highly appreciated. This document provides guidelines to ensure smooth collaboration and contribution.

## Setting Up Your Development Environment

### Prerequisites

- Python: Version 3.x
- Git: Latest version

### Steps

1. **Fork the Repository**: Click on the "Fork" button at the top-right corner of the [repository page](https://github.com/monutech/tito-taco-shop).
   
2. **Clone the Forked Repository**: 
   ```sh
   git clone https://github.com/[YourUsername]/tito-taco-shop.git
   ```
   
3. **Navigate to the Project Directory**: 
   ```sh
   cd tito-taco-shop
   ```
   
4. **Install Dependencies**: 
   ```sh
   pip install -r requirements.txt
   ```
   
5. **Create a Virtual Environment** (optional but recommended):
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
   
6. **Run Migrations and Start the Development Server**:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```
   
## How to Submit a Pull Request (PR)

### Branching Strategy

- **Main Branch**: The `main` branch is the primary branch where the stable version of the project resides. Never push changes directly to `main`.
- **Feature Branches**: Create a new branch for each feature or bugfix from `main`.

### Steps to Submit a PR

1. **Create a New Branch**: 
   ```sh
   git checkout -b [branch-name] main
   ```
   
2. **Make Your Changes**: Implement your changes, enhancements, or bugfixes.

3. **Commit Your Changes**: 
   ```sh
   git add .
   git commit -m "Your descriptive commit message"
   ```
   
4. **Push to Your Fork**: 
   ```sh
   git push origin [branch-name]
   ```
   
5. **Open a Pull Request**: Go to the [original repository](https://github.com/monutech/tito-taco-shop) and click on "New pull request". Choose your fork and the branch you created, then click "Create pull request".

6. **Describe Your PR**: Provide a concise title and describe what changes you have made.

7. **Wait for Review**: Maintainers will review your PR and may request changes. Be sure to keep an eye on the comments.

## Questions?

If you have questions or need further guidance, feel free to reach out to the maintainers or raise an issue.

---

Thank you for contributing to Tito Taco Shop! 🎉
