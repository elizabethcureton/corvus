# test_inputs.py
from ai_client import ask_ai

examples = [
    "What is the one location you are sure to find cotton candy?",
    "What threats face water treatment plants?",
    "Summarize this paragraph: “Serbian defense enterprises, contrary to the ‘neutrality’ declared by official Belgrade, continue to supply ammunition to Kyiv,” the Russian Foreign Intelligence Service, SVR, said in a statement. The statement alleged that the export of the Serbian arms to Ukraine are going through NATO intermediaries, “primarily the Czech Republic, Poland and Bulgaria. Recently, exotic options involving African states have also been used for this purpose. Serbia’s populist President Aleksandar Vucic told the state RTS television that he has recently discussed the issue of the arm exports to Ukraine with Russian President Vladimir Putin and that it was agreed that the two countries form a “working group” to establish how Serbian-made weapons reach the Ukrainian frontlines."]

for ex in examples:
    print(f"Q: {ex}")
    print(f"A: {ask_ai(ex)}\n{'-'*40}\n")
