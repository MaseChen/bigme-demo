import appdaemon.plugins.hass.hassapi as hass


class BigmiHouseProgramDemo(hass.Hass):
    """Programmable apartment demo built for easy extension by advanced users."""

    ROOMS = {
        "entryway": {
            "devices": ["input_boolean.bigmi_owner_home", "input_boolean.bigmi_entryway_light"],
            "label": "Entryway",
        },
        "living_room": {
            "devices": [
                "input_boolean.bigmi_living_room_curtain",
                "input_boolean.bigmi_living_room_ceiling_light",
                "input_boolean.bigmi_living_room_floor_lamp",
                "input_boolean.bigmi_living_room_ac",
                "input_boolean.bigmi_robot_vacuum_cleaning",
            ],
            "label": "Living Room",
        },
        "kitchen": {
            "devices": ["input_boolean.bigmi_kitchen_pendant_light"],
            "label": "Kitchen",
        },
        "bedroom": {
            "devices": [
                "input_boolean.bigmi_bedroom_curtain",
                "input_boolean.bigmi_bedroom_air_purifier",
                "input_boolean.bigmi_bedroom_bedside_lamp",
            ],
            "label": "Bedroom",
        },
        "bathroom": {
            "devices": ["input_boolean.bigmi_bathroom_water_heater"],
            "label": "Bathroom",
        },
        "study": {
            "devices": ["input_boolean.bigmi_study_desk_lamp"],
            "label": "Study",
        },
    }

    PROGRAMS = {
        "owner_arrives_home": {
            "title": "Owner Arrives Home",
            "status": "Running owner arrival sequence",
            "steps": [
                {
                    "room": "entryway",
                    "entity_id": "input_boolean.bigmi_owner_home",
                    "state": "on",
                    "note": "Mark the owner as home so dependent logic can start.",
                },
                {
                    "room": "entryway",
                    "entity_id": "input_boolean.bigmi_entryway_light",
                    "state": "on",
                    "note": "Light the entry path as soon as the owner steps in.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_robot_vacuum_cleaning",
                    "state": "off",
                    "note": "Pause cleaning so the floor is quiet and clear.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_living_room_curtain",
                    "state": "on",
                    "note": "Open the curtain to bring daylight into the main space.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_living_room_ac",
                    "state": "on",
                    "note": "Pre-cool the living room for comfort.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_living_room_ceiling_light",
                    "state": "on",
                    "note": "Turn on the main living room light for immediate visibility.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_living_room_floor_lamp",
                    "state": "on",
                    "note": "Add a warmer accent light for a relaxed atmosphere.",
                },
                {
                    "room": "kitchen",
                    "entity_id": "input_boolean.bigmi_kitchen_pendant_light",
                    "state": "on",
                    "note": "Light the kitchen island for unpacking groceries or preparing tea.",
                },
                {
                    "room": "bathroom",
                    "entity_id": "input_boolean.bigmi_bathroom_water_heater",
                    "state": "on",
                    "note": "Start the water heater so a shower is ready later.",
                },
                {
                    "room": "bedroom",
                    "entity_id": "input_boolean.bigmi_bedroom_air_purifier",
                    "state": "on",
                    "note": "Refresh bedroom air quality in the background.",
                },
                {
                    "room": "study",
                    "entity_id": "input_boolean.bigmi_study_desk_lamp",
                    "state": "on",
                    "note": "Prepare the study corner in case the owner keeps working.",
                },
            ],
            "final_status": "Owner arrival program completed",
        },
        "reset_apartment_demo": {
            "title": "Reset Apartment Demo",
            "status": "Resetting apartment to pre-arrival state",
            "steps": [
                {
                    "room": "study",
                    "entity_id": "input_boolean.bigmi_study_desk_lamp",
                    "state": "off",
                    "note": "Clear the study state.",
                },
                {
                    "room": "bathroom",
                    "entity_id": "input_boolean.bigmi_bathroom_water_heater",
                    "state": "off",
                    "note": "Turn off the water heater for the next demo run.",
                },
                {
                    "room": "bedroom",
                    "entity_id": "input_boolean.bigmi_bedroom_air_purifier",
                    "state": "off",
                    "note": "Reset bedroom environment devices.",
                },
                {
                    "room": "bedroom",
                    "entity_id": "input_boolean.bigmi_bedroom_bedside_lamp",
                    "state": "off",
                    "note": "Reset bedroom lighting.",
                },
                {
                    "room": "bedroom",
                    "entity_id": "input_boolean.bigmi_bedroom_curtain",
                    "state": "off",
                    "note": "Close the bedroom curtain for a fresh start.",
                },
                {
                    "room": "kitchen",
                    "entity_id": "input_boolean.bigmi_kitchen_pendant_light",
                    "state": "off",
                    "note": "Switch off the kitchen light.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_living_room_floor_lamp",
                    "state": "off",
                    "note": "Reset the accent light.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_living_room_ceiling_light",
                    "state": "off",
                    "note": "Reset the main living room light.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_living_room_ac",
                    "state": "off",
                    "note": "Switch off climate control.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_living_room_curtain",
                    "state": "off",
                    "note": "Close the living room curtain again.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_robot_vacuum_cleaning",
                    "state": "on",
                    "note": "Resume vacuuming so the arrival program has something to stop.",
                },
                {
                    "room": "entryway",
                    "entity_id": "input_boolean.bigmi_entryway_light",
                    "state": "off",
                    "note": "Reset the entryway light.",
                },
                {
                    "room": "entryway",
                    "entity_id": "input_boolean.bigmi_owner_home",
                    "state": "off",
                    "note": "Mark the owner as away again.",
                },
            ],
            "final_status": "Apartment reset and ready for another arrival demo",
        },
    }

    def initialize(self):
        self.listen_event(self._handle_program_event, "bigmi_run_house_program")
        self._write_status("Apartment programmer ready")
        self._write_last_room("none")
        self.log("Bigmi house program demo initialized.")

    def _handle_program_event(self, event_name, data, kwargs):
        program_name = str(data.get("program", "")).strip()
        source = str(data.get("source", "unknown")).strip() or "unknown"
        note = str(data.get("note", "")).strip() or "No note supplied"
        program = self.PROGRAMS.get(program_name)

        if not program:
            self.log(f"Unknown house program '{program_name}' from '{source}'.", level="WARNING")
            self._write_runtime(
                action=f"Rejected unknown house program {program_name}",
                channel=f"house-program:{source}",
                payload=f"note={note}",
            )
            return

        steps = program["steps"]
        self.log(
            f"Launching house program '{program_name}' from '{source}' with {len(steps)} steps."
        )
        self._write_status(program["status"])
        self._write_runtime(
            action=f"House program launched: {program['title']}",
            channel=f"house-program:{source}",
            payload=f"program={program_name} note={note}",
        )

        for index, step in enumerate(steps):
            self.run_in(
                self._execute_step,
                index,
                program_name=program_name,
                source=source,
                step=step,
                step_number=index + 1,
                total_steps=len(steps),
            )

        self.run_in(
            self._finish_program,
            len(steps) + 1,
            program_name=program_name,
            source=source,
        )

    def _execute_step(self, kwargs):
        step = kwargs["step"]
        entity_id = step["entity_id"]
        target_state = step["state"]
        room_key = step["room"]
        room_label = self.ROOMS[room_key]["label"]
        step_number = kwargs["step_number"]
        total_steps = kwargs["total_steps"]
        service = "turn_on" if target_state == "on" else "turn_off"

        self.call_service(f"input_boolean/{service}", entity_id=entity_id)
        self._write_last_room(room_label)
        self._write_status(f"{kwargs['program_name']} step {step_number}/{total_steps}: {room_label}")
        self._write_runtime(
            action=f"{kwargs['program_name']} -> {entity_id} {target_state}",
            channel=f"house-program:{kwargs['source']}",
            payload=step["note"],
        )

    def _finish_program(self, kwargs):
        program = self.PROGRAMS[kwargs["program_name"]]
        final_status = program["final_status"]
        self._write_status(final_status)
        self._write_runtime(
            action=final_status,
            channel=f"house-program:{kwargs['source']}",
            payload=f"program={kwargs['program_name']}",
        )
        self.call_service(
            "persistent_notification/create",
            title="Bigmi House Program",
            message=f"{program['title']} finished through the programmable house demo.",
        )

    def _write_status(self, value):
        self._safe_write_text("input_text.bigmi_house_program_status", value)

    def _write_last_room(self, value):
        self._safe_write_text("input_text.bigmi_last_room_touched", value)

    def _write_runtime(self, action, channel, payload):
        self._safe_write_text("input_text.bigmi_last_runtime_action", action)
        self._safe_write_text("input_text.bigmi_last_runtime_channel", channel)
        self._safe_write_text("input_text.bigmi_last_program_payload", payload or "none")

    def _safe_write_text(self, entity_id, value):
        try:
            self.call_service(
                "input_text/set_value",
                entity_id=entity_id,
                value=str(value)[:255],
            )
        except Exception as err:
            self.log(
                f"Skipping write to {entity_id} because the helper is not ready yet: {err}",
                level="WARNING",
            )
