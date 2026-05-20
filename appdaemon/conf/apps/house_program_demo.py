import appdaemon.plugins.hass.hassapi as hass


class BigmiHouseProgramDemo(hass.Hass):
    """Programmable apartment demo built for easy extension by advanced users."""

    ROOMS = {
        "entryway": {
            "devices": [
                "input_boolean.bigmi_owner_home",
                "input_boolean.bigmi_entryway_light",
                "input_boolean.bigmi_entryway_air_freshener",
            ],
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
                "input_boolean.bigmi_bedroom_night_light",
            ],
            "label": "Bedroom",
        },
        "bathroom": {
            "devices": ["input_boolean.bigmi_bathroom_water_heater"],
            "label": "Bathroom",
        },
        "study": {
            "devices": [
                "input_boolean.bigmi_study_desk_lamp",
                "input_boolean.bigmi_study_monitor",
                "input_boolean.bigmi_focus_mode",
            ],
            "label": "Study",
        },
        "support": {
            "devices": [
                "input_boolean.bigmi_medication_reminder",
                "input_boolean.bigmi_fall_sensor_guard",
                "input_boolean.bigmi_pet_feeder",
                "input_boolean.bigmi_pet_camera",
                "input_boolean.bigmi_guest_checkin_tablet",
                "input_boolean.bigmi_doorbell_mute",
                "input_boolean.bigmi_white_noise",
                "input_boolean.bigmi_energy_saver_banner",
            ],
            "label": "Support Systems",
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
                    "room": "support",
                    "entity_id": "input_boolean.bigmi_energy_saver_banner",
                    "state": "off",
                    "note": "Clear the energy saver status banner.",
                },
                {
                    "room": "support",
                    "entity_id": "input_boolean.bigmi_white_noise",
                    "state": "off",
                    "note": "Mute night ambience.",
                },
                {
                    "room": "support",
                    "entity_id": "input_boolean.bigmi_doorbell_mute",
                    "state": "off",
                    "note": "Restore normal doorbell behavior.",
                },
                {
                    "room": "support",
                    "entity_id": "input_boolean.bigmi_guest_checkin_tablet",
                    "state": "off",
                    "note": "Hide the guest check-in screen.",
                },
                {
                    "room": "support",
                    "entity_id": "input_boolean.bigmi_pet_camera",
                    "state": "off",
                    "note": "Return pet monitoring to idle state.",
                },
                {
                    "room": "support",
                    "entity_id": "input_boolean.bigmi_pet_feeder",
                    "state": "off",
                    "note": "Reset the feeder state.",
                },
                {
                    "room": "support",
                    "entity_id": "input_boolean.bigmi_fall_sensor_guard",
                    "state": "off",
                    "note": "Clear elder care guard mode.",
                },
                {
                    "room": "support",
                    "entity_id": "input_boolean.bigmi_medication_reminder",
                    "state": "off",
                    "note": "Clear reminder indicators.",
                },
                {
                    "room": "study",
                    "entity_id": "input_boolean.bigmi_focus_mode",
                    "state": "off",
                    "note": "Clear focus workflows.",
                },
                {
                    "room": "study",
                    "entity_id": "input_boolean.bigmi_study_monitor",
                    "state": "off",
                    "note": "Turn off the study monitor.",
                },
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
                    "entity_id": "input_boolean.bigmi_bedroom_night_light",
                    "state": "off",
                    "note": "Switch off the night light.",
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
                    "entity_id": "input_boolean.bigmi_entryway_air_freshener",
                    "state": "off",
                    "note": "Switch off entryway freshness effects.",
                },
                {
                    "room": "entryway",
                    "entity_id": "input_boolean.bigmi_owner_home",
                    "state": "off",
                    "note": "Mark the owner as away again.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_pc_power",
                    "state": "off",
                    "note": "Turn off the gaming PC state.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_ambient_strip",
                    "state": "off",
                    "note": "Reset accent lighting from esports or cinema mode.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_projector_power",
                    "state": "off",
                    "note": "Turn off the projector state.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_guest_welcome",
                    "state": "off",
                    "note": "Clear guest welcome state.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_esports_mode",
                    "state": "off",
                    "note": "Clear esports room mode status.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_rental_mode",
                    "state": "off",
                    "note": "Clear rental host mode status.",
                },
                {
                    "room": "living_room",
                    "entity_id": "input_boolean.bigmi_cinema_mode",
                    "state": "off",
                    "note": "Clear cinema room mode status.",
                },
            ],
            "final_status": "Apartment reset and ready for another arrival demo",
        },
        "elder_care_mode": {
            "title": "Elder Care Mode",
            "status": "Running elder care support sequence",
            "steps": [
                {"room": "entryway", "entity_id": "input_boolean.bigmi_owner_home", "state": "on", "note": "Keep the apartment marked as occupied."},
                {"room": "entryway", "entity_id": "input_boolean.bigmi_entryway_light", "state": "on", "note": "Keep circulation paths brightly lit."},
                {"room": "bedroom", "entity_id": "input_boolean.bigmi_bedroom_night_light", "state": "on", "note": "Reduce trip risk at night."},
                {"room": "support", "entity_id": "input_boolean.bigmi_fall_sensor_guard", "state": "on", "note": "Enable extra monitoring for fall response."},
                {"room": "support", "entity_id": "input_boolean.bigmi_medication_reminder", "state": "on", "note": "Turn on medicine reminders."},
                {"room": "bathroom", "entity_id": "input_boolean.bigmi_bathroom_water_heater", "state": "on", "note": "Prepare hot water early for comfort and safety."},
                {"room": "bedroom", "entity_id": "input_boolean.bigmi_bedroom_air_purifier", "state": "on", "note": "Keep bedroom air quality steady."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_robot_vacuum_cleaning", "state": "off", "note": "Pause cleaning to avoid obstacles and noise."},
            ],
            "final_status": "Elder care mode activated",
        },
        "energy_saver_mode": {
            "title": "Energy Saver Mode",
            "status": "Running energy saver sequence",
            "steps": [
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_ceiling_light", "state": "off", "note": "Cut unnecessary lighting load."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_floor_lamp", "state": "off", "note": "Switch off accent lighting."},
                {"room": "kitchen", "entity_id": "input_boolean.bigmi_kitchen_pendant_light", "state": "off", "note": "Turn off kitchen lighting."},
                {"room": "study", "entity_id": "input_boolean.bigmi_study_desk_lamp", "state": "off", "note": "Turn off work lighting."},
                {"room": "study", "entity_id": "input_boolean.bigmi_study_monitor", "state": "off", "note": "Switch off monitor standby draw."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_ac", "state": "off", "note": "Stop cooling when the room is idle."},
                {"room": "bathroom", "entity_id": "input_boolean.bigmi_bathroom_water_heater", "state": "off", "note": "Avoid background heating cost."},
                {"room": "bedroom", "entity_id": "input_boolean.bigmi_bedroom_air_purifier", "state": "off", "note": "Pause air purifier during saver mode."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_pc_power", "state": "off", "note": "Make sure gaming hardware is shut down."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_projector_power", "state": "off", "note": "Avoid projector standby power."},
                {"room": "support", "entity_id": "input_boolean.bigmi_energy_saver_banner", "state": "on", "note": "Surface the apartment-wide energy saver state."},
            ],
            "final_status": "Energy saver mode activated",
        },
        "pet_mode": {
            "title": "Pet Mode",
            "status": "Running pet comfort sequence",
            "steps": [
                {"room": "support", "entity_id": "input_boolean.bigmi_pet_feeder", "state": "on", "note": "Prepare the scheduled feeding flow."},
                {"room": "support", "entity_id": "input_boolean.bigmi_pet_camera", "state": "on", "note": "Enable pet monitoring for remote check-ins."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_curtain", "state": "on", "note": "Let daylight in while pets stay home."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_floor_lamp", "state": "on", "note": "Keep the room softly lit for pets."},
                {"room": "bedroom", "entity_id": "input_boolean.bigmi_bedroom_air_purifier", "state": "on", "note": "Improve air quality around pet areas."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_robot_vacuum_cleaning", "state": "off", "note": "Avoid stressing pets with vacuum noise."},
                {"room": "entryway", "entity_id": "input_boolean.bigmi_entryway_air_freshener", "state": "on", "note": "Freshen the space during longer pet stays."},
            ],
            "final_status": "Pet mode activated",
        },
        "rental_checkin_mode": {
            "title": "Rental Check-in Mode",
            "status": "Running rental check-in sequence",
            "steps": [
                {"room": "living_room", "entity_id": "input_boolean.bigmi_rental_mode", "state": "on", "note": "Mark the apartment as running rental host mode."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_guest_welcome", "state": "on", "note": "Enable welcome workflows."},
                {"room": "support", "entity_id": "input_boolean.bigmi_guest_checkin_tablet", "state": "on", "note": "Present check-in instructions to guests."},
                {"room": "entryway", "entity_id": "input_boolean.bigmi_entryway_light", "state": "on", "note": "Light the first guest touchpoint."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_ac", "state": "on", "note": "Set a comfortable arrival climate."},
                {"room": "kitchen", "entity_id": "input_boolean.bigmi_kitchen_pendant_light", "state": "on", "note": "Illuminate the shared prep area."},
                {"room": "bedroom", "entity_id": "input_boolean.bigmi_bedroom_bedside_lamp", "state": "on", "note": "Create a welcoming bedroom scene."},
                {"room": "bathroom", "entity_id": "input_boolean.bigmi_bathroom_water_heater", "state": "on", "note": "Prepare hot water for arriving guests."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_robot_vacuum_cleaning", "state": "off", "note": "Keep the unit quiet and tidy during check-in."},
            ],
            "final_status": "Rental check-in mode activated",
        },
        "esports_room_mode": {
            "title": "Esports Room Mode",
            "status": "Running esports room sequence",
            "steps": [
                {"room": "living_room", "entity_id": "input_boolean.bigmi_esports_mode", "state": "on", "note": "Mark the apartment as running esports mode."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_pc_power", "state": "on", "note": "Power the gaming rig."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_ambient_strip", "state": "on", "note": "Turn on reactive ambient lighting."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_ac", "state": "on", "note": "Keep the room cool under load."},
                {"room": "study", "entity_id": "input_boolean.bigmi_study_monitor", "state": "on", "note": "Use the monitor for stats or streaming."},
                {"room": "study", "entity_id": "input_boolean.bigmi_focus_mode", "state": "on", "note": "Reduce distractions during matches."},
                {"room": "support", "entity_id": "input_boolean.bigmi_doorbell_mute", "state": "on", "note": "Mute interruptions while gaming."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_robot_vacuum_cleaning", "state": "off", "note": "Keep the room quiet for voice comms."},
            ],
            "final_status": "Esports room mode activated",
        },
        "cinema_room_mode": {
            "title": "Cinema Room Mode",
            "status": "Running cinema room sequence",
            "steps": [
                {"room": "living_room", "entity_id": "input_boolean.bigmi_cinema_mode", "state": "on", "note": "Mark the apartment as running cinema mode."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_projector_power", "state": "on", "note": "Power up the projector."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_ambient_strip", "state": "on", "note": "Set cinematic accent lighting."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_curtain", "state": "off", "note": "Close the curtain to darken the room."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_ceiling_light", "state": "off", "note": "Switch off the main ceiling light."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_floor_lamp", "state": "off", "note": "Switch off accent lamps near the screen."},
                {"room": "support", "entity_id": "input_boolean.bigmi_doorbell_mute", "state": "on", "note": "Mute interruptions during the movie."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_ac", "state": "on", "note": "Keep the room comfortable during viewing."},
            ],
            "final_status": "Cinema room mode activated",
        },
        "quiet_night_mode": {
            "title": "Quiet Night Mode",
            "status": "Running quiet night sequence",
            "steps": [
                {"room": "support", "entity_id": "input_boolean.bigmi_doorbell_mute", "state": "on", "note": "Silence night interruptions."},
                {"room": "support", "entity_id": "input_boolean.bigmi_white_noise", "state": "on", "note": "Turn on soft white noise."},
                {"room": "bedroom", "entity_id": "input_boolean.bigmi_bedroom_night_light", "state": "on", "note": "Leave a minimal night path light on."},
                {"room": "bedroom", "entity_id": "input_boolean.bigmi_bedroom_bedside_lamp", "state": "off", "note": "Switch off brighter bedside lighting."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_ceiling_light", "state": "off", "note": "Darken the main common space."},
                {"room": "kitchen", "entity_id": "input_boolean.bigmi_kitchen_pendant_light", "state": "off", "note": "Switch off kitchen lighting."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_robot_vacuum_cleaning", "state": "off", "note": "Prevent cleaning noise overnight."},
                {"room": "study", "entity_id": "input_boolean.bigmi_focus_mode", "state": "off", "note": "End workday focus automation."},
            ],
            "final_status": "Quiet night mode activated",
        },
        "work_from_home_mode": {
            "title": "Work From Home Mode",
            "status": "Running work from home sequence",
            "steps": [
                {"room": "entryway", "entity_id": "input_boolean.bigmi_owner_home", "state": "on", "note": "Mark the apartment as occupied for daytime routines."},
                {"room": "study", "entity_id": "input_boolean.bigmi_study_monitor", "state": "on", "note": "Power the main work monitor."},
                {"room": "study", "entity_id": "input_boolean.bigmi_study_desk_lamp", "state": "on", "note": "Light the desk for long work sessions."},
                {"room": "study", "entity_id": "input_boolean.bigmi_focus_mode", "state": "on", "note": "Reduce interruptions and enable work focus."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_living_room_ac", "state": "on", "note": "Keep the apartment comfortable during work hours."},
                {"room": "kitchen", "entity_id": "input_boolean.bigmi_kitchen_pendant_light", "state": "on", "note": "Prepare the kitchen for coffee or lunch."},
                {"room": "support", "entity_id": "input_boolean.bigmi_doorbell_mute", "state": "on", "note": "Silence interruptions during calls."},
                {"room": "living_room", "entity_id": "input_boolean.bigmi_robot_vacuum_cleaning", "state": "off", "note": "Pause cleaning during meetings."},
            ],
            "final_status": "Work from home mode activated",
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
