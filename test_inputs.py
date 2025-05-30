# test_inputs.py
from ai_client import ask_ai

examples = [
"An unpatched vulnerability in Apache Struts was exploited by a hacker group linked to North Korea to gain access to U.S. water treatment plant SCADA systems. The attackers exfiltrated data and left behind ransomware payloads.",
"A coordinated drone swarm was detected near a NATO military depot in Poland. The drones appeared to be conducting surveillance and evaded jamming attempts before disappearing toward Belarusian airspace.",
"Thousands of fake social media accounts were used to spread misinformation about an upcoming German referendum, including forged statements from officials and AI-generated video clips impersonating news anchors.",
"A Chinese-owned company quietly acquired a key sensor manufacturer supplying components to U.S. critical infrastructure contractors. The deal was approved by a shell intermediary registered in the Cayman Islands.",
"A disgruntled employee at the cybersecurity firm NetSecure attempted to sell admin credentials for a major European bank on the dark web. The incident was flagged by Europol during a routine marketplace scan.",
"Hospitals across Brazil reported simultaneous outages of medical devices linked to a firmware update from a third-party vendor. The issue disabled ventilators and biometric monitors in ICU units for several hours.",
"Severe flooding in northern Italy damaged fiber-optic trunk lines, disrupting internet and emergency communications across four provinces. No foul play is suspected, but restoration could take weeks.",
"A fake NGO operating under the name 'Children for Freedom' has been conducting door-to-door surveys in rural Ukrainian towns, asking detailed questions about military-age residents and logistics infrastructure.",
"An educational app used by over 10 million K-12 students in the U.S. was found sending unencrypted behavioral data to a third-party analytics firm based in Singapore, raising national data security concerns."
]

for ex in examples:
    print(f"Q: {ex}")
    print(f"A: {ask_ai(ex)}\n{'-'*40}\n")
