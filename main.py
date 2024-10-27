import asyncio
import json
import os
from dotenv import load_dotenv
import anthropic
from scenarios.natural_disaster import get_earthquake_scenario
from scenarios.medical_triage import get_medical_scenario
from scenarios.infrastructure_crisis import get_infrastructure_scenario
from utils.evaluator import StressSimulation

async def run_evaluations():
    load_dotenv()
    print(os.getenv('ANTHROPIC_API_KEY'))
    client = anthropic.Client(os.getenv('ANTHROPIC_API_KEY'))
    
    # Run earthquake scenario
    earthquake_sim = StressSimulation("Earthquake Response", client)
    for event in get_earthquake_scenario():
        earthquake_sim.add_event(event)
    
    earthquake_results = await earthquake_sim.run_simulation()
    
    # Print results
    print("\nEarthquake Scenario Results:")
    print(f"Average Response Time: {earthquake_results['metrics']['avg_response_time']:.2f} seconds")
    print(f"Average Safety Score: {earthquake_results['metrics']['avg_safety']:.2f}")
    print(f"Average Ethical Alignment: {earthquake_results['metrics']['avg_ethics']:.2f}")
    
    # Save results
    with open("earthquake_results.json", "w") as f:
        json.dump(earthquake_results, f, indent=2, default=str)

if __name__ == "__main__":
    asyncio.run(run_evaluations())

from utils.evaluator import ComparativeStressSimulation

async def run_comparative_evaluations():
    # Run earthquake scenario across all models
    earthquake_sim = ComparativeStressSimulation("Earthquake Response")
    for event in get_earthquake_scenario():
        earthquake_sim.add_event(event)
    
    results = await earthquake_sim.run_comparative_simulation()
    
    # Print comparative results
    print("\nComparative Results:")
    for model_name, model_results in results["model_results"].items():
        print(f"\n{model_name.upper()} Results:")
        metrics = model_results["metrics"]
        print(f"Average Response Time: {metrics['avg_response_time']:.2f} seconds")
        print(f"Average Safety Score: {metrics['avg_safety']:.2f}")
        print(f"Average Ethical Alignment: {metrics['avg_ethics']:.2f}")
    
    # Save results
    with open("comparative_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)

if __name__ == "__main__":
    asyncio.run(run_comparative_evaluations())