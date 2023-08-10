from googletrans import Translator, LANGUAGES

def main(source_text, source_code, dest_code):
    translator = Translator()
    tl = translator.translate(str(source_text), src=source_code, dest=dest_code)
    return tl.text

    #if tl.text is not None:
    #    return tl.text
    #else:
    #    return "Translation failed or resulted in None text."

'''
    print("언어 코드:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language}")

    source_text = input("번역할 텍스트를 입력하세요: ")
    source_language = input("입력한 텍스트의 언어 코드를 입력하세요: ")
    target_language = input("번역할 언어 코드를 입력하세요: ")

    print("\n번역 결과:")
    print(f"원본 언어: {LANGUAGES[source_language]}")
    print(f"번역 언어: {LANGUAGES[target_language]}")
    print(f"번역된 텍스트: {tl.text}")
'''

if __name__ == "__main__":
    main()