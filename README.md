# Braille-Autocorrect-and-Suggestion-System

A Django-based application that provides auto-correction and word suggestions for Braille input using QWERTY Braille typing format. Designed for visually impaired users to improve typing accuracy and minimize frustration from mispressed keys.

---

## 🧠 Project Background

Braille is a tactile writing system using raised dots, where each character is a unique combination of six dots arranged in a 2x3 matrix. Visually impaired users can type Braille using a standard QWERTY keyboard mapped to specific Braille dots:

| Braille Dot | QWERTY Key |
|-------------|------------|
| Dot 1       | D          |
| Dot 2       | W          |
| Dot 3       | Q          |
| Dot 4       | K          |
| Dot 5       | O          |
| Dot 6       | P          |

Users press combinations of these keys to form Braille characters. Errors such as missing, extra, or incorrect key presses are common, making a real-time auto-correction system essential.

---

## 🚀 Features

- ✅ Suggests closest word based on Braille-like input using fuzzy matching.
- ✅ Efficient correction of typos, extra/missing characters.
- ✅ Optimized with `rapidfuzz` for real-time performance.
- ✅ Easily expandable dictionary for learning and accessibility contexts.
- ✅ Django-based UI for easy web testing.

---