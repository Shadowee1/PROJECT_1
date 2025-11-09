import requests
import sys
from dotenv import load_dotenv
import os
from mistralai import Mistral
from fpdf import FPDF
import pyttsx3
import time


load_dotenv("keys.env")

API_KEY = os.getenv("API_KEY")
API_KEY2 = os.getenv("API_KEY2")
API_KEY_AI = os.getenv("API_KEY_MISTRAL")


# get the userinput in the way you want
def main():
    while True:
        if len(sys.argv) > 1:
            country_name = sys.argv[1].lower().strip()
            break
        else:
            try:
                country_name = (
                    input(
                        "Enter the name of the country whose languages you want to know about:- "
                    )
                    .lower()
                    .strip()
                )
            except EOFError:
                sys.exit("Program interrupted by User.")
            if len(country_name) < 4:
                sys.exit("Shortest name for any country is at least 4 letters long.")
            else:
                break
    data_file, i = country_language_data(country_code(country_name)), 1
    if len(data_file) > 0:
        (
            print(
                f"You can travel very comfortably in {country_name} if you know one and only:-"
            )
            if len(data_file) == 1
            else print(
                f"You can travel very comfortably in {country_name} if you know these languages:-"
            )
        )
        for data in data_file:
            print(i, data, sep=". ")
            i += 1

    # Asking User if he is interested in more information on that specific country
    user_response = (
        input(
            f"Do you want to get more Information on {country_name.title()}(True/False): "
        )
        .strip()
        .lower()
        .capitalize()
    )
    if user_response == "True":
        data_ai = data_on_country(country_name, API_KEY_AI)
    elif user_response == "False":
        sys.exit("THANK YOU FOR USING OUR PROGRAM.")
    else:
        sys.exit(
            "You didn't type one of the desired inputs so this program is going to be Terminated."
        )

    # Creating a pdf by using fpdf library
    pdf_name = input(
        "Name of pdf you want to get as output(must include .pdf at last: "
    )
    if not pdf_name.endswith(".pdf"):
        pdf_name = f"{pdf_name}.pdf"
    save_to_pdf(data_ai, pdf_name)

    # Thanking CS50P Team
    thanking()

    print(end())


# get the 2 alphabet long unique iso identification of the country from what the user game us as input
def country_code(name_of_the_country):
    response = requests.post(
        f"https://aaapis.com/api/v1/info/country/",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Token {API_KEY}",
        },
        json={"country": f"{name_of_the_country}"},
    )
    if response.status_code == 200:
        return response.json()["country_code"]
    else:
        sys.exit(
            "An unexpected Error Occurred while converting country's name to ISO identification for that country."
        )


# using apis to get info about languages spoken in that nation


def country_language_data(country_iso_code):
    language_stats = requests.get(
        f"https://api.apiverve.com/v1/countrylanguages?country={country_iso_code}",
        headers={"x-api-key": API_KEY2},
    )
    if language_stats.status_code == 200:
        return language_stats.json()["data"]["officialLanguages"]
    else:
        sys.exit("An unexpected error occurred.")


# Using an AI to get more information about that country you were asking about
def data_on_country(name_of_the_country, api_key):
    model = "mistral-small-latest"
    client = Mistral(api_key=api_key)

    response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": f"Give me more information about the country of {name_of_the_country} except of it's iso code with specific sections and with it reaching only 500 words. Remember no unicode font only non-unicode font like 'Times' or any other format. your answers should not have unicode font.",
            },
        ],
    )
    return response.choices[0].message.content


def save_to_pdf(text, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Times", size=12)

    pdf.multi_cell(0, 10, text)

    pdf.output(filename)

def end():
    return "Program Ended"

def thanking():
    engine = pyttsx3.init()
    time.sleep(3)
    engine.say("THANK YOU CS50P TEAM.")
    engine.runAndWait()


if __name__ == "__main__":
    main()
