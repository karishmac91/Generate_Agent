#from recommendation import create_recommendation_agent
from crewai import Crew, Task
from app.agents.recommendation import create_recommendation_agent
from app.merge.mergefeatures import get_applicant_features

def run_recommendation_pipeline(applicant_id):
    """
    Runs the recommendation pipeline for a given applicant.
    This function retrieves the features of the specified applicant, creates a recommendation agent,
    and defines a task for the agent to analyze the applicant's data. The agent determines whether
    the applicant should be approved or soft-declined for social support, providing a justification
    and confidence level. The task is executed within a crew, and the result is returned.
    Args:
        applicant_id (str or int): The unique identifier of the applicant whose data will be analyzed.
    Returns:
        Any: The result of the recommendation process, including the decision, justification, and confidence level.
    """
    features = get_applicant_features(applicant_id)

    recommendation_agent = create_recommendation_agent()

    task = Task(
        description=(
            f"Given the applicant data: {features}, "
            "analyze all fields and determine if the applicant should be approved or soft-declined for social support. "
            "Return a justification and confidence level."
        ),
        expected_output="Decision: Approve | Soft Decline + Reason",
        agent=recommendation_agent
    )

    crew = Crew(
        agents=[recommendation_agent],
        tasks=[task],
        verbose=True
    )

    result = crew.kickoff()
    return result
