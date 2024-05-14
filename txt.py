text = """In a world often dominated by negativity, it's important to remember the power of kindness and compassion. Small acts of kindness have the ability to brighten someone's day, uplift spirits, and create a ripple effect of positivity that can spread far and wide. Whether it's a smile to a stranger, a helping hand to a friend in need, or a thoughtful gesture to a colleague, every act of kindness has the potential to make a difference in someone's life.Beyond individual actions, there is also immense power in collective efforts to create positive change. When communities come together to support one another, incredible things can happen. From grassroots initiatives to global movements, people are uniting to tackle pressing social and environmental issues, driving meaningful progress and inspiring hope for a better future.It's also important to recognize the strength that lies within each and every one of us. We all have the ability to make a positive impact, no matter how small our actions may seem. By tapping into our innate compassion and empathy, we can cultivate a culture of kindness and empathy that enriches our lives and those around us.So let's embrace the power of kindness, and strive to make the world a better place one small act at a time. Together, we can create a brighter, more compassionate future for all."""
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
tokens = [token.text.lower() for token in doc
          if not token.is_stop and
          not token.is_punct and
          token.text !='\n']
tokens
tokens1=[]
stopwords = list(STOP_WORDS)
allowed_pos = ['ADJ','PROPN','VERB','NOUN']
for token in doc:
    if token.text in stopwords or token.text in punctuation:
        continue
    if token.pos_ in allowed_pos:
        tokens1.append(token.text)
tokens1
from collections import Counter
word_freq
max_freq = max(word_freq.values())
for word in word_freq.keys():
    word_freq[word] = word_freq[word]/max_freq
sent_token
sent_score = {}
for sent in sent_token:
    for word in sent.split():
        if word.lower() in word_freq.keys():
            if sent not in sent_score.keys():
                sent_score[sent] = word_freq[word]
            else:
                sent_score[sent] +=word_freq[word]
        print(word)
sent_score
import pandas as pd
pd.DataFrame(list(sent_score.items()),columns=['Sentence','Score'])
from heapq import nlargest
" ".join(n)
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import END

# Importing the summarization code
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

def summarize_text():
    # Get text from the text box
    text = text_box.get("1.0", "end-1c")

    # Loading spaCy model
    nlp = spacy.load('en_core_web_sm')

    # Tokenization and removing stopwords
    doc = nlp(text)
    tokens = [token.text.lower() for token in doc
              if not token.is_stop and not token.is_punct and token.text != '\n']

    # Calculating word frequency
    word_freq = Counter(tokens)
    if not word_freq:
        messagebox.showerror("Error", "No words found in the text.")
        return

    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    # Sentence tokenization
    sent_token = [sent.text for sent in doc.sents]

    sent_score = {}
    for sent in sent_token:
        for word in sent.split():
            if word.lower() in word_freq.keys():
                if sent not in sent_score.keys():
                    sent_score[sent] = word_freq[word]
                else:
                    sent_score[sent] += word_freq[word]

    # Select top-scoring sentences based on user input
    num_sentences = int(num_sentences_entry.get())
    summarized_sentences = nlargest(num_sentences, sent_score, key=sent_score.get)

    # Display summarized text in the result box
    result_box.delete(1.0, END)
    result_box.insert(END, " ".join(summarized_sentences))


root = tk.Tk()
root.title("Text Summarizer")

# Text box for input
text_box = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_box.pack(pady=10)

# Entry field for the number of sentences
num_sentences_label = tk.Label(root, text="Number of Sentences:")
num_sentences_label.pack()
num_sentences_entry = tk.Entry(root, width=10)
num_sentences_entry.insert(END, "3")  # Default value
num_sentences_entry.pack()

# Button to summarize
summarize_button = tk.Button(root, text="Summarize", command=summarize_text)
summarize_button.pack(pady=5)

# Result box for output
result_box = scrolledtext.ScrolledText(root, width=50, height=5, wrap=tk.WORD)
result_box.pack(pady=10)

root.mainloop()
from transformers import pipeline
summarizer=pipeline("summarization",model='t5-base',tokenizer='t5-base',framework='pt')
print(summary[0]['summary_text'])
import tkinter as tk
from transformers import pipeline

def summarize_text():
    # Get text from the input text box
    text = text_entry.get("1.0", "end-1c")

    # Summarize the text
    summary = summarizer(text, max_length=100, min_length=10, do_sample=False)

    # Update the output text box with the summary
    output_text.delete("1.0", "end")
    output_text.insert("1.0", summary[0]['summary_text'])

# Create a Tkinter window
window = tk.Tk()
window.title("Text Summarizer")

# Create input text box
text_entry = tk.Text(window, height=10, width=60)
text_entry.pack(pady=10)

# Create a button to trigger text summarization
summarize_button = tk.Button(window, text="Summarize", command=summarize_text)
summarize_button.pack()

# Create output text box
output_text = tk.Text(window, height=10, width=60)
output_text.pack(pady=10)

# Initialize the summarizer pipeline
summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="pt")

# Run the Tkinter event loop
window.mainloop()


