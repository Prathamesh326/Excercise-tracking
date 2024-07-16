# Exercise Tracker

This project is a simple exercise tracker that logs your workouts and records the details in a Google Sheet. The application uses the Nutritionix API to process exercise data and store the information in a specified Google Sheet.

## Features

- Input exercise details manually.
- Uses the Nutritionix API to calculate calories burned.
- Logs exercise details (date, time, exercise name, duration, calories) in a Google Sheet.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Prathamesh326/Excercise-tracking.git
    cd Excercise-tracking
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables. Create a `.env` file in the root directory of your project and add the following:
    ```plaintext
    APP_ID=your_app_id
    API_KEY=your_api_key
    exercise_endpoint=https://trackapi.nutritionix.com/v2/natural/exercise
    sheet_endpoint=your_google_sheet_endpoint
    USER=your_sheet_username
    PASSWORD=your_sheet_password
    ```

5. Run the application:
    ```bash
    python main.py
    ```

## Usage

1. When prompted, enter the details of the exercises you did. For example:
    ```plaintext
    Tell me which exercises you did: ran 3 miles and cycled for 30 minutes
    ```

2. The application will send this information to the Nutritionix API to calculate the calories burned and other details.

3. The workout details will then be logged in the specified Google Sheet.

## Dependencies

- requests
- dotenv

Make sure to add these to your `requirements.txt` file:
```plaintext
requests
python-dotenv
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Open a pull request.
