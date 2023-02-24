from fastapi import FastAPI
import random  # import the random module for shuffling letters
import datetime  # import the datetime module for timestamping

app = FastAPI()  # create a new FastAPI instance

audit_list = []  # create an empty list to store API call details

@app.get("/jumble/{word}")  # define an endpoint for jumbling words
def jumble(word: str):
    letters = list(word)  # convert the input word to a list of letters
    random.shuffle(letters)  # shuffle the letters randomly
    jumbled_word = "".join(letters)  # convert the shuffled letters back to a word
    
    # append the API call details to the audit list
    audit_list.append({
        "api": "jumble",
        "payload": {"word": word},
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    return {"jumbled_word": jumbled_word}  # return the jumbled word as a JSON response

@app.get("/audit")  # define an endpoint for auditing API calls
def audit():
    return {"audit": audit_list[-10:]}  # return the last 10 items in the audit list as a JSON response