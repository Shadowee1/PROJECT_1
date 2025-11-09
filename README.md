 # LANGUAGES AND OTHER INFO OF COUNTRIES
    #### Video Demo:  'https://youtu.be/_ksOhSGuxLM'
    #### Description:
     This project is a simple yet powerful tool designed to fetch detailed information about countries using multiple APIs. The key functionalities include retrieving the ISO country code, obtaining data about languages spoken in the country, and gathering additional insights through an AI-powered API. This project is ideal for anyone interested in geography, linguistics, or AI integration with real-world data.

The program interacts with the user by prompting them to enter the name of a country. Alternatively, users can provide the country name through command line arguments, allowing for flexible input methods depending on user preference. This dual input method enhances usability, whether the project is run in an interactive shell or as part of a script.



# REQUIREMENTS FOR INPUT:
        There are some clear requirements for input. Some of them are:
    1. The name of the country should not be an abbreviation.
    2. If the name of country is like this "Czech Republic" then please considering
        typing name in "" (double quotes) if using name_of_the_country CLA (command line arguments).
    3. Please remember that the shortest name for any country is something like
        "FIJI" or "CHAD" so that number that "4" is not randomly selected.
    4. Please ensure you have a stable internet connection as this code fetches
        information from various APIs.

# How different functions work:

    (i) country_code(name_of_the_country):
        This fn takes in user input (as parameter suggests it takes name of the
    country). This function uses an Api to get ISO code of the country from the
    name of the country and then returns it to the main() function.

    (ii) country_language_data(country_iso_code):
        It just uses another API to get the information on languages spoken
    in that country using the ISO code we got in our call to prior function.

    (iii) data_on_country(name_of_the_country, api_key):
        Using an AI API, this function provides additional contextual information about the country, including historical facts, demographics    economic data, or current events, based on the user’s query. This integration showcases how AI can supplement traditional API data with nuanced insights.

    (iv) save_to_pdf(text, filename="output.pdf"):
             After gathering all relevant data, this function formats and saves the information into a PDF document. Users can customize the
        filename as needed. This feature allows easy sharing and offline access to the project output.

    (v) thanking():
        This function doesn't have to do with any functioning of the code it
    is just my way of thanking CS50P team.

# APIs used:-
    1. AAPIS country ISO code API
    (This API translates country names into their official ISO codes, serving as a foundation for further data queries.)

    2. API Verve - Country language API
    (It provides detailed language information associated with countries, helping understand linguistic distributions worldwide.)

    3. Mistral AI API
    (An AI-driven service that generates contextual, descriptive, and insightful information about countries, enhancing the factual data with human-like understanding.)

    1st API deals with getting ISO code for country from it's name.
    2nd one deals with getting language from the ISO code we received from the
        API we used earlier.
    3rd one deals with AI part of this code.


    NOTE: You need authorisation for using all three APIs used here.

# SUMMARY:
    Accepts user input via interactive prompt or command line arguments for flexibility.

    Fetches official ISO country codes using the AAPIS API based on country name.

    Retrieves detailed language information through API Verve using the ISO code.

    Integrates Mistral AI API to provide rich, contextual info like history, demographics, and current events.

    Generates a customizable PDF report to save and share the compiled country data offline.

    Enforces clear input requirements (full country names, use of quotes for multi-word names).

    Requires stable internet connection for real-time API data fetching.

    Includes a “thanking” function as a personal touch without affecting core operations.

    Combines traditional APIs and AI for a modern, informative, and user-friendly project experience.



