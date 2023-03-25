# Zank Media Player

This is a custom component for Home Assistant that allows you to control Zank Media Players.

## Features

- Control media playback (play, pause, stop, previous track, next track)
- Adjust volume (volume up, volume down, mute)
- Channel control (channel up, channel down)
- Additional remote control functionality

## Installation

### Via HACS

1. Open the Home Assistant web interface.
2. Click on "HACS" in the sidebar.
3. Click on "Integrations."
4. Click on the three dots in the upper right corner and choose "Custom repositories."
5. Enter the URL of this GitHub repository (e.g., `https://github.com/zimmra/zank_media_player`) and select "Integration" as the category.
6. Click "Add."
7. The custom component should now be available in HACS. Install it by clicking on it and then clicking "Install."

### Manual Installation

1. Clone or download this repository.
2. Copy the `zank_media_player` folder into the `custom_components` folder in your Home Assistant configuration directory.

## Configuration

This custom component uses the Home Assistant Integrations User Interface for configuration. After installation, follow these steps to set up the integration:

1. Open the Home Assistant web interface.
2. Click on "Configuration" in the sidebar.
3. Click on "Integrations."
4. Click on the "+" button in the lower right corner.
5. Search for "Zank Media Player" and click on it.
6. Enter the IP address and port of your Zank Media Player in the provided fields. The default port is 1028.
7. Click "Submit."

## Usage

Once the integration is configured, a new `media_player` entity will be created for your Zank Media Player. You can control the media player using Home Assistant's built-in media player controls or via automations and scripts.

For more advanced control, you can use the `media_player.send_command` service with the available commands.

## Available Commands

The following commands can be used with the `media_player.send_command` service:

- home
- back
- recent
- scrollUp
- scrollDown
- pageRight
- pageLeft
- volumeUp
- volumeDown
- volumeMute
- pageUp
- pageDown
- dpadUp
- dpadDown
- dpadLeft
- dpadRight
- dpadCenter
- dpadCenterLong
- openNotification
- takeScreenShot
- powerDialog
- lockScreen
- switchToTV
- mediaPrevious
- mediaNext
- mediaPlayPause
- channelUp
- channelDown
- fastRewind
- fastForward
- pressNumber (0-9)
- pressMenu
- keycodeGuide
- click
- longClick
