import sublime
import sublime_plugin
from typing import Dict, Any
import os
import json
import hashlib

class VolumeCommand(sublime_plugin.WindowCommand):

  index: int = 0

  cached_settings = None
  cache_settings_hash = None

  def run(self, **args):
    window = self.window

    if window:
      settings = args
      # TODO: Check for validity of settings structure
      # TODO: Support order (increase or decrease on each invocation)
      # TODO: Support boundary (rollover or stop)
      # TODO: Have separate cache setting per invocation. This would require a unique id per invocation.
      if settings:
        self.reload_settings_on_change(settings)

        commands = VolumeCommand.cached_settings['commands']
        commands_length = len(commands)
        temp_index = VolumeCommand.index if VolumeCommand.index < commands_length else 0

        command = commands[temp_index]
        window.run_command(command['command'], command['args'])

        VolumeCommand.index = (temp_index + 1) % commands_length
      else:
        self.show_error("Could not load volume.sublime-settings")
    else:
      self.show_error("No active window found")

  def reload_settings_on_change(self, settings: Dict[str, Any]) -> None:
    print(f"{settings}")
    settings_hash: str = self.get_settings_hash(settings)
    print(f"settings_hash: {settings_hash}")
    print(f"cache_settings_hash: {settings_hash}")

    if not (
        VolumeCommand.cached_settings and
        VolumeCommand.cache_settings_hash and
        VolumeCommand.cache_settings_hash == settings_hash):
      print(f"updating cache_settings")
      VolumeCommand.cached_settings = settings
      VolumeCommand.cache_settings_hash = settings_hash

  def get_settings_hash(self, settings: Dict[str, Any]) -> str:
     encoded_settings = json.dumps(settings, sort_keys = True).encode("utf-8")
     return hashlib.md5(encoded_settings).hexdigest()

  def show_info(self, message: str) -> None:
    sublime.message_dialog(message)

  def show_error(self, message: str) -> None:
    sublime.error_message(message)
