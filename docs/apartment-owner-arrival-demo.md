# Bigmi Apartment Demo

这份文档描述的是一个“可编程空间程序”而不是一组孤立设备。

它最适合用来讲 proposal 里的四件事：

- `可编程`
- `高权限`
- `开发者友好`
- `小型空间运营场景`

## Apartment layout

The demo apartment contains six spaces plus a shared support layer:

- Entryway
- Living Room
- Kitchen
- Bedroom
- Bathroom
- Study
- Support Systems

## Devices by room

### Entryway

- Owner Home flag
- Entryway Light
- Entryway Air Freshener

### Living Room

- Living Room Curtain
- Living Room Ceiling Light
- Living Room Floor Lamp
- Living Room Air Conditioner
- Robot Vacuum Cleaning
- Gaming PC
- Ambient Strip
- Projector Power
- Guest Welcome Automation

### Kitchen

- Kitchen Pendant Light

### Bedroom

- Bedroom Curtain
- Bedroom Air Purifier
- Bedroom Bedside Lamp
- Bedroom Night Light

### Bathroom

- Bathroom Water Heater

### Study

- Study Desk Lamp
- Study Monitor
- Focus Mode

### Support Systems

- Medication Reminder
- Fall Sensor Guard
- Pet Feeder
- Pet Camera
- Guest Check-in Tablet
- Doorbell Mute
- White Noise Speaker
- Energy Saver Banner

## Scenario library

The apartment now exposes a reusable library of programmable programs:

1. `Owner Arrives Home`
2. `Elder Care Mode`
3. `Energy Saver Mode`
4. `Pet Mode`
5. `Rental Check-in Mode`
6. `Esports Room Mode`
7. `Cinema Room Mode`
8. `Quiet Night Mode`
9. `Work From Home Mode`

These are all implemented in:

- [house_program_demo.py](../appdaemon/conf/apps/house_program_demo.py)

## Example scenario: Owner Arrives Home

The arrival sequence is still the best “first demo” because it immediately shows staged orchestration across multiple rooms.

Its current sequence is:

1. Mark owner as home
2. Turn on the entryway light
3. Stop the robot vacuum
4. Open the living room curtain
5. Turn on the living room AC
6. Turn on the living room ceiling light
7. Turn on the living room floor lamp
8. Turn on the kitchen pendant light
9. Turn on the bathroom water heater
10. Turn on the bedroom air purifier
11. Turn on the study desk lamp

## What each scenario demonstrates

### Elder Care Mode

- Lights circulation paths
- Enables fall sensor guard
- Turns on medication reminders
- Prepares hot water
- Pauses the robot vacuum

This is the clearest demonstration of `高权限 + 安全可控 + 照护场景`.

### Energy Saver Mode

- Turns off unnecessary lights
- Stops cooling and hot water heating
- Powers down monitor, gaming PC, and projector
- Raises a visible saver banner

This shows Bigmi can optimize a whole apartment state, not just trigger single devices.

### Pet Mode

- Activates feeder and pet camera
- Keeps lighting and ventilation comfortable
- Pauses the vacuum
- Freshens the entryway

This is a good example of “人在外，系统还在替你照顾空间”。

### Rental Check-in Mode

- Enables rental host mode
- Turns on guest welcome automation
- Activates a check-in tablet
- Prepares climate, lighting, and hot water

This maps directly to proposal 里的 `民宿入住模式` 和 `小型空间运营`.

### Esports Room Mode

- Powers the gaming rig
- Turns on ambient lighting
- Enables focus mode
- Cools the room
- Mutes interruptions

This is one of the clearest “high value lifestyle space” demos for PPT.

### Cinema Room Mode

- Powers the projector
- Dims the room
- Mutes interruptions
- Keeps the room comfortable

This demonstrates atmosphere orchestration rather than simple device control.

### Quiet Night Mode

- Mutes the doorbell
- Turns on white noise
- Leaves only low-light navigation
- Stops noisy cleaning

This is a compact example of household policy automation.

### Work From Home Mode

- Powers the work monitor
- Lights the desk
- Enables focus mode
- Keeps the apartment comfortable
- Silences interruptions

This shows Bigmi can treat the apartment as a programmable productivity environment.

## Why this matters for Bigmi

### 1. It is a space-level program, not a single-device rule

The demo does not say:

- turn on one lamp

It says:

- when the owner arrives home, reshape the whole apartment state

That is much closer to Bigmi's product positioning.

### 2. It shows high privilege orchestration

One action affects:

- lighting
- curtain state
- climate control
- hot water
- cleaning workflow

This is why safety and audit are product requirements, not optional extras.

### 3. It is easy for advanced users to modify

The script is intentionally structured around:

- `ROOMS`
- `PROGRAMS`
- ordered `steps`

So a power user can customize the apartment without needing to understand the whole runtime.

### 4. It maps well to small-space operators

The same script structure can later represent:

- rental check-in
- office open / close
- movie room preparation
- esports room startup
- cleaning turnover between guests

## How to run it

1. Open `Bigmi Console -> Apartment`
2. Click `Reset Apartment`
3. Click any scenario in `Scenario Library`
4. Watch the room tiles change one by one
5. Repeat with another scenario to show that the same apartment supports many programmable behaviors

## How advanced users can customize it

Edit the following sections in `house_program_demo.py`:

- `ROOMS`
  Add or rename rooms and attach device entities.
- `PROGRAMS`
  Define new programs like `movie_night`, `leave_for_work`, or `guest_mode`.
- `PROGRAMS["owner_arrives_home"]["steps"]`
  Reorder or replace actions to match another apartment layout.
- `PROGRAMS["elder_care_mode"]["steps"]`
  Rework the care policy, reminders, or assisted-living devices.
- `PROGRAMS["rental_checkin_mode"]["steps"]`
  Adapt the check-in flow for different properties or guest tiers.

Each step has:

- `room`
- `entity_id`
- `state`
- `note`

That makes the script easy to understand and extend without rewriting the whole runtime.

## Suggested PPT narration

You can describe this page in three short beats:

1. `This is not a control panel for one brand of devices.`
2. `This is a programmable apartment object with room-aware scenario programs.`
3. `Advanced users can rewrite any mode by editing a readable program instead of rebuilding the system from scratch.`
