# Flask Name Nest

A simple Flask web application that showcases blog posts, provides a fun guessing game based on names, and displays
random numbers.

## Features

- Display a random number and the current year on the home page.
- Guess the gender and approximate age of a person based on their name.
- Display a list of blog posts fetched from a local JSON file.

## Installation and Setup

1. Clone the repository.
   ```
   git clone  https://github.com/j-breedlove/flask_name_nest.git
   ```
2. Navigate to the project directory:

```
cd flask_name_nest
```

3. Install `pipenv` if you haven't already:

```
   pip install pipenv
```

4. Use `pipenv` to create a new virtual environment and install the required packages:

   ```
   pipenv install flask requests
   ```

4. Activate the virtual environment:

   ```
   pipenv shell
   ```

5. Run the application:

   ```
   python app.py
   ```

6. Visit `http://127.0.0.1:5000/` in your browser to access the app.

## APIs Used

- [Genderize.io](https://genderize.io/) - To guess the gender based on a name.
- [Agify.io](https://agify.io/) - To guess the approximate age based on a name.

## License

MIT License. See the [LICENSE](LICENSE) file for details.
