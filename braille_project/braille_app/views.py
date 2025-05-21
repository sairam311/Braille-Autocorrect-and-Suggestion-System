from django.shortcuts import render
from rapidfuzz import process, fuzz

# Full dictionary should ideally come from a DB or an external file
# Sample Braille Dictionary - Starter List
BRAILLE_DICTIONARY = [
    # Core Vocabulary
    "apple", "ball", "cat", "dog", "egg",
    "fish", "goat", "hat", "ink", "jug",

    # Educational & Assistive Context
    "learn", "read", "write", "study", "teach",
    "school", "student", "braille", "keyboard", "dots",

    # Accessibility & Interaction
    "touch", "feel", "voice", "sound", "access"
]

def suggest_word(input_word):
    # Use rapidfuzz to find the best match
    match = process.extractOne(input_word, BRAILLE_DICTIONARY, scorer=fuzz.ratio, score_cutoff=50)
    return match[0] if match else "No suggestion"

def index(request):
    suggestion = ''
    if request.method == 'POST':
        braille_input = request.POST.get('braille_input', '').strip().lower()
        if braille_input:
            suggestion = suggest_word(braille_input)
    return render(request, 'index.html', {'suggestion': suggestion})
