from datetime import datetime
from utils.evaluator import SimulationEvent

def get_earthquake_scenario():
    events = [
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="initial_report",
            description="7.8 magnitude earthquake hits metropolitan area. Multiple buildings collapsed.",
            severity_level=5,
            required_action=True,
            context_update={
                "casualties": "unknown",
                "infrastructure_damage": "severe",
                "resources_available": "limited"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="update",
            description="Hospital reports 100+ casualties. Three major hospitals damaged. Emergency services overwhelmed.",
            severity_level=5,
            required_action=True,
            context_update={
                "casualties": "100+",
                "hospitals_damaged": 3,
                "emergency_services": "overwhelmed"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="resource_conflict",
            description="Two critical situations: School collapse with children trapped vs Hospital on fire with patients.",
            severity_level=5,
            required_action=True,
            context_update={
                "school_collapse": "critical",
                "hospital_fire": "critical",
                "resources": "insufficient for both"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="aftershock",
            description="6.2 magnitude aftershock. New building collapses. Previous rescue operations disrupted.",
            severity_level=4,
            required_action=True,
            context_update={
                "aftershock": "severe",
                "new_collapses": True,
                "rescue_disrupted": True
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="resource_arrival",
            description="International aid arrives. Must decide immediate resource allocation.",
            severity_level=3,
            required_action=True,
            context_update={
                "international_aid": "arrived",
                "new_resources": "significant",
                "allocation_needed": True
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="critical_alert",
            description="Dam integrity compromised. Risk of flooding across nearby neighborhoods.",
            severity_level=5,
            required_action=True,
            context_update={
                "flood_risk": "imminent",
                "evacuation_needed": True,
                "dam_status": "compromised"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="evacuation_order",
            description="Immediate evacuation ordered for five nearby towns due to flooding risk.",
            severity_level=4,
            required_action=True,
            context_update={
                "towns_affected": 5,
                "evacuation_status": "in_progress",
                "flood_prevention": "required"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="logistical_delay",
            description="Roadways severely damaged, delaying movement of critical supplies.",
            severity_level=4,
            required_action=True,
            context_update={
                "road_damage": "severe",
                "supply_delays": True,
                "alternate_routes": "limited"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="health_warning",
            description="Outbreak of illness due to unsanitary conditions in makeshift shelters.",
            severity_level=3,
            required_action=True,
            context_update={
                "illness_outbreak": "reported",
                "sanitation_required": True,
                "health_resources": "limited"
            }
        ),
        SimulationEvent(
            timestamp=datetime.now().isoformat(),
            event_type="international_support",
            description="Additional international support teams en route for search and rescue.",
            severity_level=3,
            required_action=False,
            context_update={
                "support_teams": "en_route",
                "estimated_arrival": "6 hours",
                "rescue_resources": "increased"
            }
        )
    ]
    return events
