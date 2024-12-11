The system helps me research something.
I designe my system to be that will be one agent who does search engin to get list of website and I want agent or agent systems scrape information from each website and summarize and go through all the list of the website from the search and then collectively summarize again. So for this feature I have a lead summarizer who will issue one website at a time to an agent, a specific agent who is responsible for scrapping one that one particular given website, scrape it up and summarize. When it finishes job return to the lead summarizer and the lead summarizer will will go throuh the website one by one and when it finishes it will collect everything and summarize and give it back to a user proxy.

# Group chat

1. **User Proxy**: This component acts as the interface between the user and the agent-based system. It receives the user's research request and passes it on to the Agent Search module.

2. **Agent Search**: This agent is responsible for performing the initial search for relevant websites on the given topic. It queries search engines and compiles a list of potentially relevant websites.

3. **Agent Lead Summarizer**: The Lead Summarizer agent is in charge of coordinating the overall summarization process. It assigns each website from the search results to a dedicated Scrape & Summarize agent, and then aggregates the individual summaries into a final report for the User Proxy.

4. **Agent Scrape & Summarize**: These agents are responsible for scraping the content of a single assigned website and generating a summary of the key information. Once completed, they return the summary to the Lead Summarizer.

The workflow of the system is as follows:

1. The user submits a research request to the User Proxy.
2. The User Proxy forwards the request to the Agent Search module.
3. The Agent Search performs a web search and compiles a list of relevant websites.
4. The Agent Lead Summarizer receives the list of websites and assigns each one to a dedicated Scrape & Summarize agent.
5. The Scrape & Summarize agents retrieve the content of their assigned websites, analyze the information, and generate a summary.
6. The Scrape & Summarize agents return their individual summaries to the Lead Summarizer.
7. The Lead Summarizer collates all the summaries and generates a final comprehensive report.
8. The final report is returned to the User Proxy, which presents the information to the user.
