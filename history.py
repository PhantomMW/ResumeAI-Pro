import json
import os

FILE_NAME = "history.json"


def save_analysis(job_title, result):

    history = []

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, "r") as f:

            history = json.load(f)

    history.append({

        "job": job_title,

        "ats": result.get("ats_score", 0),

        "resume": result.get("resume_score", 0),

        "decision": result.get("hiring_decision", "")

    })

    with open(FILE_NAME, "w") as f:

        json.dump(history, f, indent=4)


def load_history():

    if not os.path.exists(FILE_NAME):

        return []

    with open(FILE_NAME, "r") as f:

        return json.load(f)