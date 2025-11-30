
import wikipedia

def main():
    print("Welcome to the Wikipedia Search Tool.\n")
    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("\nThank you.")
            break
        try:
            page = wikipedia.page(title, autosuggest=False)
            print("\n" + page.title)
            print(page.summary[:500] + "...\n")
            print(page.url + "\n")
        except wikipedia.DisambiguationError as e:
            print("\nWe need a more specific title. Try a new search:\n")
            print(e.options[:15], "...\n")
        except wikipedia.PageError:
            print(f'\nPage id "{title}" does not match any pages. Try some other id!\n')
        except Exception as e:
            print(f"\nunexpected error occurred: {e}\n")

main()
