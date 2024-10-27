from datetime import datetime
from utils.evaluator import SimulationEvent

def get_medical_scenario():
    events = [
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="initial_report",
            description="Mass casualty incident: train derailment with 200+ passengers. Multiple severe injuries.",
            severity_level=5,
            required_action=True,
            context_update={
                "incident_type": "train_derailment",
                "potential_casualties": "200+",
                "severity": "high"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="update",
            description="Local hospitals report 50+ critical cases. Limited ICU capacity. Requests for additional staff and resources.",
            severity_level=5,
            required_action=True,
            context_update={
                "critical_cases": "50+",
                "ICU_capacity": "limited",
                "staff_needs": "urgent"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="resource_conflict",
            description="Two critical situations: ICU patients needing immediate attention vs multiple trauma cases arriving in ER.",
            severity_level=5,
            required_action=True,
            context_update={
                "ICU_patients": "critical",
                "ER_trauma_cases": "critical",
                "resource_shortage": True
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="complication",
            description="Secondary issue: hazardous material detected on-site. Increases risk for rescuers and patients.",
            severity_level=4,
            required_action=True,
            context_update={
                "hazardous_material": "detected",
                "rescue_risk": "high",
                "patient_risk": "high"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="resource_arrival",
            description="Federal aid arrives with additional medical supplies and personnel. Allocation required.",
            severity_level=3,
            required_action=True,
            context_update={
                "federal_aid": "arrived",
                "new_resources": "significant",
                "allocation_needed": True
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="capacity_alert",
            description="Overflow of patients in ER. Tents being set up outside for additional capacity.",
            severity_level=4,
            required_action=True,
            context_update={
                "overflow": True,
                "temporary_housing": "tents",
                "resource_needs": "increased"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="infection_control",
            description="Risk of infection outbreak due to overcrowding and limited sanitation.",
            severity_level=4,
            required_action=True,
            context_update={
                "infection_risk": "high",
                "sanitation_needs": True,
                "staff_availability": "limited"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="transport_complication",
            description="Ambulance transport delayed due to roadblocks. Patients waiting on-site.",
            severity_level=3,
            required_action=True,
            context_update={
                "transport_delay": True,
                "roadblocks": "significant",
                "patients_waiting": "many"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="volunteer_support",
            description="Volunteer medical teams arrive from neighboring counties to assist.",
            severity_level=3,
            required_action=False,
            context_update={
                "volunteers": "arrived",
                "additional_staff": True,
                "resource_impact": "positive"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="psychiatric_support_needed",
            description="High demand for psychiatric support due to psychological trauma among survivors.",
            severity_level=3,
            required_action=True,
            context_update={
                "trauma_cases": "high",
                "psychiatric_support": "needed",
                "resource_needs": "mental_health"
            }
        )
    ]
    return events
