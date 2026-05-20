import appdaemon.plugins.hass.hassapi as hass


class BigmiRuntime(hass.Hass):
    """PoC runtime layer that turns HA helpers into a programmable automation hub."""

    def initialize(self):
        self.mode_entities = {
            "esports": self.args["esports_toggle"],
            "rental": self.args["rental_toggle"],
            "cinema": self.args["cinema_toggle"],
        }
        self.mode_activation_notes = {
            "esports": "High-performance low-latency room setup applied",
            "rental": "Rental-ready hospitality scene applied",
            "cinema": "Immersive cinema scene applied",
        }

        for mode_name, entity_id in self.mode_entities.items():
            self.listen_state(self._handle_mode_change, entity_id, mode=mode_name)

        self.listen_event(self._handle_program_event, "bigmi_activate_scene")

        self.log("Bigmi Runtime initialized and listening for scenario changes.")
        self._record_runtime(
            channel="appdaemon-bootstrap",
            action="AppDaemon runtime boot completed",
            payload="runtime=ready",
        )

    def _handle_mode_change(self, entity, attribute, old, new, kwargs):
        if old == new:
            return

        mode = kwargs["mode"]

        if new == "on":
            self.log(f"Activating {mode} mode from AppDaemon.")
            self._disable_other_modes(current_mode=mode)
            self.call_service(
                "script/turn_on",
                entity_id=f"script.bigmi_activate_{mode}_mode",
            )
            self._record_runtime(
                channel="appdaemon-state-listener",
                action=f"AppDaemon activated {mode} mode",
                payload=f"mode={mode} note={self.mode_activation_notes[mode]}",
            )
            self.call_service(
                "persistent_notification/create",
                title="Bigmi Runtime",
                message=f"{mode.title()} mode was activated by the AppDaemon runtime.",
            )
        elif new == "off":
            self.log(f"Deactivating {mode} mode from AppDaemon.")
            self.call_service(
                "script/turn_on",
                entity_id=f"script.bigmi_deactivate_{mode}_mode",
            )
            self._record_runtime(
                channel="appdaemon-state-listener",
                action=f"AppDaemon deactivated {mode} mode",
                payload=f"mode={mode} state=off",
            )

    def _handle_program_event(self, event_name, data, kwargs):
        mode = str(data.get("mode", "")).strip().lower()
        source = str(data.get("source", "unknown")).strip() or "unknown"
        note = str(data.get("note", "No note supplied")).strip() or "No note supplied"
        payload = data.get("payload", {})

        if mode not in self.mode_entities:
            self.log(
                f"Ignoring unsupported mode '{mode}' from source '{source}'.",
                level="WARNING",
            )
            self._record_runtime(
                channel=f"event:{source}",
                action=f"Rejected unsupported mode '{mode}'",
                payload=f"note={note}",
            )
            return

        if bool(data.get("requires_approval")) and self.get_state(
            "input_boolean.bigmi_safety_guard"
        ) == "on":
            self.turn_on("input_boolean.bigmi_sensitive_unlock_pending")
            self._record_runtime(
                channel=f"event:{source}",
                action=f"Program event for {mode} queued for approval",
                payload=f"note={note}",
            )
            return

        payload_text = self._payload_to_text(payload)
        self.log(
            f"Program event received from '{source}' for mode '{mode}' with note '{note}'."
        )
        self._record_runtime(
            channel=f"event:{source}",
            action=f"Program event accepted for {mode}",
            payload=f"note={note} {payload_text}".strip(),
        )
        self.turn_on(self.mode_entities[mode])

    def _disable_other_modes(self, current_mode):
        for mode_name, entity_id in self.mode_entities.items():
            if mode_name == current_mode:
                continue

            if self.get_state(entity_id) == "on":
                self.turn_off(entity_id)

    def _payload_to_text(self, payload):
        if isinstance(payload, dict):
            pairs = [f"{key}={value}" for key, value in payload.items()]
            return " ".join(pairs)
        if payload in (None, ""):
            return ""
        return str(payload)

    def _record_runtime(self, channel, action, payload):
        try:
            self.call_service(
                "input_text/set_value",
                entity_id="input_text.bigmi_last_runtime_action",
                value=action[:255],
            )
            self.call_service(
                "input_text/set_value",
                entity_id="input_text.bigmi_last_runtime_channel",
                value=channel[:255],
            )
            self.call_service(
                "input_text/set_value",
                entity_id="input_text.bigmi_last_program_payload",
                value=(payload or "none")[:255],
            )
        except Exception as err:
            # Home Assistant can briefly come up in recovery mode before helpers exist.
            self.log(
                f"Skipping runtime status write because helper entities are not ready yet: {err}",
                level="WARNING",
            )
