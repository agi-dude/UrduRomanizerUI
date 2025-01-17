import gradio as gr

letter_map = {
    u"\u0627": "A",
    u"\u0627": "A",
    u"\u0675": "A",
    u"\u0673": "A",
    u"\u0630": "A",
    u"\u0622": "AA",
    u"\u0628": "B",
    u"\u067E": "P",
    u"\u062A": "T",
    u"\u0637": "T",
    u"\u0679": "T",
    u"\u062C": "J",
    u"\u0633": "S",
    u"\u062B": "S",
    u"\u0635": "S",
    u"\u0686": "CH",
    u"\u062D": "H",
    u"\u0647": "H",
    u"\u0629": "H",
    u"\u06DF": "H",
    u"\u062E": "KH",
    u"\u062F": "D",
    u"\u0688": "D",
    u"\u0630": "Z",
    u"\u0632": "Z",
    u"\u0636": "Z",
    u"\u0638": "Z",
    u"\u068E": "Z",
    u"\u0631": "R",
    u"\u0691": "R",
    u"\u0634": "SH",
    u"\u063A": "GH",
    u"\u0641": "F",
    u"\u06A9": "K",
    u"\u0642": "K",
    u"\u06AF": "G",
    u"\u0644": "L",
    u"\u0645": "M",
    u"\u0646": "N",
    u"\u06BA": "N",
    u"\u0648": "O",
    u"\u0649": "Y",
    u"\u0626": "Y",
    u"\u06CC": "Y",
    u"\u06D2": "E",
    u"\u06C1": "H",
    u"\u064A": "E",
    u"\u06C2": "AH",
    u"\u06BE": "H",
    u"\u0639": "A",
    u"\u0643": "K",
    u"\u0621": "A",
    u"\u0624": "O",
    "ہیں": "AYN",
    "ہیں": "AIN",
    " ": " "}


def romanize(urdu):
    roman = ''
    for i in range(len(urdu)):
        for k, v in letter_map.items():
            if urdu[i] == k:
                roman = roman + v
    return roman.lower()


iface = gr.Interface(fn=romanize, inputs="text", outputs="text", title="Urdu to Roman Transliterator")

if __name__ == "__main__":
    iface.launch()
