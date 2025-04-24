# Flash-Card-App

A Python-based flashcard application designed to help users learn French vocabulary. The app presents French words on cards that automatically flip to show their English translations after 3 seconds.

## Features

- Interactive flashcard interface with flip animation
- French to English vocabulary learning
- Progress tracking system
- Auto-save learning progress
- Simple and intuitive UI with right/wrong buttons
- Focuses on words you need to practice most

## Requirements

- Python 3.x
- tkinter (usually comes with Python)
- pandas

## Files Structure

- `main.py` - Main application file
- `data/french_words.csv` - Contains the French-English word pairs
- `images/` - Contains UI assets:
  - card_front.png
  - card_back.png
  - right.png
  - wrong.png

## How to Use

1. Run `main.py` to start the application
2. A French word will appear on the screen
3. After 3 seconds, the card will flip to show the English translation
4. Click the ✓ button if you knew the word
5. Click the ✗ button if you didn't know the word
6. Unknown words will appear more frequently in future reviews
7. Your progress is automatically saved between sessions

## Learning Features

- Words you know will be removed from the rotation
- The app creates a "words_to_learn.csv" file to track your progress
- Focus on challenging words that need more practice
- Visual feedback for correct and incorrect answers

## Note

The application will automatically save your progress when you close it. When you restart, it will load your previous learning session, allowing you to continue where you left off.