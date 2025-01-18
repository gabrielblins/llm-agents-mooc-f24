#!/usr/bin/env python
import sys
import warnings

from quality_monitoring.crew import QualityMonitoring

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # inputs = {
    #     'topic': 'AI LLMs'
    # }
    # QualityMonitoring().crew().kickoff(inputs=inputs)
    # Prepare inputs for the crew

    # Example service transcript
    service_transcript = """
    Customer: I'm having issues with my recent purchase.
    Operator: I'm sorry to hear that. Can you tell me more about the problem?
    Customer: The product I received is damaged.
    Operator: I understand. I'll help you process a return and send a replacement right away.
    Customer: Thank you for your help.
    Operator: You're welcome. Is there anything else I can assist you with today?
    Customer: No just this. Thank you.
    """

    # Example service guidelines
    service_guidelines = [
        "Greet the customer warmly",
        "Listen actively and show empathy",
        "Provide clear and helpful solutions",
        "Confirm customer satisfaction",
        "Offer additional assistance"
    ]

    # # Initialize and run the quality analysis
    # quality_analysis_crew = QualityMonitoring()
    # feedback_report = quality_analysis_crew.run(
    #     service_transcript, 
    #     service_guidelines
    # )
    
    # Print the final feedback report
    #print(feedback_report)
    
    inputs = {
        'transcript': service_transcript,
        'guidelines': service_guidelines
    }
    
    # Kick off the crew
    return QualityMonitoring().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        QualityMonitoring().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        QualityMonitoring().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        QualityMonitoring().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
