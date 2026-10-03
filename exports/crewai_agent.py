from crewai import Agent

sbom_reachability_mitigation_engine = Agent(
    role="Sbom Reachability Mitigation Engine",
    goal="Deliver high-precision autonomous Sbom Reachability Mitigation Engine operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
