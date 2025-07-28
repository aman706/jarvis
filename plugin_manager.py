import os
import importlib.util

PLUGIN_FOLDER = "plugins"

def load_plugins():
    plugins = {}
    for filename in os.listdir(PLUGIN_FOLDER):
        if filename.endswith(".py"):
            plugin_name = filename[:-3]
            path = os.path.join(PLUGIN_FOLDER, filename)

            spec = importlib.util.spec_from_file_location(plugin_name, path)
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
                if hasattr(module, "run") and hasattr(module, "command"):
                    plugins[module.command.lower()] = module.run
            except Exception as e:
                print(f"[PLUGIN ERROR] {filename}: {e}")
    return plugins
