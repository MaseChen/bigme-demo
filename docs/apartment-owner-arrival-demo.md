# Bigmi Apartment Demo

这份文档描述的是一个“可编程空间程序”而不是一组孤立设备。

它最适合用来讲 proposal 里的四件事：

- `可编程`
- `高权限`
- `开发者友好`
- `小型空间运营场景`

## Apartment layout

The demo apartment contains six spaces:

- Entryway
- Living Room
- Kitchen
- Bedroom
- Bathroom
- Study

## Devices by room

### Entryway

- Owner Home flag
- Entryway Light

### Living Room

- Living Room Curtain
- Living Room Ceiling Light
- Living Room Floor Lamp
- Living Room Air Conditioner
- Robot Vacuum Cleaning

### Kitchen

- Kitchen Pendant Light

### Bedroom

- Bedroom Curtain
- Bedroom Air Purifier
- Bedroom Bedside Lamp

### Bathroom

- Bathroom Water Heater

### Study

- Study Desk Lamp

## Main scenario: Owner Arrives Home

This program is implemented in:

- [house_program_demo.py](/Users/jarason/Documents/code/bigme-demo/appdaemon/conf/apps/house_program_demo.py)

The current sequence is:

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
3. Click `Owner Arrives Home`
4. Watch the room tiles change one by one

## How advanced users can customize it

Edit the following sections in `house_program_demo.py`:

- `ROOMS`
  Add or rename rooms and attach device entities.
- `PROGRAMS`
  Define new programs like `movie_night`, `leave_for_work`, or `guest_mode`.
- `PROGRAMS["owner_arrives_home"]["steps"]`
  Reorder or replace actions to match another apartment layout.

Each step has:

- `room`
- `entity_id`
- `state`
- `note`

That makes the script easy to understand and extend without rewriting the whole runtime.

## Suggested PPT narration

You can describe this page in three short beats:

1. `This is not a control panel for one brand of devices.`
2. `This is a programmable apartment object with room-aware automation.`
3. `Advanced users can rewrite the behavior by editing a readable program instead of rebuilding the system from scratch.`
