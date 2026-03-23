# BLX-UNKNOWN-0
# PROJECT 13 // TYPING SPEED TEST
 
import time   # NEW CONCEPT 1: time module
import random
 
SENTENCES = [
    "the quick brown fox jumps over the lazy dog",
    "python is a powerful and beginner friendly programming language",
    "practice makes perfect when it comes to typing speed",
    "every expert was once a beginner who refused to give up",
    "code is like poetry it should be clean and easy to read",
    "the best way to learn programming is to build real projects",
    "nepal is a beautiful country with the highest mountains on earth",
]
 
def calculate_accuracy(original, typed):  # NEW CONCEPT 2: comparing strings word by word
    original_words = original.split()
    typed_words = typed.split()
    
    correct = 0
    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i] == typed_words[i]:
            correct += 1
    
    total = len(original_words)
    return round((correct / total) * 100, 1)
 
def get_wpm(text, elapsed_seconds):  # NEW CONCEPT 3: WPM formula
    words = len(text.split())
    minutes = elapsed_seconds / 60
    return round(words / minutes)
 
def rating(wpm):
    if wpm >= 80:
        return "🔥 Elite"
    elif wpm >= 60:
        return "⚡ Fast"
    elif wpm >= 40:
        return "✅ Average"
    elif wpm >= 20:
        return "🐢 Slow"
    else:
        return "🐌 Beginner"
 
def play():
    sentence = random.choice(SENTENCES)
    
    print("\n" + "=" * 55)
    print("  ⌨️  TYPING SPEED TEST — BLX_UNKNOWN-0")
    print("=" * 55)
    print("\nType this sentence EXACTLY:")
    print(f"\n  👉 {sentence}\n")
    input("Press ENTER when ready...")
    print("\nGO! ⬇️\n")
    
    start = time.time()      # start timer
    typed = input("> ").strip().lower()
    end = time.time()        # stop timer
    
    elapsed = end - start    # NEW CONCEPT 1 in use: time difference
    
    wpm = get_wpm(typed, elapsed)
    accuracy = calculate_accuracy(sentence, typed)
    
    print("\n--- Results ---")
    print(f"⏱️  Time     : {elapsed:.2f} seconds")
    print(f"🚀 WPM      : {wpm}")
    print(f"🎯 Accuracy : {accuracy}%")
    print(f"🏆 Rating   : {rating(wpm)}")
    
    if typed == sentence:
        print("\n✅ Perfect match!")
    else:
        print(f"\n📝 Original : {sentence}")
        print(f"✍️  You typed: {typed}")
 
def main():
    while True:
        play()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Keep practicing!")
            break
 
if __name__ == "__main__":
    main()