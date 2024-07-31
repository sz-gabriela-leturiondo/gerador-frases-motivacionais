import requests
from googletrans import Translator
# from google.cloud import translate_v2 as translate

def get_motivational_quote():
    """Fetches a random motivational quote from ZenQuotes API."""
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an HTTPError for bad responses
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f"{quote} - {author}"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching quote: {e}")
        return "Não foi possível obter uma citação motivacional no momento."

def translate_to_portuguese(text):
    """Translates a given text from English to Portuguese."""
    try:
        translator = Translator()
        translation = translator.translate(text, src='en', dest='pt')
        return translation.text
    except Exception as e:
        print(f"Error translating text: {e}")
        return text  # Fallback to the original text if translation fails

if __name__ == "__main__":
    quote = get_motivational_quote()
    translated_quote = translate_to_portuguese(quote)
    print(translated_quote)
