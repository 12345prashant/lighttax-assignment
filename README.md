<<<<<<< HEAD
# lighttax-assignment
=======
**Flow Diagram**

https://drive.google.com/file/d/15ZlLU44XlrYHls6n6ojPB8gz1IyOOUH_/view?usp=sharing

<img width="749" height="547" alt="Screenshot 2026-02-28 175908" src="https://github.com/user-attachments/assets/94c30c64-5648-428a-bd1e-c37e74fe76b3" />




**System Architecture**

The system follows a pipeline-based architecture.

Input JSON
   ->
Schedule Instruction Processing
   ->
Income Calculation ( Schedule c)
   ->
Deduction Processing (Schedule 1) 
   ->
Taxable Income Calculation (Form 1040) 
   ->
Final Tax Computation
   ↓
Output Generation

**Project Structure**
 main.py -> Entry point
 input.json -> Test case
 data/pdfs -> Instructions (Schedule c, Schedule 1, Form 1040) 
 model/schemas.js -> Defined Structured of the input and output data for each agent
 agents -> Base Agent (Base class) , Schedule_c_agent , Scheduler_1_agent, Form_1040_agent
 tools -> pdf_navigator tool , deductio_tool , tax_table


 **Approach:**

 1. As mentioned in the assignment ( to complete 3 modules) , I have chosen 3 modules ( Form 1040, Schedule c , Schedule 1)
 2. Form_1040 , Schedule_c , Schedule_1 are 3 agents connected with each in a chain structure such that tax payer data first goes to schedule_c agent which calculates , extra incomes , profit and loss via gig works .
 3. The output of schedule_c agent is than feeded to schedule_1 which calculates the adjustments and additional expenses that will not be included in tax calculations.
 4. The output of schedule_1 agent is than feeded to form_1040 agent that uses predefined python functions to calcualte tax deductions according to user tax income.
 5. Schedule_c and Schedule_1 uses pdf_navigator tool to retrives instructions from the documents.
 6. Currently I am using keyword search method to fetch data from a pdf ( we can scale it to rag pipeline)

**LLM Used** : Cohere
**Framework**: Langchain

**Steps to Start the application**
Step 1: Clone the repository.
Step 2: Install dependecies: pip install langchain langchain-cohere pydantic PyPDF2 python-dotenv  
Step 3: python main.py


**How did you break down the paper into implementable pieces? What was your plan before you started coding?**

My Idea was to build a Supervisor agent that will control the subagents ( schedule_c , schedule_1, Form 1040) . First I thaught that we need to use a langgraph but later i realized that the flow is fixed , for example first the schedule_agent will be invoked its output will be feeded to schedule_1 and than further this goes on. So I changed my plan to use langchain because the workflow is fixed. 
My approach was to build a rag pipleline such that during chunking the instructions pdf we will store some metadata like file_name , page number etc. So we can use that same rag pipeline for each subagent . We can apply filtering over chunks before retrieving instructions , for eg. if the schedule_c agent is running than we will apply filtering over chunks such that the response is generated only from schedule_c instructions pdf. 
The response from sub agents will be passed in chain and at the end form_1040 will use pre defined determinstic tools to calculate tax. 

**How did you model the dependency graph between forms? Did you think in terms of a DAG, a pipeline, message passing?**

Yes, My thinking was to follow a rag pipeline by retrieving data by applying pre filtering . A pipeline where all the 3 agents is connected in chain based structure and the output is passed node by node. 

**What was your strategy for grounding LLM reasoning in IRS instructions? How did you decide what context to feed the model?**

My thinking was that , give llm a large amount of context to avoid hallucinations. For each subagent i have attached a system prompt ( for eg. You are IRS Schedule C expert.

IRS Instructions:
{context}

Explain briefly how net profit is computed from income and expenses.
Return JSON:

{{
"citation": "IRS reference used"
}}) . so the context comes from rag pipleline by extracting data from the instructions pdf. Each agent has its own pdf of instructions to deal with so the context for each agent will always going to be different.

**Did you make smart decisions about what to build vs. what to skip? Can you articulate
why?** 

One thing that i could think of is , we can scale it further by using a caching mechanism. The idea why should we invoke the rag pipline , it will use a lot of resources and tokens , instead we can invoke it for the first time , for eg. we can retrieve instructions and than stored them in a json file , so it will save a lot of time. 

**What would you do differently with 2 more weeks? What about 2 more months?**

I would first build a optimized rag pipeline that can support pre filtering , extracting sub queries and than i will work upon organizing the tax tables data , so that we can create a determinstic tool. Beacause the whole system is dependent on the context we are giving to LLM.




 
>>>>>>> master
