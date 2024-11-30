.PHONY: all
all: kinematics workspace singularities

.PHONY: kinematics
kinematics:
	@echo "Running kinematics simulation..."
	@python trossen/kinematics.py


.PHONY: workspace
workspace:
	@echo "Running workspace simulation..."
	@python trossen/workspace.py

.PHONY: singularities
singularities:
	@echo "Running singularities simulation..."
	@python trossen/singularities.py
