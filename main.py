import json
from models.schemas import TaxPayer
from agents.schedule_c_agent import ScheduleCAgent
from agents.schedule1_agent import Schedule1Agent
from agents.form1040_agent import Form1040Agent
from dotenv import load_dotenv
import os

load_dotenv()


def main():

    
    with open("input.json") as f:
        data = json.load(f)

    taxpayer = TaxPayer(**data)

    schedule_c = ScheduleCAgent()
    schedule1 = Schedule1Agent()

    sc_output = schedule_c.run(taxpayer)
    print("✅ Schedule C Output:", sc_output)

    s1_output = schedule1.run(sc_output)
    print("✅ Schedule 1 Output:", s1_output)

    form1040 = Form1040Agent()
    final = form1040.run(taxpayer, s1_output)

    print(final.model_dump_json(indent=2))


main() 