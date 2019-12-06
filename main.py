from flask import Flask

# Import the configurations
from config.configs import Development

# Import the Employee class that will be used to generate a payroll
from resources.employee import Employee

app = Flask(__name__)

# Set up the configuration with the Flask app above
app.config.from_object(Development)


if __name__ == '__main__':
    app.run(debug=True)