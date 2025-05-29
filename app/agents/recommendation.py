from crewai import Agent

def create_recommendation_agent():
    return Agent(
        role="Support Recommendation Agent",
        goal="Provide support approval or soft decline recommendation based on full applicant profile",
        backstory=(
            "An AI policy advisor trained on social support policies. "
            "Expert in evaluating eligibility based on income, credit, employment, and risk profiles."
        )
    )
