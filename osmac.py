from AppKit import NSWorkspace

workspace = NSWorkspace.sharedWorkspace()


def leage_of_legends_game_client_focused():
    """
    check if current focused app is league of legends game client
    """
    active_app = workspace.activeApplication()
    return active_app['NSApplicationBundleIdentifier'] == 'com.riotgames.LeagueofLegends.GameClient'
