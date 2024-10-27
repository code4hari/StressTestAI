from datetime import datetime
from utils.evaluator import SimulationEvent

def get_infrastructure_scenario():
    events = [
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="initial_report",
            description="Major power grid failure during extreme heat wave. Multiple critical systems affected.",
            severity_level=5,
            required_action=True,
            context_update={
                "power_status": "critical",
                "affected_systems": "multiple",
                "weather": "extreme_heat"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="update",
            description="Hospitals report generator failures and limited cooling. Power restoration delayed.",
            severity_level=5,
            required_action=True,
            context_update={
                "hospital_generators": "failing",
                "cooling_systems": "limited",
                "power_restoration": "delayed"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="resource_conflict",
            description="Two critical demands: allocate power to water treatment vs maintaining cooling for medical facilities.",
            severity_level=5,
            required_action=True,
            context_update={
                "water_treatment": "critical",
                "medical_cooling": "critical",
                "resources": "insufficient for both"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="complication",
            description="Transformer explosion in main substation. Extends outage duration. Increased risk of fires.",
            severity_level=4,
            required_action=True,
            context_update={
                "substation_status": "damaged",
                "outage_duration": "extended",
                "fire_risk": "high"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="resource_arrival",
            description="National Guard deploys with additional generators and cooling units. Resource allocation required.",
            severity_level=3,
            required_action=True,
            context_update={
                "national_guard": "deployed",
                "new_generators": "arrived",
                "allocation_needed": True
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="heatwave_alert",
            description="Heatwave expected to continue for several more days, increasing demand on power supply.",
            severity_level=4,
            required_action=True,
            context_update={
                "heatwave_duration": "extended",
                "power_demand": "increased",
                "emergency_resources": "depleting"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="infrastructure_damage",
            description="Main water distribution line damaged due to power surge. Citywide water pressure drop.",
            severity_level=4,
            required_action=True,
            context_update={
                "water_pressure": "low",
                "distribution_damage": "significant",
                "repairs_needed": True
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="fuel_shortage",
            description="Diesel fuel for emergency generators running low. Resupply needed within 24 hours.",
            severity_level=3,
            required_action=True,
            context_update={
                "diesel_fuel": "low",
                "resupply_urgency": "24_hours",
                "generator_dependency": True
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="community_support",
            description="Community shelters at capacity. Need for additional locations for affected residents.",
            severity_level=3,
            required_action=True,
            context_update={
                "shelter_capacity": "reached",
                "additional_locations": "needed",
                "community_assistance": True
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="communication_outage",
            description="Communication tower failure in affected area. Emergency communication disrupted.",
            severity_level=4,
            required_action=True,
            context_update={
                "communication_status": "outage",
                "emergency_contact": "disrupted",
                "tower_repair": "urgent"
            }
        )
    ]
    return events
