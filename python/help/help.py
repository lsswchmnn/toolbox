from cli_utils.display import print_heading, enter_continue
#=========================================================================
HELP_REGISTRY: dict[str, str] = {
    "key_1": (
        "help-string"
    ),
    "key_2": ("...")
}
#-------------------------------------------------------------------------

def print_help(key: str) -> None:
    text = HELP_REGISTRY.get(key)
    if text is None:
        raise KeyError(f"No help text registered for key: '{key}'")
    print_heading("HELP MENU")
    print(text)
    enter_continue()
