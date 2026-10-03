# Duties and Responsibilities for SBOM Reachability Mitigation Engine Agent

## Dual-Control Architecture
Maker:
callgraph-traverser

Checker:
reachability-proof-checker

## Operational Workflow
1. The Maker (callgraph-traverser) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (reachability-proof-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
